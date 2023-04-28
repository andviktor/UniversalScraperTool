import functions.f_requests as f_requests
import functions.f_bs4 as f_bs
import functions.f_csv as f_csv
import functions.f_txt as f_txt
import re

def scrape_requests(attrs, report=False):
    """Get request and return html objects

        Params:
            attrs (dict):
                url (string) : scrape url
                headers (dict) : headers dict
                elements (list of dicts(name, xpath, regex) ) : xpath for elements
                    name - name of result
                    xpath - xpath for searching elements
                    regex_sub (optional) - re.sub - find and replace
                    regex_search (optional) - get match with regex
                    concat_results (optional) - concat results with character
                    example:
                    [
                        {
                            'name': 'links',
                            'xpath': '//a',
                            'regex_sub': [r'[a-zA-Z]', 'newstring'],
                            'regex_search': r'[a-zA-Z]',
                            'concat_results': ' | '
                        }
                    ]

        Return:
            list of elements objects
            example:
            [
                [
                    <object of div>,
                    <object of div>...
                ],
                [
                    <object of a>,
                    <object of a>...
                ]
            ]
            example 2:
            result[0][0].attrib['href'] - first result for the first xpath, get attribute 'href'
    """
    response = f_requests.get(attrs['url'], headers=attrs['headers'])
    soup = f_bs.set_soup(response)
    output = {}
    for xpath in attrs['elements']:
        result = f_bs.get_elements(soup, xpath['xpath'])
        if 'regex_sub' in xpath.keys():
            for i, res in enumerate(result):
                result[i] = re.sub(xpath['regex_sub'][0], xpath['regex_sub'][1], res)
        if 'regex_search' in xpath.keys():
            for i, res in enumerate(result):
                match = re.search(xpath['regex_search'], res)
                if match:
                    result[i] = match.group()
        if 'concat_results' in xpath.keys():
            result = xpath['concat_results'].join(result)
        if len(result) == 1:
            result = result[0]
        output[xpath['name']] = result
        if report:
            print('Collected - {} : {}'.format(xpath['name'],len(result) if isinstance(result, list) else 1))
    if report:
        print(output)
    return output

def main():

    # Input/Output filenames
    output_links = './output/links.csv'
    output = './output/output.csv'

    # Headers
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"

    # Scraping: get all links
    attrs = {
        'url': 'http://ns-maf.ru/catalog/kacheli',
        'headers': {
            'User-Agent': user_agent
            },
        'elements': [
            {
                'name': 'links',
                'xpath': '//div[contains(@class,"block-4 text-center border h-100")]/a'
            }
        ]
    }
    links = scrape_requests(attrs)['links']
    
    # Scraping: get every link page data
    attrs = {
        'headers': {
            'User-Agent': user_agent
            },
        'elements': [
            {
                'name': 'title',
                'xpath': '(//h1)[1]/text()'
            },
            {
                'name': 'sku',
                'xpath': '//p[@class="mb-2"]/text()'
            },
            {
                'name': 'price',
                'xpath': '(//div[@class="price"])[1]/text()[1]',
                'regex_sub': [r'\s', ''],
                'regex_search': r'[\d]+'
            },
            {
                'name': 'description',
                'xpath': '//div[@class="prod-description"]//*/text()',
                'concat_results': ' '
            },
            {
                'name': 'images',
                'xpath': '//a[@class="image-popup"]/@href',
                'concat_results': ','
            }
        ]
    }
    csv_header = [
        'title',
        'sku',
        'price',
        'description',
        'images'
    ]
    links_done = f_txt.read_file_txt(output_links)
    for link in links:
        if not link.attrib['href'] in links_done:
            try:
                attrs['url'] = link.attrib['href']
                elements = scrape_requests(attrs, report=False)
                f_csv.write_dict_row_csv(output, csv_header, elements)
                f_txt.write_row_txt(output_links, link.attrib['href'], mode='a')
            except:
                print('Error: ' + link.attrib['href'])

if __name__ == '__main__':
    main()
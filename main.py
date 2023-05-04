import functions.formats.f_csv as f_csv
import functions.formats.f_txt as f_txt

import functions.modules.m_thread as m_thread
import functions.modules.m_headers as m_headers

import functions.scrapers.s_requests as s_requests

import time

def main():

    ### Start time
    start_time = time.time()
    errors = 0
    pagenotfound = 0

    ### concurrency
    concurrency = 20

    ### Input/Output filenames
    input_tasks = './input/tasks.txt'
    output_links = './output/links.txt'
    output = './output/output.csv'

    ### Scraping: get categories links
    attrs = {
        'url': 'http://ns-maf.ru/',
        'headers': m_headers.get_random_header(),
        'elements': [
            {
                'name': 'links',
                'xpath': '//ul[contains(@class,"site-menu")][1]//ul[@class="dropdown"]//a/@href'
            }
        ]
    }
    categories = s_requests.scrape_requests(attrs)['links']
    
    ### Scraping: get all links
    def scrape_category(link):
        attrs = {
            'url': link,
            'headers': m_headers.get_random_header(),
            'elements': [
                {
                    'name': 'links',
                    'xpath': '//div[contains(@class,"block-4 text-center border h-100")]/a/@href'
                }
            ]
        }
        links = s_requests.scrape_requests(attrs)['links']
        f_txt.write_txt(input_tasks, links, mode='a')
    m_thread.create_pool(scrape_category, categories, concurrency)

    ### Scraping (Pool task): get every link page data
    def scrape_link(link):
        nonlocal errors, pagenotfound
        if not link in links_done:
            try:
                attrs['url'] = link
                elements = s_requests.scrape_requests(attrs, report=False)
                if elements != 404:
                    f_csv.write_dict_row_csv(output, csv_header, elements)
                    f_txt.write_txt(output_links, link, mode='a')
                else:
                    pagenotfound += 1
            except:
                print('Error: ' + link)
                errors += 1
    
    links = f_txt.read_file_txt(input_tasks)
    attrs = {
        'headers': m_headers.get_random_header(),
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
    m_thread.create_pool(scrape_link, links, concurrency)

    print('Completed, total time is: '+str(time.time() - start_time))
    print('Errors: '+str(errors))
    print('404: '+str(pagenotfound))

if __name__ == '__main__':
    main()
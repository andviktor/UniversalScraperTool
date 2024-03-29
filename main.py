from classes.Timer import Timer
from classes.ImportExport import ImportExportTxt, ImportExportCsv
from classes.Headers import Headers
from classes.Thread import Thread
from classes.Scraper import ScraperRequests

def main():

    ### Init scraper
    scraper_requests = ScraperRequests()

    ### Start time
    total_timer = Timer('Total time')
    errors = 0
    pagenotfound = 0

    ### concurrency
    concurrency = 20

    ### Input/Output filenames
    input_tasks = './input/tasks.txt'
    output_links = './output/links.txt'
    output = './output/output.csv'

    ### Input/output objects
    io_input_tasks = ImportExportTxt(input_tasks)
    io_output_links = ImportExportTxt(output_links)
    io_output = ImportExportCsv(output)

    ### Headers
    headers = Headers('./headers/headers.json')

    ### Scraping: get categories links
    attrs = {
        'url': 'http://mywebsite.com/',
        'headers': headers.get_random(),
        'elements': [
            {
                'name': 'links',
                'xpath': '//ul[contains(@class,"site-menu")][1]//ul[@class="dropdown"]//a/@href'
            }
        ]
    }
    categories = scraper_requests.scrape(attrs)['links']
    
    ### Scraping: get all links
    def scrape_category(link):
        attrs = {
            'url': link,
            'headers': headers.get_random(),
            'elements': [
                {
                    'name': 'links',
                    'xpath': '//div[contains(@class,"block-4 text-center border h-100")]/a/@href'
                }
            ]
        }
        links = scraper_requests.scrape(attrs)['links']
        io_input_tasks.write(links, mode='a')

    def test_func(value):
        print('value: #' + str(value))

    thread = Thread(scrape_category, categories, concurrency)
    thread.set_delay(0.3)
    thread.run()

    ### Scraping (Pool task): get every link page data
    def scrape_link(link):
        nonlocal errors, pagenotfound
        if not link in links_done:
            try:
                attrs['url'] = link
                elements = scraper_requests.scrape(attrs, report=False)
                if elements != 404:
                    io_output.write(csv_header, elements)
                    io_output_links.write(link, mode='a')
                else:
                    pagenotfound += 1
            except:
                print('Error: ' + link)
                errors += 1
    
    links = io_input_tasks.read()
    attrs = {
        'headers': headers.get_random(),
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
    links_done = io_output_links.read()
    thread = Thread(scrape_link, links, concurrency)
    thread.set_delay(2)
    thread.run()

    total_timer.check_time()
    print('Errors: '+str(errors))
    print('404: '+str(pagenotfound))

if __name__ == '__main__':
    main()

from classes.Soup import Soup

import functions.modules.m_requests as f_requests
import re

def scrape_requests(attrs, report=False):
    """Gets request and returns html objects

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
    if 'cookies' in attrs:
        cookies = attrs['cookies']
    else:
        cookies = ''
    response = f_requests.get(attrs['url'], headers=attrs['headers'], cookies=cookies)
    if response.status_code == 404:
        print('404 error - {}'.format(attrs['url']))
        return 404
    soup = Soup(response)
    output = {}
    for xpath in attrs['elements']:
        result = soup.get_elements(xpath['xpath'])
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
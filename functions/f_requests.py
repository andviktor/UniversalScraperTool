import requests
import re

def get(url, headers):
    """Get request to the url and return response with print log message

        Params:
        url (str) - any url
        headers (dict) - headers dictionary

            example:

            'headers': {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
                }

        Return:
            response of the request or False

    """
    try:
        response = requests.get(url, headers)
        print('{}: {}'.format(response.status_code, url))
        return response
    except:
        print('Error get url: ' + url)
        return False

def download_file(url, dir, filename=''):
    """Downloads a file from url

        Params:
        url (str) - any url to a file to download
        dir (str) - a path on a server, where to save a file
        filename (str, optional) - name of a new file without extension
            if empty - a file will be saved with an original name
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            url_parts = re.search(r'(.*/)([^?]*)(.*)', url)
            if url_parts.group(2) != '':
                if filename == '': filename = url_parts.group(2)
                else: filename = filename + '.' + url_parts.group(2).split('.')[-1]
            open(dir + filename, "wb").write(response.content)
    except:
        print('Error download file: ' + url)
        return False
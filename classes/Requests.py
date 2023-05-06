import requests
import re

class Requests:
    """Requests operations with URL
    """
    def __init__(self, url):
        self._url = url

    def set_url(self, url):
        """Set URL
        """
        self._url = url

    def get(self, headers, cookies=''):
        """Get request to the url and return response with print log message

            Params:
            headers (dict) - headers dictionary

                example:

                'headers': {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
                    }
            
            cookies (dict) - cookies dictionary

            Return:
                response of the request or False

        """
        try:
            response = requests.get(self._url, headers=headers, cookies=cookies)
            print('{}: {}'.format(response.status_code, self._url))
            return response
        except:
            print('Error get url: ' + self._url)
            return False

    def download_file(self, dir, filename=''):
        """Downloads a file from url

            Params:
            dir (str) - a path on a server, where to save a file
            filename (str, optional) - name of a new file without extension
                if empty - a file will be saved with an original name
        """
        try:
            response = requests.get(self._url)
            if response.status_code == 200:
                url_parts = re.search(r'(.*/)([^?]*)(.*)', self._url)
                if url_parts.group(2) != '':
                    if filename == '': filename = url_parts.group(2)
                    else: filename = filename + '.' + url_parts.group(2).split('.')[-1]
                open(dir + filename, "wb").write(response.content)
        except:
            print('Error download file: ' + self._url)
            return False
        
    def auth_post(self, data):
        """Posts request to an auth form and returns cookies

            Params:
            data (dict) - data dictionary for a post request

            Return:
            returns cookies dictionary.

            Example:
            url = 'https://www.pakwheels.com/login-with-email'
            data = {
                'username': 'myuser',
                'password': '123pass'
            }
            cookies = m_requests.auth_post(url, data)

        """
        response = requests.post(self._url, data=data)
        return response.cookies
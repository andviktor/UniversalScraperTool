import requests

def get(url, headers):
    try:
        response = requests.get(url, headers)
        print('{}: {}'.format(response.status_code, url))
        return response
    except:
        return False
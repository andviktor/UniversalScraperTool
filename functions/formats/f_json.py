import json

def print_json(json_object):
    """Print JSON pretty

        Params:
        json_object (dict) - JSON dictionary, can be result of requests.get(...).json()
            example:
                response = f_requests.get(url, headers).json()
                print(response)

    """
    json_formatted_str = json.dumps(json_object, indent=2)
    print(json_formatted_str)

def read_json(filename):
    """Reads JSON file to dictionary

        Params:
        filename (str) - local path to a .JSON file

        Return: JSON dictionary as object
    """
    with open(filename) as json_file:
        return json.load(json_file)
    
def write_json(filename, dict, mode='a'):
    """Writes JSON dictionary to file

        Params: 
        filename (str) - local path to save a file,
        dict (dict) - a dictionary with data,
        mode (str, optional) - write mode, default 'a'

    """
    with open(filename, mode) as outfile:
        json.dump(dict, outfile)
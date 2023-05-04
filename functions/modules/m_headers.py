import functions.formats.f_json as f_json
import random

def get_random_header(filename='./headers/headers.json'):
    """Returns a random headers dictionary

        Params:
        filename (str, optional) - path to a json file with headers list, default './headers/headers.json'

    """
    headers_list = f_json.read_json(filename)
    return random.choice(headers_list)
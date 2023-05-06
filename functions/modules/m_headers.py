from classes.ImportExport import ImportExportJson
import random

def get_random_header(filename='./headers/headers.json'):
    """Returns a random headers dictionary

        Params:
        filename (str, optional) - path to a json file with headers list, default './headers/headers.json'

    """
    json_file = ImportExportJson(filename)
    headers_list = json_file.read()
    return random.choice(headers_list)
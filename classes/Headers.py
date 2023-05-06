from classes.ImportExport import ImportExportJson
import random

class Headers:
    """Headers for requests
    """
    def __init__(self, filename='./headers/headers.json'):
        self.filename = filename

    def get_random(self, filename=None):
        """Returns a random headers dictionary

            Params:
            filename (str, optional) - path to a json file with headers list, default self.filename

        """
        if filename is None:
            filename = self.filename
        json_file = ImportExportJson(filename)
        headers_list = json_file.read()
        return random.choice(headers_list)
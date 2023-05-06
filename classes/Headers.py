from classes.ImportExport import ImportExportJson
import random

class Headers:
    """Headers for requests

        Params:
        filename (str) - path to a json file with headers
    """
    def __init__(self, filename):
        self._filename = filename

    def set_filename(self, filename):
        """Set filename
        """
        try:
            open(filename, 'r')
            self._filename = filename
        except Exception:
            raise

    def get_random(self):
        """Returns a random headers dictionary
        """
        json_file = ImportExportJson(self._filename)
        headers_list = json_file.read()
        return random.choice(headers_list)
import csv
import json

class ImportExportTxt:
    """Reads and writes *.txt files

        Params:
        filename (str) - path to a TXT file
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

    def read(self):
        """Returns a content of a TXT file
        """
        output = []
        try:
            with open(self._filename, 'r', encoding='utf8') as file:
                for line in file: output.append(line.replace('\n',''))
            return output
        except Exception:
            raise
    
    def write(self, rows, mode='a'):
        """Write any string or list to a txt file

            Params:
            rows (str or list) - content to write to a file
            mode (str, optional) - file open mode, default 'a'
            encoding (str, optional) - encoding, default 'utf-8'
        """
        try:
            with open(self._filename, mode, encoding='utf-8') as file:
                if not isinstance(rows, list): rows = [rows]
                for row in rows: file.write(str(row) + '\n')
        except Exception:
            raise

class ImportExportCsv:
    """Reads and writes *.csv files

        Params:
        filename (str) - path to a CSV file
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

    def read(self):
        """Read a CSV file to a dictionary

            Return:
            a list of dictionaries.
            example:
            [
                {'first':1, 'second':2, 'third':3},
                {'first':6, 'second':7, 'third':8},
            ]
        """
        try:
            with open(self._filename, 'r') as f:
                dict_reader = csv.DictReader(f)
                result = list(dict_reader)
                return result
        except Exception:
            raise

    def write(self, header, dict):
        """Write dictionary to CSV file as a row

            Params:
            filename (str) - path and name of a CSV file
            header (list) - a list of columns names
                example:
                csv_header = [
                    'title',
                    'sku',
                    'price',
                    'description'
                ]
            dict (dict) - a dictionary with data
                example:
                data = {
                    'title': 'Hello world',
                    'sku': '0001',
                    'price': '1000$',
                    'description': 'An example row'
                }
        """
        try:
            open(self._filename, 'a', encoding='utf8')
            filelen = sum(1 for line in open(self._filename, 'r', encoding='utf8'))
            if not isinstance(dict, list):
                dict = [dict]
            with open(self._filename, 'a', encoding='utf8', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = header, delimiter=';')
                if filelen == 0: writer.writeheader()
                writer.writerows(dict)
        except Exception:
            raise

class ImportExportJson:
    """Reads and writes *.json files

        Params:
        filename (str) - path to a JSON file
    """
    def __init__(self, filename=None):
        self._filename = filename

    def set_filename(self, filename):
        """Set filename
        """
        try:
            open(filename, 'r')
            self._filename = filename
        except Exception:
            raise

    def print(self, json_object):
        """Print JSON pretty

            Params:
            json_object (dict) - JSON dictionary, can be result of requests.get(...).json()
                example:
                    response = f_requests.get(url, headers).json()
                    print(response)

            Return:
            formatted JSON

        """
        try:
            json_formatted_str = json.dumps(json_object, indent=2)
            print(json_formatted_str)
            return json_formatted_str
        except Exception:
            raise

    def read(self):
        """Reads JSON file to dictionary

            Return: JSON dictionary as object
        """
        try:
            with open(self._filename) as json_file:
                return json.load(json_file)
        except Exception:
            raise
        
    def write(self, dict, mode='a'):
        """Writes JSON dictionary to file

            Params:
            dict (dict) - a dictionary with data,
            mode (str, optional) - write mode, default 'a'

        """
        try:
            with open(self._filename, mode) as outfile:
                json.dump(dict, outfile)
        except Exception:
            raise
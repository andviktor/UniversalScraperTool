import csv
import json

class ImportExportTxt:
    """Reads and writes *.txt files
    """
    def __init__(self, filename=None):
        if not filename is None:
            self.filename = filename

    def read(self, filename=None):
        """Returns a content of a TXT file
        """
        if filename is None:
            filename = self.filename
        output = []
        try:
            with open(filename, 'r', encoding='utf8') as file:
                for line in file: output.append(line.replace('\n',''))
            return output
        except Exception:
            raise
    
    def write(self, rows, filename=None, mode='a'):
        """Write any string or list to a txt file

            Params:
            rows (str or list) - content to write to a file
            filename (str, optional) - path to a file, if None or empty, will use self.filename
            mode (str, optional) - file open mode, default 'a'
        """
        if filename is None:
            filename = self.filename
        try:
            with open(filename, mode, encoding='utf8') as file:
                if not isinstance(rows, list): rows = [rows]
                for row in rows: file.write(str(row) + '\n')
        except Exception:
            raise

class ImportExportCsv:
    """Reads and writes *.csv files
    """
    def __init__(self, filename=None):
        if not filename is None:
            self.filename = filename

    def read(self, filename=None):
        """Read a CSV file to a dictionary

            Params:
            filename (str) - a path to a CSV file

            Return:
            a list of dictionaries.
            example:
            [
                {'first':1, 'second':2, 'third':3},
                {'first':6, 'second':7, 'third':8},
            ]
        """
        if filename is None:
            filename = self.filename
        try:
            with open(filename, 'r') as f:
                dict_reader = csv.DictReader(f)
                result = list(dict_reader)
                return result
        except Exception:
            raise

    def write(self, header, dict, filename=None):
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
        if filename is None:
            filename = self.filename
        try:
            open(filename, 'a', encoding='utf8')
            filelen = sum(1 for line in open(filename, 'r', encoding='utf8'))
            if not isinstance(dict, list):
                dict = [dict]
            with open(filename, 'a', encoding='utf8', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = header, delimiter=';')
                if filelen == 0: writer.writeheader()
                writer.writerows(dict)
        except Exception:
            raise

class ImportExportJson:
    """Reads and writes *.json files
    """
    def __init__(self, filename=None):
        if not filename is None:
            self.filename = filename

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

    def read(self, filename=None):
        """Reads JSON file to dictionary

            Params:
            filename (str) - local path to a .JSON file

            Return: JSON dictionary as object
        """
        if filename is None:
            filename = self.filename
        try:
            with open(filename) as json_file:
                return json.load(json_file)
        except Exception:
            raise
        
    def write(self, dict, filename=None, mode='a'):
        """Writes JSON dictionary to file

            Params: 
            filename (str) - local path to save a file,
            dict (dict) - a dictionary with data,
            mode (str, optional) - write mode, default 'a'

        """
        if filename is None:
            filename = self.filename
        try:
            with open(filename, mode) as outfile:
                json.dump(dict, outfile)
        except Exception:
            raise
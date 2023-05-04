import csv

def write_dict_row_csv(filename, header, dict):
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
    open(filename, 'a', encoding='utf8')
    filelen = sum(1 for line in open(filename, 'r', encoding='utf8'))
    if not isinstance(dict, list):
        dict = [dict]
    with open(filename, 'a', encoding='utf8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = header, delimiter=';')
        if filelen == 0: writer.writeheader()
        writer.writerows(dict)

def read_csv_to_dict(filename):
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
    with open(filename, 'r') as f:
        dict_reader = csv.DictReader(f)
        result = list(dict_reader)
        return result
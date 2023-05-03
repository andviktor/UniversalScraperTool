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
    filelen = sum(1 for line in open(filename, 'r', encoding='utf8'))
    if not isinstance(dict, list):
        dict = [dict]
    with open(filename, 'a', encoding='utf8',newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = header, delimiter=';')
        if filelen == 0: writer.writeheader()
        writer.writerows(dict)
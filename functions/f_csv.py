import csv

def write_dict_row_csv(filename, header, dict):
    filelen = sum(1 for line in open(filename, 'r'))
    if not isinstance(dict, list):
        dict = [dict]
    with open(filename, 'a', encoding='utf-8-sig',newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = header, delimiter=';')
        if filelen == 0:
            writer.writeheader()
        writer.writerows(dict)
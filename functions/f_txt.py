def read_file_txt(filename):
    """Returns a content of a TXT file
    """
    output = []
    with open(filename, 'r', encoding='utf8') as file:
        for line in file: output.append(line.replace('\n',''))
    return output

def write_txt(filename, rows, mode='a'):
    """Write any string or list to a txt file

        Params:
        filename (str) - path to a file
        rows (str or list) - content to write to a file
        mode (str, optional) - file open mode, default 'a'
    """
    with open(filename, mode, encoding='utf8') as file:
        if not isinstance(rows, list): rows = [rows]
        for row in rows: file.write(str(row) + '\n')
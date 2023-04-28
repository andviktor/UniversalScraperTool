def read_file_txt(filename):
    output = []
    with open(filename, 'r', encoding='utf8') as file:
        for line in file:
            output.append(line.replace('\n',''))
    return output

def write_txt(filename, rows, mode='a'):
    with open(filename, mode, encoding='utf8') as file:
        if not isinstance(rows, list):
            rows = [rows]
        for row in rows:
            file.write(str(row) + '\n')
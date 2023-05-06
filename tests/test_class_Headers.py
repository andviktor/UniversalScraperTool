from classes.ImportExport import ImportExportJson
from classes.Headers import Headers

import os

def test_get_random_headers():

    filename = './tests/tmp_files/test_headers_tmp.json'
    open(filename, 'w')
    json_file = ImportExportJson(filename)
    os.remove(filename)
    assert json_file._filename == filename

    filename = './tests/tmp_files/test_headers.json'
    open(filename, 'w')
    json_file.set_filename(filename)
    os.remove(filename)
    assert json_file._filename == filename

    test_data = [
        {
            'header': 'x'
        },
        {
            'header': 'y'
        }
    ]
    json_file.write(test_data, mode='w')

    headers = Headers(filename)
    result = ''
    for i in range(100):
        result += headers.get_random()['header']
    os.remove(filename)
    assert 'x' in result and 'y' in result
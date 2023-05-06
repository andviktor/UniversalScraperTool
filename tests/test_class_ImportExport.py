from classes.ImportExport import ImportExportTxt, ImportExportCsv, ImportExportJson
from classes.String import String

import os, json

def test_write_read_txt():
    filename = './tests/tmp_files/test_write_read_txt.txt'
    txt_file = ImportExportTxt(filename)
    input_data_1 = 'Test write and read txt file.'
    input_data_2 = ['Test write','read txt file.']
    txt_file.write(input_data_1, mode='w')
    result_1 = txt_file.read()
    txt_file.write(input_data_2, mode='w')
    result_2 = txt_file.read()
    os.remove(filename)
    assert result_1 == ['Test write and read txt file.'] and result_2 == ['Test write', 'read txt file.']

def test_write_read_csv():
    filename = './tests/tmp_files/test_write_read_dict_row_csv.csv'
    csv_file = ImportExportCsv(filename)
    expected_result = [{'first;second;third': '1;2;3'}]
    open(filename, 'w', encoding='utf8')
    input_header = ['first','second','third']
    input_data = {
        'first': 1,
        'second': 2,
        'third': 3
    }
    csv_file.write(input_header, input_data)
    result = csv_file.read(filename)
    os.remove(filename)
    assert result == expected_result

def test_print_json():
    json_object = ImportExportJson()
    input_dict = {
        'first': 1,
        'second': [
            {
                'second_1': 2
            }
        ],
        'third': {
            'third_1': 3
        }
    }
    result = json.loads(json_object.print(input_dict))
    assert result['first'] == 1 and result['second'][0]['second_1'] == 2 and result['third']['third_1'] == 3

def test_write_read_json():
    filename = './tests/tmp_files/test_write_read_dict_json.json'
    json_file = ImportExportJson(filename)
    input_dict = {
        'first': 1,
        'second': 2,
        'third': 3
    }
    json_file.write(input_dict, mode='w')
    result = json_file.read()
    os.remove(filename)
    assert input_dict == result

def test_get_url_parts_str():
    url = 'https://test123.com/dir/file_русский.moredot.pdf?attr1=1&attr2=2'
    string = String(url)
    result_1 = string.get_url_parts(params_list=False)
    result_2 = string.get_url_parts(params_list=True)
    assert result_1['dir'] == result_2['dir'] == 'https://test123.com/dir/' and result_1['filename'] == result_2['filename'] == 'file_русский.moredot.pdf' and result_1['params'] == '?attr1=1&attr2=2' and result_2['params'] == [['attr1', '1'], ['attr2', '2']]
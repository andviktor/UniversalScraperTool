import functions.formats.f_csv as f_csv
import functions.formats.f_json as f_json
import functions.formats.f_str as f_str
import functions.formats.f_txt as f_txt

import os, json

def test_write_read_dict_csv():
    expected_result = [{'first;second;third': '1;2;3'}]
    filename = './tests/tmp_files/test_write_read_dict_row_csv.csv'
    open(filename, 'w', encoding='utf8')
    input_header = ['first','second','third']
    input_data = {
        'first': 1,
        'second': 2,
        'third': 3
    }
    f_csv.write_dict_row_csv(filename, input_header, input_data)
    result = f_csv.read_csv_to_dict(filename)
    os.remove(filename)
    assert result == expected_result

def test_print_json():
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
    result = json.loads(f_json.print_json(input_dict))
    assert result['first'] == 1 and result['second'][0]['second_1'] == 2 and result['third']['third_1'] == 3

def test_write_read_json():
    filename = './tests/tmp_files/test_write_read_dict_json.json'
    input_dict = {
        'first': 1,
        'second': 2,
        'third': 3
    }
    f_json.write_json(filename, input_dict, mode='w')
    result = f_json.read_json(filename)
    os.remove(filename)
    assert input_dict == result

def test_get_url_parts_str():
    url = 'https://test123.com/dir/file_русский.moredot.pdf?attr1=1&attr2=2'
    result_1 = f_str.get_url_parts(url, params_list=False)
    result_2 = f_str.get_url_parts(url, params_list=True)
    assert result_1['dir'] == result_2['dir'] == 'https://test123.com/dir/' and result_1['filename'] == result_2['filename'] == 'file_русский.moredot.pdf' and result_1['params'] == '?attr1=1&attr2=2' and result_2['params'] == [['attr1', '1'], ['attr2', '2']]

def test_write_read_txt():
    filename = './tests/tmp_files/test_write_read_txt.txt'
    input_data_1 = 'Test write and read txt file.'
    input_data_2 = ['Test write','read txt file.']
    f_txt.write_txt(filename, input_data_1, mode='w')
    result_1 = f_txt.read_file_txt(filename)
    f_txt.write_txt(filename, input_data_2, mode='w')
    result_2 = f_txt.read_file_txt(filename)
    os.remove(filename)
    assert result_1 == ['Test write and read txt file.'] and result_2 == ['Test write', 'read txt file.']



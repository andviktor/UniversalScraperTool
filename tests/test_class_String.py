from classes.String import String

def test_get_url_parts_str():
    url = 'https://test123.com/dir/file_русский.moredot.pdf?attr1=1&attr2=2'
    string = String(url)
    result_1 = string.get_url_parts(params_list=False)
    result_2 = string.get_url_parts(params_list=True)
    assert result_1['dir'] == result_2['dir'] == 'https://test123.com/dir/' and result_1['filename'] == result_2['filename'] == 'file_русский.moredot.pdf' and result_1['params'] == '?attr1=1&attr2=2' and result_2['params'] == [['attr1', '1'], ['attr2', '2']]
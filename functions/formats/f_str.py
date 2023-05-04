import re

def get_url_parts(url, params_list=False):
    """Get parts of url

        Params:
        url (str) - any URL (example: https://testsite.com/folder/subfolder/Test-Name.pdf?testparam1=123123&testparam2=sjdkfjsd)
        params_list (bool) - if TRUE returns URL params in the list format

        Example:
        print(f_str.get_url_parts('https://testsite.com/folder/subfolder/Tes.tF_фil.e-Name.pdf?testparam1=123123&testparam2=sjdkfjsd', params_list=True))

        Result:
        {
            'dir': 'https://testsite.com/folder/subfolder/',
            'filename': 'Tes.tF_фil.e-Name.pdf',
            'params': [
                [
                    'testparam1',
                    '123123'
                ],
                [
                    'testparam2',
                    'sjdkfjsd'
                ]
            ]
        }
    """
    try:
        output = {}
        filename = re.search(r'(.*/)([^?]*)(.*)', url)
        if filename.group(1) != '': output['dir'] = filename.group(1)
        if filename.group(2) != '': output['filename'] = filename.group(2)
        if not params_list:
            if filename.group(3) != '': output['params'] = filename.group(3)
        elif params_list:
            if filename.group(3) != '': output['params'] = [param.split('=') for param in filename.group(3)[1:].split('&')]
        return output
    except:
        print('Get filename from url error! Url: ' + url)
        return False
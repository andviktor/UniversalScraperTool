import re

class String:
    """String operations
    """
    def __init__(self, string):
        self._string = string

    def set_string(self, string):
        """Set string
        """
        self._string = string

    def get_url_parts(self, params_list=False):
        """Get parts of url

            Params:
            params_list (bool) - if TRUE returns URL params in the list format

            Example:
            string = String('https://testsite.com/folder/subfolder/Tes.tF_фil.e-Name.pdf?testparam1=123123&testparam2=sjdkfjsd')
            print(string.get_url_parts(params_list=True))

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
            filename = re.search(r'(.*/)([^?]*)(.*)', self._string)
            if filename.group(1) != '': output['dir'] = filename.group(1)
            if filename.group(2) != '': output['filename'] = filename.group(2)
            if not params_list:
                if filename.group(3) != '': output['params'] = filename.group(3)
            elif params_list:
                if filename.group(3) != '': output['params'] = [param.split('=') for param in filename.group(3)[1:].split('&')]
            return output
        except Exception:
            raise
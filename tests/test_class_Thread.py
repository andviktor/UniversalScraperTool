from classes.ImportExport import ImportExportJson

import timeit
import os

def test_thread():

    filename = './tests/tmp_files/test_thread.json'
    json_file = ImportExportJson(filename)
    input_dict = {
        'first': 1,
        'second': 2,
        'third': 3
    }

    def func(i):
        nonlocal json_file
        json_file.write(input_dict, mode='w')
        

    data = range(1000)

    time_1 = timeit.timeit('Thread(func, data, 1)', number=5, setup="from classes.Thread import Thread", globals={'func': func, 'data': data})
    time_2 = timeit.timeit('Thread(func, data, 20)', number=5, setup="from classes.Thread import Thread", globals={'func': func, 'data': data})

    os.remove(filename)

    print('Concurrency 1: ' + str(time_1))
    print('Concurrency 2: ' + str(time_2))
    assert time_1/time_2 > 1.4
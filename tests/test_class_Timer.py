from classes.Timer import Timer

import time

def test_timer():
    timer = Timer('test')
    time.sleep(2)
    timer.reset_timer()
    time.sleep(2)
    assert round(timer.check_time()) == 2
    assert timer._format_time(5000) == '1h 23m 20s'


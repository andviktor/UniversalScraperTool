import time

class Timer:
    """A timer that allows you to track the execution time of a section of code

        Methods:
        __init__ (name: str='Timer') - creates a timer with name 'name'

        _format_time (time_in_seconds: float) - formats time in seconds to a human friendly format

        reset_timer - set current time as start time
        
        check_time (message: str=None) - returns (and prints) the difference between start time and current time in seconds.
                If no message is specified, displays the name of the timer
                
                Example:
                    ExecTime.check_time('Total time')
                    Result:
                    Total time: 35.0s

    """
    def __init__(self, name: str='Timer'):
        self.name = name
        self.reset_timer()
        print('{}: timer initialized.'.format(self.name))

    def _format_time(self, time_in_seconds: float):
        time_in_seconds = round(time_in_seconds, 2)
        total_time = ''
        hours = int(time_in_seconds // 3600)
        minutes = int((time_in_seconds%3600) // 60)
        seconds = int((time_in_seconds%3600) % 60)
        if hours:
            total_time += str(hours) + 'h '
        if minutes:
            total_time += str(minutes) + 'm '
        if seconds:
            total_time += str(seconds) + 's'
        return total_time

    def reset_timer(self):
        self._start_time = time.time()

    def check_time(self, message: str=None):
        if not message:
            message = self.name
        formatted_time = self._format_time(time.time() - self._start_time)
        print(message + ': ' + formatted_time)
        return time.time() - self._start_time
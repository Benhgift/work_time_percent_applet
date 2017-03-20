import config
from datetime import datetime


class WorkPercent:
    def __init__(self, work_start, work_end):
        self.work_start = 60 * 60 * work_start
        self.work_end = 60 * 60 * work_end
        self.seconds_in_day = 60 * 60 * 24
        self.special_midnight_crossing_case = False
        if self.work_start > self.work_end:
            self.special_midnight_crossing_case = True
            self.seconds_in_work_day = self.seconds_in_day - self.work_start
            self.seconds_in_work_day += self.work_end
        else:
            self.seconds_in_work_day = self.work_end - self.work_start

    def _special_midnight_wrapping_percent(self, current_seconds):
        if current_seconds >= self.work_start or current_seconds < self.work_end:
            if current_seconds >= self.work_start: 
                total = current_seconds - self.work_start
            else:
                total = self.seconds_in_day - self.work_start
                total += current_seconds
            return (total/self.seconds_in_work_day) * 100
        else:
            return 0

    def work_percent(self):
        now = datetime.now()
        start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
        seconds = (now - start_of_day).seconds
        # if it's the special midnight crossing case
        if self.special_midnight_crossing_case:
            return self._special_midnight_wrapping_percent(seconds)
        if seconds <= self.work_start:
            return 0
        elif seconds >= self.work_end:
            return 100
        else:
            seconds_since_work = seconds - self.work_start
            return (seconds_since_work/self.seconds_in_work_day) * 100

    def update_ui_number(self, indicator):
        display_string = '%.{}f'.format(config.decimal_places)
        display_string = display_string % self.work_percent() + '%'
        indicator.set_label(display_string, 'work time percent')
        return True

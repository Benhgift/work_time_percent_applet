import config
from datetime import datetime, timedelta, date
import time


class WorkPercent:
    def __init__(self, work_start, work_end):
        # Determine start and end times.
        self.work_start = float(work_start)
        self.work_end = float(work_end)
        self.work_start_int = int(work_start)
        self.work_end_int = int(work_end)
        # Break up each start and end time into hours, minutes, seconds.
        self.start_hours = int(self.work_start)
        self.start_added_mins = int((self.work_start % 1) * 60)
        self.start_minutes = (self.work_start_int * 60) % 60
        self.start_minutes = self.start_minutes + self.start_added_mins
        self.start_seconds = (self.work_start_int * 3600) % 60
        self.work_start = datetime.now().replace(hour=self.start_hours, minute=self.start_minutes, second=self.start_seconds, microsecond=0)
        self.end_hours = int(self.work_end)
        self.end_added_mins = int((self.work_end % 1) * 60)
        self.end_minutes = (self.work_end_int * 60) % 60
        self.end_minutes = self.end_minutes + self.end_added_mins
        self.end_seconds = (self.work_end_int * 3600) % 60
        if (work_end == 24):
            self.work_end = datetime.now() + timedelta(days=1)
            self.work_end = self.work_end.replace(hour=0, minute=0, second=0, microsecond=0)
        else:
            self.work_end = datetime.now().replace(hour=self.end_hours, minute=self.end_minutes, second=self.end_seconds, microsecond=0)

    def work_percent(self):
        # If start time is later than end time, add 24 hours (1 day).
        if self.work_start > self.work_end:
            self.work_end = self.work_end + timedelta(hours=24)
        # Calculate total work time (in minutes).
        self.total_added_mins = self.start_added_mins + self.end_added_mins
        self.work_total_time = ((self.work_end - self.work_start).total_seconds() / 60) + self.total_added_mins
        # Get current time and separate it into hours, minutes, seconds.
        self.work_progress = datetime.now()
        self.hours = float(self.work_progress.strftime('%H'))
        self.minutes = float(self.work_progress.strftime('%M'))
        self.seconds = float(self.work_progress.strftime('%S'))
        # If time is past start time, return 100%.
        if self.hours >= self.end_hours and self.minutes >= self.end_minutes:
            self.work_percentage = 100.0
            return self.work_percentage
        if self.start_hours <= self.hours and self.start_minutes <= self.minutes:
            # Calculate current time since work start (in minutes).
            self.work_progress = ((self.hours - self.start_hours) * 60 ) + (self.minutes) + (self.seconds / 60)
            # Calculate percentage and return.
            self.work_percentage = (self.work_progress / self.work_total_time) * 100
            self.printDebug(False)
            return self.work_percentage
        else:
            # Else return 0%.
            self.work_percentage = 0.0
            return self.work_percentage

    def update_ui_number(self, indicator):
        display_string = '%.{}f'.format(config.decimal_places)
        display_string = display_string % self.work_percent() + '%'
        indicator.set_label(display_string, 'work time percent')
        return True

    def printDebug(self, enabled):
        if enabled:
            print('---- DEBUG ----')
            print('Start Time: %s' % (self.work_start))
            print('End Time: %s' % (self.work_end))
            print('Total Work Time (minutes): %s' % (self.work_total_time))
            print('Current Hours: %s' % (self.hours))
            print('Current Minutes: %s' % (self.minutes))
            print('Current Seconds: %s' % (self.seconds))
            print('Current Minutes Progressed: %s' % (self.work_progress))
            print('Current Percentage: %s' % (self.work_percentage))
            print('\n')

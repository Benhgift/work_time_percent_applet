from datetime import datetime


class WorkPercent:
    def __init__(self, work_start, work_end):
        self.work_start = 60 * 60 * work_start
        self.work_end = 60 * 60 * work_end
        self.seconds_in_work_day = self.work_end - self.work_start

    def work_percent(self):
        now = datetime.now()
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        seconds = (now - midnight).seconds
        if seconds <= self.work_start:
            return 0
        elif seconds >= self.work_end:
            return 100
        else:
            seconds_since_work = seconds - self.work_start
            return (seconds_since_work/self.seconds_in_work_day) * 100

    def update_ui_number(self, indicator):
        indicator.set_label('%.3f' % self.work_percent() + '%', 'work time percent')
        return True

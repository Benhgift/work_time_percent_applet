from datetime import datetime


class WorkPercent:
    def __init__(self, work_start, work_end, decimal_places):
        # These will be handled based on if we're passing midnight
        self.work_time_comparison_funcs = []
        self.seconds_from_start_till_now = None
        self.work_seconds = None

        self.start = self._make_time_object(work_start)
        self.end = self._make_time_object(work_end)
        if not self._try_setup_midnight_functions():
            self._setup_normal_functions()

        self.decimal_places = decimal_places

    def work_percent(self):
        now = datetime.now().replace(1, 1, 1)
        if any([working_during(now) for working_during in self.work_time_comparison_funcs]):
            return (self.seconds_from_start_till_now(now) / self.work_seconds) * 100
        else:
            return 100

    def update_ui_number(self, indicator):
        display_string = '{0:.{1}f}%'.format(self.work_percent(), self.decimal_places)
        indicator.set_label(display_string, 'work time percent')
        return True

    def _try_setup_midnight_functions(self):
        if self.start < self.end:
            return False
        self.work_time_comparison_funcs = [
            lambda now: now < self.end,
            lambda now: now > self.start
        ]
        self._setup_midnight_seconds_func()
        return True

    def _setup_midnight_seconds_func(self):
        secs_in_day = 60 * 60 * 24
        secs_from_end_to_12pm = secs_in_day - self._get_secs(self.start)

        def time_passed(now):
            if now > self.start:
                return (now - self.start).total_seconds()
            else:
                return self._get_secs(now) + secs_from_end_to_12pm
        self.seconds_from_start_till_now = time_passed
        self.work_seconds = secs_from_end_to_12pm + self._get_secs(self.end)

    def _setup_normal_functions(self):
        self.work_time_comparison_funcs = [lambda now: self.start < now <= self.end]
        self.seconds_from_start_till_now = lambda now: (now - self.start).seconds
        self.work_seconds = (self.end - self.start).total_seconds()
        return True

    @staticmethod
    def _get_secs(_time):
        return (_time - datetime(1, 1, 1)).total_seconds()

    @staticmethod
    def _make_time_object(target_time):
        hour = int(target_time) % 24
        minute = int((target_time - hour) * 60)
        second = int((target_time - hour) * 3600) % 60
        return datetime(1, 1, 1, hour=hour, minute=minute, second=second, microsecond=0)


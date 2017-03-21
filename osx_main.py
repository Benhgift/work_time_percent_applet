import rumps
import work_percent


def main(start, end, decimal_places):
    percent_tracker = work_percent.WorkPercent(start, end, decimal_places)
    app = WorkPercentApp(percent_tracker, decimal_places)

    app.run()


class WorkPercentApp(rumps.App):
    def __init__(self, percent_tracker, decimal_places):
        super().__init__("Work Percentage App")

        self.percent_tracker = percent_tracker
        self.decimal_places = decimal_places

    # Run every second
    @rumps.timer(1)
    def refresh_timer(self, _):
        display_string = '{0:.{1}f}%'.format(self.percent_tracker.work_percent(), self.decimal_places)
        self.title = display_string

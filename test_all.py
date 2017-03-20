import work_percent
from freezegun import freeze_time
from datetime import datetime

# If your work day is between 9am and 5pm, make sure that at 1pm it displays 50%
@freeze_time("13:00:00")
def test_basic_percent_calculation():
    _test_half_way_between_range(9, 17)


# Now if your work day starts late at night (10pm), make sure it can cross midnight if you work till 4am
@freeze_time("01:00:00")
def test_percent_calculation_when_range_crosses_midnight():
    _test_half_way_between_range(22, 4)


def _test_half_way_between_range(start, end):
    workPercent = work_percent.WorkPercent(start, end)
    percent = workPercent.work_percent()
    assert percent == 50

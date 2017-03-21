import work_percent
from freezegun import freeze_time
from datetime import datetime


@freeze_time("13:00:00")
def test_basic_percent_calculation():
    """ If your work day is between 9am and 5pm, make sure that at 1pm it displays 50% """
    _test_half_way_between_range(9, 17)


@freeze_time("01:00:00")
def test_percent_calculation_when_range_crosses_midnight():
    """ Now if your work day starts late at night (10pm), make sure it can cross midnight if you work till 4am """
    _test_half_way_between_range(22, 4)


@freeze_time("12:00:00")
def test_full_day_percent():
    """ Test a full day from 0am to 0am which should be half done at noon """
    _test_half_way_between_range(0, 0)


@freeze_time("00:00:00")
def test_full_day_starting_at_noon():
    """ Test a full day but start from noon """
    _test_half_way_between_range(12, 12)


def _test_half_way_between_range(start, end):
    workPercent = work_percent.WorkPercent(start, end)
    percent = workPercent.work_percent()
    assert percent == 50

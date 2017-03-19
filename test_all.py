import work_percent
from freezegun import freeze_time
from datetime import datetime

# If your work day is between 9am and 5pm, make sure that at 1pm it displays 50%
@freeze_time("13:00:00")
def test_basic_percent_calculation():
    workPercent = work_percent.WorkPercent(9, 17)
    percent = workPercent.work_percent()
    assert percent == 50


# Now if your work day starts late at night (9pm), make sure it can cross midnight if you work till 3am
@freeze_time("00:00:00")
def test_basic_percent_calculation():
    workPercent = work_percent.WorkPercent(21, 3)
    percent = workPercent.work_percent()
    assert percent == 50

![image](https://travis-ci.org/Benhgift/work_time_percent_applet.svg?branch=master)

# Work Day Percentage Display Applet

This will display the percent of the work day that's passed (8am - 5pm) as an Ubuntu applet

![image](https://i.imgur.com/HAxybM0.png)

# Quickstart

To run: `python3 main.py`

To run on boot open the Ubuntu "Startup Applications" app and add an entry for `main.py`

If you want a different time range then pass it in, for example: `python3 main.py 9 20`
 or edit the `config.py` file to change the defaults. 

# Tests

To run tests run `pytest`

# Config

You can edit the start and end times in the `config.py` file, and change the number of decimal places to display. 

You can also change the icon that appears next to the applet by passing in a number from 0-4 for `--icon_num` when you run the applet: 

`python3 main.py --icon_num=1`

import signal
from datetime import datetime
from time import sleep
from gi.repository import Gtk as gtk
from gi.repository import GObject
from gi.repository import AppIndicator3 as appindicator

APPINDICATOR_ID = 'myappindicator'

work_start_second = 60 * 60 * 8
work_end_second = 60 * 60 * 17
seconds_in_work_day = work_end_second - work_start_second

def work_percent():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    seconds = (now - midnight).seconds - work_start_second
    if seconds <= work_start_second:
        return 0
    elif seconds >= work_end_second:
        return 100
    else:
        return (seconds/seconds_in_work_day) * 100

def update_ui_number(indicator):
    indicator.set_label('%.3f' % work_percent() + '%', 'work time percent')
    return True

def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, gtk.STOCK_APPLY, appindicator.IndicatorCategory.SYSTEM_SERVICES)
    GObject.timeout_add(1000, update_ui_number, indicator)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    gtk.main()

def build_menu():
    menu = gtk.Menu()
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu
 
def quit(source):
    gtk.main_quit()

if __name__ == "__main__":
    main()

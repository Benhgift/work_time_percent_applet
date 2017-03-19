#!/usr/bin/env python3

import work_percent
import config
import fire
import signal
import sys
from os import path
#Check version.
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import GObject
from gi.repository import AppIndicator3 as appindicator

APPINDICATOR_ID = 'myappindicator'

def main(start=config.start, end=config.end, icon_num=0):
    script_path = path.abspath(path.dirname(sys.argv[0]))
    blank_icon = path.join(script_path, 'img', 'icon.png')
    icons = [blank_icon, gtk.STOCK_APPLY, gtk.STOCK_ADD, gtk.STOCK_YES, gtk.STOCK_ABOUT]
    workPercent = work_percent.WorkPercent(start, end)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, icons[icon_num], appindicator.IndicatorCategory.SYSTEM_SERVICES)
    GObject.timeout_add(1000, workPercent.update_ui_number, indicator)
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
    fire.Fire(main)

#!/usr/bin/env python3

import platform
import fire
import signal
import config


def main(start=config.start, end=config.end, decimal_places=config.decimal_places, icon_num=0):
    # Let ctrl-c kill the applet
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    system = platform.system()
    if system == "Linux":
        import ubuntu_main
        ubuntu_main.main(start, end, icon_num, decimal_places)

    elif system == "Darwin":
        import osx_main
        osx_main.main(start, end, decimal_places)


if __name__ == "__main__":
    fire.Fire(main)

#!/usr/bin/env python3
"""
Polyglot v2 node server NOAA weather data
Copyright (C) 2020 Robert Paauwe
"""

try:
    import polyinterface
except ImportError:
    import pgc_interface as polyinterface
import sys
import time
from nodes import noaa

LOGGER = polyinterface.LOGGER

if __name__ == "__main__":
    try:
        polyglot = polyinterface.Interface('NOAA')
        polyglot.start()
        control = noaa.Controller(polyglot)
        control.runForever()
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
        


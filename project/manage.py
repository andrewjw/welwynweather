#!/usr/bin/env python
import os
import os.path
import sys

if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../weatherve/lib/python2.7/site-packages")    

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weather.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

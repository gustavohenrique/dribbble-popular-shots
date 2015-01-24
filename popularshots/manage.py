#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    APP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app')
    sys.path.insert(0, APP_DIR)

    TEST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test')
    os.environ.setdefault("TEST_DISCOVER_TOP_LEVEL", TEST_DIR)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

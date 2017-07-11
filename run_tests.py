import argparse
import json
import sys

import pytest


DEFAULT_WEBDRIVER = 'firefox'


if __name__ == '__main__':

    # Read drivers.json from the project's root directory.
    drivers_json = None
    with open('drivers.json', 'r') as json_file:
        drivers_json = json.load(json_file)

    # Parse command line arguments.
    cmd_line_args = {}
    current_param = None
    for item in sys.argv[1:]:
        if item.startswith('--'):
            current_param = item[2:]

        else:
            cmd_line_args[current_param] = item

    driver = drivers_json.get(cmd_line_args.get('driver', DEFAULT_WEBDRIVER))
    test_suite = cmd_line_args.get('suite')


    pytest.main(['-s', 'tests/test.py'])

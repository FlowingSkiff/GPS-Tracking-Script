#!/usr/bin/env
import logging

from gps_tracking_script.cli import parse_args
from gps_tracking_script.parse import parse_test_file

logging.basicConfig(level=logging.DEBUG)
args = parse_args()
parse_test_file(args.input_file)

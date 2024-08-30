#!/usr/bin/env
import logging
import pathlib
from gps_tracking_script.parse import parse_test_file

logging.basicConfig(level=logging.DEBUG)

parse_test_file(pathlib.Path.cwd() / "sample_data.txt")

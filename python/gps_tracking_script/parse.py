#!/usr/bin/env
"""
parse.py

Parsing functions for handling raw text files and streams from other processes
"""
import json
import logging
import pathlib

import pandas

__all__ = "parse_test_file"

_logger = logging.getLogger(__name__)


def parse_test_file(
    input_file: pathlib.Path, encoding: str = "UTF-8"
) -> pandas.DataFrame:
    """Parse the input file into a dataframe for data manipulation

    input_file: file path that has an array of json like objects (without the beginning and ending [] and no newline commas)
    """

    _logger.debug("Loading text from %s", input_file)
    with input_file.open("r", encoding=encoding) as _input_file_stream:
        _input_file_text = ",".join(_input_file_stream.readlines())
    _input_file_text = "[" + _input_file_text + "]"
    _json_data = json.loads(_input_file_text)
    _logger.debug("Loaded jsonified data: %s", _json_data)

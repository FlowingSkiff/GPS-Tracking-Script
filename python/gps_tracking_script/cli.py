#!/usr/bin/env
import argparse
from dataclasses import dataclass
from pathlib import Path

__all__ = ("CLIArgs", "parse_args")


@dataclass
class CLIArgs:
    input_file: str | Path

    def __post_init__(self):
        self.input_file = Path(self.input_file).resolve()


def parse_args():
    "Parse command line arguments for module gps_tracking_script"
    _parser = argparse.ArgumentParser()
    _parser.add_argument("input_file", type=str)
    _namespace = _parser.parse_args()
    return CLIArgs(input_file=_namespace.input_file)

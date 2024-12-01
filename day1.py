from typing import Any

import day1
from utils.AOCParser import AOCParser


def header_parser(header: str) -> Any:
    pass


def row_parser(row: str) -> Any:
    pass


def main(aocp: AOCParser):
    pass


if __name__ == '__main__':
    aocp = AOCParser(input_str=day1.demoinput,
                     row_parser=row_parser,
                     has_header=False,
                     header_parser=None)

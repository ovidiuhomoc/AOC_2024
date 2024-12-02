from collections import Counter
from typing import Any

import day2
from utils.AOCParser import AOCParser


def header_parser(header: str) -> Any:
    pass


def row_parser(row: str) -> tuple[int, int]:
    pass


def part1(aocp: AOCParser):
    aocp.parse()

    pass


def part2(aocp: AOCParser):
    aocp.parse()

    pass


if __name__ == '__main__':
    aocp = AOCParser(input_str=day2.demoinput,
                     row_parser=row_parser,
                     has_header=False,
                     header_parser=None)

    # aocp = AOCParser(input_str=day2.input1,
    #                  row_parser=row_parser,
    #                  has_header=False,
    #                  header_parser=None)

    print(f"{part1(aocp) = }")
    # print(f"{part2(aocp) = }")

from collections import Counter
from typing import Any

import day1
from utils.AOCParser import AOCParser


def header_parser(header: str) -> Any:
    pass


def row_parser(row: str) -> tuple[int, int]:
    parsed_row = tuple(map(int, str(row).strip().split()))
    return parsed_row[0], parsed_row[1]


def part1(aocp: AOCParser):
    aocp.parse()

    list_1: list = [row[0] for row in aocp.rows]
    list_2: list = [row[1] for row in aocp.rows]

    list_1.sort(reverse=False)
    list_2.sort(reverse=False)

    total_dif = 0

    for l1_el, l2_el in zip(list_1, list_2):
        diff = abs(l1_el - l2_el)
        total_dif += diff

    return total_dif


def part2(aocp: AOCParser):
    aocp.parse()

    list_1: list = [row[0] for row in aocp.rows]
    list_2: list = [row[1] for row in aocp.rows]

    c = Counter(list_2)

    total_sum = 0

    for l1_el in list_1:
        multip = c[l1_el] if c and l1_el in c else 0
        total_sum += l1_el * multip

    return total_sum


if __name__ == '__main__':
    # aocp = AOCParser(input_str=day1.demoinput,
    #                  row_parser=row_parser,
    #                  has_header=False,
    #                  header_parser=None)

    aocp = AOCParser(input_str=day1.input1,
                     row_parser=row_parser,
                     has_header=False,
                     header_parser=None)

    # print(f"{part1(aocp) = }")
    print(f"{part2(aocp) = }")

import copy
from typing import Any

import day2
from utils.AOCParser import AOCParser


def header_parser(header: str) -> Any:
    pass


def row_parser(row: str) -> list[int]:
    return list(map(int, str(row).split()))


def is_report_safe(levels: list[int]) -> bool:
    if levels[0] == levels[1]:
        return False

    if abs(levels[0] - levels[1]) > 3:
        return False

    ascending = True if levels[0] < levels[1] else False

    for i in range(1, len(levels) - 1):
        if levels[i] == levels[i + 1]:
            return False
        if ascending and levels[i] > levels[i + 1]:
            return False
        if not ascending and levels[i] < levels[i + 1]:
            return False
        if abs(levels[i] - levels[i + 1]) > 3:
            return False

    return True


def part1(aocp: AOCParser):
    aocp.parse()

    safe_count = 0
    for row in aocp.rows:
        if is_report_safe(row):
            safe_count += 1

    return safe_count


def part2(aocp: AOCParser):
    aocp.parse()

    safe_count = 0
    for row in aocp.rows:
        if is_report_safe(row):
            safe_count += 1
        else:
            for i in range(0, len(row)):
                row_copy = copy.deepcopy(row)
                new_row = row_copy[:i] + row_copy[i + 1:]
                if is_report_safe(new_row):
                    safe_count += 1
                    break

    return safe_count


if __name__ == '__main__':
    # aocp = AOCParser(input_str=day2.demoinput,
    #                  row_parser=row_parser,
    #                  has_header=False,
    #                  header_parser=header_parser)

    aocp = AOCParser(input_str=day2.input1,
                     row_parser=row_parser,
                     has_header=False,
                     header_parser=header_parser)

    # print(f"{part1(aocp) = }")
    print(f"{part2(aocp) = }")

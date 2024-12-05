import copy
from typing import Any

import day04
from utils.AOCParser import AOCParser

directions: dict = {'E': (0, 1),
                    'W': (0, -1),
                    'S': (1, 0),
                    'N': (-1, 0),
                    'SE': (1, 1),
                    'SW': (1, -1),
                    'NE': (-1, 1),
                    'NW': (-1, -1)}



def header_parser(header: str) -> Any:
    pass


def row_parser(row: str) -> str:
    refined_row = copy.deepcopy(row)
    ch_set = set(row.upper())

    for ch in ch_set:
        if ch not in ['X', 'M', 'A', 'S']:
            refined_row = refined_row.replace(ch, '.')

    return refined_row


def construct_word(table: list[list[str]], row_index: int, col_index: int, horiz_direction: int, vert_direction: int, length: int = 4) -> str:
    word = table[row_index][col_index]
    next_row_index = row_index + vert_direction
    next_col_index = col_index + horiz_direction

    while 0 <= next_row_index < len(table) and 0 <= next_col_index < len(table[0]) and len(word) < length:
        word += table[next_row_index][next_col_index]
        next_row_index += vert_direction
        next_col_index += horiz_direction

    return word



def part1(aocp: AOCParser):
    aocp.parse()

    table = []
    for row in aocp.rows:
        table.append(list(row))

    counter = 0

    # construct all possible words in all directions
    for row_index, row in enumerate(table):
        for col_index, ch in enumerate(row):
            if ch == 'X':
                for direction, (v_increment, h_increment) in directions.items():
                    candidate = construct_word(table, row_index, col_index, h_increment, v_increment)
                    if candidate and candidate.upper() == 'XMAS':
                        counter += 1

    return counter


def part2(aocp: AOCParser):
    aocp.parse()

    table = []
    for row in aocp.rows:
        table.append(list(row))

    candidate_words: list[tuple[int, int, str]] = []

    counter = 0

    # construct all possible words in all directions
    for row_index, row in enumerate(table):
        for col_index, ch in enumerate(row):
            if ch == 'A':
                diagonal_up_right_candidate = construct_word(table, row_index, col_index, horiz_direction=1, vert_direction=-1, length=2)
                diagonal_down_left_candidate = construct_word(table, row_index, col_index, horiz_direction=-1, vert_direction=1, length=2)

                correct_diagonal = (diagonal_up_right_candidate == "AM" and diagonal_down_left_candidate == "AS") or (diagonal_up_right_candidate == "AS" and diagonal_down_left_candidate == "AM")
                if not correct_diagonal:
                    continue

                diagonal_up_left_candidate = construct_word(table, row_index, col_index, horiz_direction=-1, vert_direction=-1, length=2)
                diagonal_down_right_candidate = construct_word(table, row_index, col_index, horiz_direction=1, vert_direction=1, length=2)
                correct_diagonal = (diagonal_up_left_candidate == "AM" and diagonal_down_right_candidate == "AS") or (diagonal_up_left_candidate == "AS" and diagonal_down_right_candidate == "AM")
                if not correct_diagonal:
                    continue

                counter += 1

    return counter


if __name__ == '__main__':
    # aocp = AOCParser(input_str=day04.demoinput,
    #                  row_parser=row_parser,
    #                  has_header=False,
    #                  header_parser=header_parser)

    aocp = AOCParser(input_str=day04.input1,
                     row_parser=row_parser,
                     has_header=False,
                     header_parser=header_parser)

    print(f"{part1(aocp) = }")
    print(f"{part2(aocp) = }")

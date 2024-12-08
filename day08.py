import day08


def is_antinode_valid(antinode: tuple[int, int], max_row: int, max_col: int) -> bool:
    row, col = antinode
    return 0 <= row < max_row and 0 <= col < max_col


def compute_antinodes(coord_antenna_1: tuple[int, int], coord_antenna_2: tuple[int, int], row_limit: int, col_limit: int, compute_harmonics: int) -> list[tuple[int, int]]:
    results = []

    first_antenna, second_antenna = (coord_antenna_1, coord_antenna_2) if coord_antenna_1[0] < coord_antenna_2[0] else (coord_antenna_2, coord_antenna_1)

    row1, col1 = first_antenna
    row2, col2 = second_antenna

    row_diff = row2 - row1
    col_diff = col2 - col1

    next_up_antinode_row = row1 - row_diff
    next_up_antinode_col = col1 - col_diff

    if is_antinode_valid((next_up_antinode_row, next_up_antinode_col), row_limit, col_limit):
        results.append((next_up_antinode_row, next_up_antinode_col))

        while True and compute_harmonics:
            next_up_antinode_row = next_up_antinode_row - row_diff
            next_up_antinode_col = next_up_antinode_col - col_diff

            if is_antinode_valid((next_up_antinode_row, next_up_antinode_col), row_limit, col_limit):
                results.append((next_up_antinode_row, next_up_antinode_col))
            else:
                break

    row_diff = row2 - row1
    col_diff = col2 - col1
    next_down_antinode_row = row2 + row_diff
    next_down_antinode_col = col2 + col_diff

    if is_antinode_valid((next_down_antinode_row, next_down_antinode_col), row_limit, col_limit):
        results.append((next_down_antinode_row, next_down_antinode_col))

        while True and compute_harmonics:
            next_down_antinode_row = next_down_antinode_row + row_diff
            next_down_antinode_col = next_down_antinode_col + col_diff

            if is_antinode_valid((next_down_antinode_row, next_down_antinode_col), row_limit, col_limit):
                results.append((next_down_antinode_row, next_down_antinode_col))
            else:
                break

    return results


def main(input: str, part=1):
    antenna_grid: list[list[str]] = []

    for line in input.splitlines():
        antenna_grid.append(list(line))

    grouped_antennas = {}

    for row_index, row in enumerate(antenna_grid):
        for col_index, candidate in enumerate(row):
            if candidate != '.':
                grouped_antennas.setdefault(candidate, []).append((row_index, col_index))

    max_row = len(antenna_grid)
    max_col = len(antenna_grid[0])

    antinodes_set = set()
    for antenna_type, antennas in grouped_antennas.items():

        for antenna_index, antenna_1 in enumerate(antennas):
            for antenna_2 in antennas[antenna_index + 1:]:
                if antenna_1 != antenna_2:
                    antinodes = compute_antinodes(antenna_1, antenna_2, row_limit=max_row, col_limit=max_col, compute_harmonics=False if part == 1 else True)
                    antinodes_set.update(antinodes)

                    if part == 2:
                        antinodes_set.update([antenna_1, antenna_2])

    for row_index, row in enumerate(antenna_grid):
        for col_index, candidate in enumerate(row):
            if candidate != '.':
                print(candidate, end='')
                continue

            if (row_index, col_index) in antinodes_set:
                print('#', end='')
            else:
                print('.', end='')

        print()

    return len(antinodes_set)


def part2(input: str):
    pass


if __name__ == '__main__':
    dinput = day08.demoinput
    dinput2 = day08.demoinput2
    input = day08.input1

    # print(f"{main(input, part=1) = }")
    # print(f"{main(dinput2, part=2) = }")
    print(f"{main(input, part=2) = }")

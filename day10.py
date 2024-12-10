import day10

coords = {"N": (-1, 0),
          "S": (1, 0),
          "E": (0, 1),
          "W": (0, -1)}


def get_trailheads_success(grid: list[list[int]], start_pos: tuple[int, int]) -> tuple[set[tuple[int, int]], list[int]]:
    row, col = start_pos
    current_pos_value = grid[row][col]

    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
        return set(), []

    if current_pos_value == 9:
        return {(row, col)}, [1]

    candidates = []

    for coord_candidate in coords.keys():
        next_row, next_col = row + coords[coord_candidate][0], col + coords[coord_candidate][1]
        if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
            next_value = grid[next_row][next_col]
            if isinstance(next_value, int) and next_value == current_pos_value + 1:
                candidates.append((next_row, next_col))

    if not candidates:
        return set(), []

    final_peaks_reached = set()
    final_success_lists = []
    for candidate in candidates:
        candidate_peaks, candidate_success_lists = get_trailheads_success(grid, candidate)

        final_peaks_reached = final_peaks_reached | candidate_peaks
        final_success_lists = final_success_lists + candidate_success_lists

    return final_peaks_reached, final_success_lists


def main(input: str, part: int = 1):
    grid: list[list[int]] = [[int(char) if char.isdigit() else char for char in line] for line in input.splitlines()]

    starts: list[tuple[int, int]] = [(row_index, col_index) for row_index, row in enumerate(grid) for col_index, char in enumerate(row) if char == 0]

    total_sum_part_1 = 0
    total_sum_part_2 = 0
    for start in starts:
        final_peaks_reached, final_success_lists = get_trailheads_success(grid, start)
        total_sum_part_1 += len(final_peaks_reached)
        total_sum_part_2 += sum(final_success_lists)

    if part == 1:
        return total_sum_part_1
    else:
        return total_sum_part_1, total_sum_part_2



if __name__ == '__main__':
    dinput = day10.demoinput
    dinput1 = day10.demoinput1
    dinput2 = day10.demoinput2
    input1 = day10.input1

    # print(f"{main(dinput, part=1) = }")
    # print(f"{main(input1, part=1) = }")
    # print(f"{main(dinput, part=2) = }")
    print(f"{main(input1, part=2) = }")

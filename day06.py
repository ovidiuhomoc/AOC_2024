import copy

import day06

directions = ['N', 'E', 'S', 'W']


class MapPoint:
    def __init__(self, row: int, col: int, ch: str):
        self.row = row
        self.col = col
        self.value = ch

    def is_guard(self):
        return self.value in ['X', '^']

    def is_obstacle(self):
        return self.value == '#'

    def is_empty(self):
        return self.value == '.'

    def is_visited(self):
        return self.value in ['X', '^']


class Guard:
    def __init__(self, coord: MapPoint):
        self.coord = coord
        self.direction = 'N'

    @property
    def rotate(self, direction: str = 'R'):
        if direction == 'L':
            self.direction = directions[(directions.index(self.direction) - 1) % 4]
        elif direction == 'R':
            self.direction = directions[(directions.index(self.direction) + 1) % 4]

        return self

    def get_next_step_coord(self, step: int = 1):
        if self.direction == 'N':
            return self.coord.row - step, self.coord.col
        elif self.direction == 'E':
            return self.coord.row, self.coord.col + step
        elif self.direction == 'S':
            return self.coord.row + step, self.coord.col
        elif self.direction == 'W':
            return self.coord.row, self.coord.col - step


class MapGame:
    def __init__(self, init_data: str | None = None, map_data: list[list[MapPoint]] | None = None):
        self.map = [] if map_data is None else map_data
        if not self.map:
            self.initialize_map(init_data)

        self.guard: Guard | None = None
        self.initialize_guard()

    def print_map(self):
        for row in self.map:
            print(''.join([point.value for point in row]))

    def initialize_map(self, init_data: str):
        for line_index, line in enumerate(init_data.split('\n')):
            current_row = []
            for ch_index, ch in enumerate(line):
                current_row.append(MapPoint(line_index, ch_index, ch))
            self.map.append(current_row)

    def initialize_guard(self):
        for row in self.map:
            for point in row:
                if point.is_guard():
                    self.guard = Guard(point)
                    return

    def move_step(self, step: int = 1):
        next_row, next_col = self.guard.get_next_step_coord(step)
        current_point = self.map[self.guard.coord.row][self.guard.coord.col]
        if not (0 <= next_row < len(self.map) and 0 <= next_col < len(self.map[0])):
            current_point.value = 'X'
            return None

        next_point = self.map[next_row][next_col]
        if not next_point.is_obstacle():
            self.guard.coord = next_point
            current_point.value = 'X'
            next_point.value = 'X'
            return True

        # first 90 degree turn
        next_row, next_col = self.guard.rotate.get_next_step_coord(step)
        if not (0 <= next_row < len(self.map) and 0 <= next_col < len(self.map[0])):
            current_point.value = 'X'
            return None

        next_point = self.map[next_row][next_col]
        if not next_point.is_obstacle():
            self.guard.coord = next_point
            current_point.value = 'X'
            next_point.value = 'X'
            return True

        # second 90 degree turn
        next_row, next_col = self.guard.rotate.get_next_step_coord(step)
        if not (0 <= next_row < len(self.map) and 0 <= next_col < len(self.map[0])):
            current_point.value = 'X'
            next_point.value = 'X'
            return None

        next_point = self.map[next_row][next_col]
        if not next_point.is_obstacle():
            self.guard.coord = next_point
            current_point.value = 'X'
            next_point.value = 'X'
            return True

        # third 90 degree turn
        next_row, next_col = self.guard.rotate.get_next_step_coord(step)
        if not (0 <= next_row < len(self.map) and 0 <= next_col < len(self.map[0])):
            current_point.value = 'X'
            next_point.value = 'X'
            return None

        next_point = self.map[next_row][next_col]
        if not next_point.is_obstacle():
            self.guard.coord = next_point
            current_point.value = 'X'
            next_point.value = 'X'
            return True

        return False

    def compute_next_step(self, step: int = 1):
        simulated_guard = Guard(MapPoint(self.guard.coord.row, self.guard.coord.col, "^"))
        simulated_guard.direction = self.guard.direction

        next_row, next_col = simulated_guard.get_next_step_coord()
        current_point = self.map[simulated_guard.coord.row][simulated_guard.coord.col]
        if not (0 <= next_row < len(self.map) and 0 <= next_col < len(self.map[0])):
            return None

        next_point = self.map[next_row][next_col]
        if not next_point.is_obstacle():
            return next_row, next_col

        # first 90 degree turn
        next_row, next_col = simulated_guard.rotate.get_next_step_coord(step)
        if not (0 <= next_row < len(self.map) and 0 <= next_col < len(self.map[0])):
            return None

        next_point = self.map[next_row][next_col]
        if not next_point.is_obstacle():
            return next_row, next_col

        # second 90 degree turn
        next_row, next_col = simulated_guard.rotate.get_next_step_coord(step)
        if not (0 <= next_row < len(self.map) and 0 <= next_col < len(self.map[0])):
            return None

        next_point = self.map[next_row][next_col]
        if not next_point.is_obstacle():
            return next_row, next_col

        # third 90 degree turn
        next_row, next_col = simulated_guard.rotate.get_next_step_coord(step)
        if not (0 <= next_row < len(self.map) and 0 <= next_col < len(self.map[0])):
            return None

        next_point = self.map[next_row][next_col]
        if not next_point.is_obstacle():
            return next_row, next_col

        return False


def part1(input: str):
    mg = MapGame(input)

    result = mg.move_step()
    while result:
        result = mg.move_step()

    assert result is None, "Guard is stuck"

    x_count = 0
    mg.print_map()
    for row in mg.map:
        for point in row:
            if point.is_visited():
                x_count += 1

    return x_count


def is_a_loop(mg: MapGame):
    result = mg.move_step()
    current_guard_row, current_guard_col = mg.guard.coord.row, mg.guard.coord.col
    compute_result = mg.compute_next_step()
    if not compute_result:
        return False
    else:
        next_row, next_col = compute_result

    if mg.map[current_guard_row][current_guard_col].value == "X" and mg.map[next_row][next_col].value == "X" and not (current_guard_row == next_row and current_guard_col == next_col):
        return True

    while result:
        result = mg.move_step()

        if result:
            current_guard_row, current_guard_col = mg.guard.coord.row, mg.guard.coord.col
            compute_result = mg.compute_next_step()
            if not compute_result:
                return False
            else:
                next_row, next_col = compute_result

            if mg.map[current_guard_row][current_guard_col].value == "X" and mg.map[next_row][next_col].value == "X" and not (current_guard_row == next_row and current_guard_col == next_col):
                return True

    if result is False:
        return False


def is_a_loop_v2(mg: MapGame):
    all_pos = []
    current_guard_row, current_guard_col, current_guard_direction = mg.guard.coord.row, mg.guard.coord.col, mg.guard.direction
    all_pos.append((current_guard_row, current_guard_col, current_guard_direction))

    result = mg.move_step()
    while result:
        current_guard_row, current_guard_col, current_guard_direction = mg.guard.coord.row, mg.guard.coord.col, mg.guard.direction
        if (current_guard_row, current_guard_col, current_guard_direction) in all_pos:
            return True
        else:
            all_pos.append((current_guard_row, current_guard_col, current_guard_direction))

        result = mg.move_step()

    return False


def part2(input: str):
    mg = MapGame(input)
    initial_map_data = mg.map

    position_options_count = 0

    for row in mg.map:
        for point in row:
            if point.is_guard():
                continue

            if point.is_obstacle():
                continue

            row_index = point.row
            col_index = point.col

            modified_map_data = copy.deepcopy(initial_map_data)
            modified_map_data[row_index][col_index].value = '#'

            new_mg = MapGame(map_data=modified_map_data)
            new_mg.print_map()
            print()
            print()

            try:
                result = is_a_loop_v2(new_mg)
            except Exception as e:
                raise e
            if result:
                position_options_count += 1

    return position_options_count


if __name__ == '__main__':
    # input = day06.demoinput
    input = day06.input1

    # part = part1
    part = part2

    print(f"{part(input) = }")

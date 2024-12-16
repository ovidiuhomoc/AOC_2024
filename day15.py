from dataclasses import dataclass
from typing import Literal

import day15


@dataclass
class Entity:
    """An entity and point in 2D space where the real and imaginary parts are integers and the complex number real represents the x-coordinate and imaginary represents the y-coordinate."""
    entity_type: Literal["robot", "box", "wall", "empty"]
    coord: complex

    @property
    def x(self) -> int:
        return int(self.coord.real)

    @property
    def y(self) -> int:
        return int(self.coord.imag)

    @property
    def as_char(self) -> str:
        match self.entity_type:
            case "robot":
                return "@"
            case "box":
                return "O"
            case "wall":
                return "#"
            case "empty":
                return "."

    def swap(self, other: "Entity" or None):
        if other is None:
            raise ValueError("Cannot swap with None")
        self.coord, other.coord = other.coord, self.coord


def get_empty_slot(entity_list: list[Entity | None], reverse_search=False):
    if not reverse_search:
        list_to_iterate = [(entity_index_in_list, entity) for entity_index_in_list, entity in enumerate(entity_list)]
    else:
        list_to_iterate = [(entity_index_in_list, entity) for entity_index_in_list, entity in enumerate(entity_list)][::-1]

    for (entity_index_in_list, entity) in list_to_iterate:
        if entity and entity.entity_type == "empty":
            yield entity_index_in_list


class Grid:
    def __init__(self, input_string: str):
        self.width: int = 0
        self.height: int = 0
        self.grid_robot: Entity | None = None
        self.objects: list[Entity] = []

        self.input_string = input_string
        self.parse_input(input_string)

    def parse_input(self, input_string: str):
        for line_index, line in enumerate(input_string.splitlines()):
            for ch_index, ch in enumerate(line):
                # line_index = y, ch_index = x
                self.width = max(self.width, ch_index + 1)
                self.height = max(self.height, line_index + 1)

                match ch:
                    case "#":
                        # Wall
                        self.objects.append(Entity(coord=ch_index + line_index * 1j, entity_type="wall"))
                    case ".":
                        # Empty space
                        self.objects.append(Entity(coord=ch_index + line_index * 1j, entity_type="empty"))
                    case "O":
                        # box
                        self.objects.append(Entity(coord=ch_index + line_index * 1j, entity_type="box"))
                    case "@":
                        # robot
                        robot_entity = Entity(coord=ch_index + line_index * 1j, entity_type="robot")
                        self.objects.append(robot_entity)
                        self.grid_robot = robot_entity

    @property
    def as_table(self) -> list[list[Entity | None]]:
        table: list[list[Entity | None]] = [[None for _ in range(self.width)] for _ in range(self.height)]
        for obj in self.objects:
            table[obj.y][obj.x] = obj

        return table

    def __str__(self):
        return "\n".join("".join(obj.as_char for obj in row) for row in self.as_table)

    def attempt_move(self, direction: str):
        temp_grid_snapshot: list[list[Entity | None]] = self.as_table

        try:
            match direction:
                case ">":
                    # Move right
                    entities_list = [self.grid_robot]
                    iterator = 0
                    while True:
                        next_x = self.grid_robot.x + 1 + iterator
                        if temp_grid_snapshot[self.grid_robot.y][next_x].entity_type == "wall":
                            break
                        entities_list.append(temp_grid_snapshot[self.grid_robot.y][next_x])
                        iterator += 1
                    entity_index_in_list = next(get_empty_slot(entities_list), None)
                    if not entity_index_in_list:
                        return
                    temp_list = [(pos, entity) for pos, entity in enumerate(entities_list[:entity_index_in_list + 1])]
                case "v":
                    # Move down
                    entities_list = [self.grid_robot]
                    iterator = 0
                    while True:
                        next_y = self.grid_robot.y + 1 + iterator
                        if temp_grid_snapshot[next_y][self.grid_robot.x].entity_type == "wall":
                            break
                        entities_list.append(temp_grid_snapshot[next_y][self.grid_robot.x])
                        iterator += 1
                    entity_index_in_list = next(get_empty_slot(entities_list), None)
                    if not entity_index_in_list:
                        return
                    temp_list = [(pos, entity) for pos, entity in enumerate(entities_list[:entity_index_in_list + 1])]
                case "<":
                    # Move left
                    entities_list = [self.grid_robot]
                    iterator = 0
                    while True:
                        next_x = self.grid_robot.x - 1 - iterator
                        if temp_grid_snapshot[self.grid_robot.y][next_x].entity_type == "wall":
                            break
                        entities_list.append(temp_grid_snapshot[self.grid_robot.y][next_x])
                        iterator += 1
                    entity_index_in_list = next(get_empty_slot(entities_list), None)
                    if not entity_index_in_list:
                        return
                    temp_list = [(pos, entity) for pos, entity in enumerate(entities_list[:entity_index_in_list + 1])]
                case "^":
                    # Move up
                    entities_list = [self.grid_robot]
                    iterator = 0
                    while True:
                        next_y = self.grid_robot.y - 1 - iterator
                        if temp_grid_snapshot[next_y][self.grid_robot.x].entity_type == "wall":
                            break
                        entities_list.append(temp_grid_snapshot[next_y][self.grid_robot.x])
                        iterator += 1
                    entity_index_in_list = next(get_empty_slot(entities_list), None)
                    if not entity_index_in_list:
                        return
                    temp_list = [(pos, entity) for pos, entity in enumerate(entities_list[:entity_index_in_list + 1])]
                case _:
                    raise ValueError(f"Invalid direction: {direction}")

            # if direction in ["<", "^"]:
            #     list_to_iterate = temp_list[:-1]
            #     list_to_iterate.reverse()
            # else:
            #     list_to_iterate = temp_list[:-1]
            list_to_iterate = temp_list[:-1]

            for pos, entity in list_to_iterate:
                entity.swap(temp_list[pos + 1][1])
        except Exception as e:
            raise RuntimeError(f"Error while attempting to move {direction=}") from e


def main(input, part=1, verbosity=False):
    grid_input, moves_input = input.split("\n\n")
    grid = Grid(grid_input)

    moves: list[str] = [move for move_list in moves_input.splitlines() for move in move_list.strip()]
    for move in moves:
        grid.attempt_move(move)
        if verbosity:
            print(f"Moving {move = }")
            print(str(grid))
            print()

    temp_grid_snapshot: list[list[Entity | None]] = grid.as_table
    gps_sum = 0
    for row in temp_grid_snapshot:
        for entity in row:
            if entity and entity.entity_type == "box":
                gps_sum += entity.y * 100 + entity.x

    return gps_sum


if __name__ == '__main__':
    dinput = day15.demoinput
    dinput2 = day15.demoinput2
    input1 = day15.input1

    # print(f"{main(dinput, part=1, verbosity=True) = }")
    # print(f"{main(dinput2, part=1, verbosity=True) = }")
    print(f"{main(input1, part=1) = }")

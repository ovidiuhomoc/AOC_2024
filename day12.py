import queue

import day12


def get_neighbours(grid: list[list[str]], row: int, col: int) -> list[tuple[int, int, str]]:
    neighbours = []

    candidate_coords = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    for candidate_row, candidate_col in candidate_coords:
        if 0 <= candidate_row < len(grid) and 0 <= candidate_col < len(grid[0]):
            neighbours.append((candidate_row, candidate_col, grid[candidate_row][candidate_col]))

    return neighbours


def is_flower_in_any_region(regions: list[tuple[str, list[tuple[int, int, int]]]], row: int, col: int) -> bool:
    for flower, region in regions:
        for (r, c, _) in region:
            if row == r and col == c:
                return True

    return False


def discover_flower_region(grid: list[list[str]], regions: list[tuple[str, list[tuple[int, int, int]]]], flower: str, row: int, col: int) -> tuple[str, list[tuple[int, int, int]]]:
    to_explore = queue.SimpleQueue()
    to_explore.put((row, col, 0, 0))
    region = []

    def in_region(neighbour_row: int, neighbour_col: int, flower_type: str) -> bool:
        for r, c, _ in region:
            if neighbour_row == r and neighbour_col == c:
                return True

    while not to_explore.empty():
        current = to_explore.get()
        if not current:
            continue

        neighbours = get_neighbours(grid=grid, row=current[0], col=current[1])
        for neighbour in neighbours:
            if neighbour[2] == flower and not in_region(*neighbour) and not is_flower_in_any_region(regions, neighbour[0], neighbour[1]):
                to_explore.put(neighbour)

        contributing_perim = 4 - len(neighbours)
        contributing_perim = contributing_perim + sum(1 for neighbour in neighbours if neighbour[2] != flower)
        region.append((current[0], current[1], contributing_perim))

    return flower, region


def get_corners_count(region_coords: set[tuple[int, int]]) -> int:
    if not region_coords:
        return 0

    if len(region_coords) == 1:
        return 4

    # turn each pixel in a square of 2x2 pixels
    pixels: list[tuple[int, int]] = []
    for row, col in region_coords:
        pixels.extend([(2 * row, 2 * col), (2 * row, 2 * col + 1), (2 * row + 1, 2 * col), (2 * row + 1, 2 * col + 1)])

    def n_flower(coord: tuple[int, int]) -> tuple[int, int]:
        return coord[0] - 1, coord[1]

    def nw_flower(coord: tuple[int, int]) -> tuple[int, int]:
        return coord[0] - 1, coord[1] - 1

    def ne_flower(coord: tuple[int, int]) -> tuple[int, int]:
        return coord[0] - 1, coord[1] + 1

    def s_flower(coord: tuple[int, int]) -> tuple[int, int]:
        return coord[0] + 1, coord[1]

    def sw_flower(coord: tuple[int, int]) -> tuple[int, int]:
        return coord[0] + 1, coord[1] - 1

    def se_flower(coord: tuple[int, int]) -> tuple[int, int]:
        return coord[0] + 1, coord[1] + 1

    def w_flower(coord: tuple[int, int]) -> tuple[int, int]:
        return coord[0], coord[1] - 1

    def e_flower(coord: tuple[int, int]) -> tuple[int, int]:
        return coord[0], coord[1] + 1

    corners = 0
    for pixel in pixels:
        corners += sum([w_flower(pixel) in pixels and n_flower(pixel) in pixels and nw_flower(pixel) not in pixels,
                        n_flower(pixel) in pixels and e_flower(pixel) in pixels and ne_flower(pixel) not in pixels,
                        e_flower(pixel) in pixels and s_flower(pixel) in pixels and se_flower(pixel) not in pixels,
                        s_flower(pixel) in pixels and w_flower(pixel) in pixels and sw_flower(pixel) not in pixels])

        corners += sum([n_flower(pixel) not in pixels and e_flower(pixel) not in pixels,
                        n_flower(pixel) not in pixels and w_flower(pixel) not in pixels,
                        s_flower(pixel) not in pixels and e_flower(pixel) not in pixels,
                        s_flower(pixel) not in pixels and w_flower(pixel) not in pixels])

    return corners


def main(input: str, part: int = 1):
    grid: list[list[str]] = [[char for char in line] for line in input.splitlines()]
    regions: list[tuple[str, list[tuple[int, int, int]]]] = []

    for row_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            if not is_flower_in_any_region(regions, row_index, col_index):
                # region = flower, [ (row,col,perim)   ]
                region: tuple[str, list[tuple[int, int, int]]] = discover_flower_region(grid=grid, regions=regions, flower=char, row=row_index, col=col_index)
                regions.append(region)

    total_sum = 0
    for region in regions:
        area = len(region[1])
        perim_p1 = sum(perim for _, _, perim in region[1])
        region_corners: int = get_corners_count({(row, col) for row, col, perim in region[1]})
        if part == 1:
            total_sum += area * perim_p1
        else:
            area2 = len({(row, col) for row, col, perim in region[1]})
            total_sum += area2 * region_corners

    return total_sum


if __name__ == '__main__':
    dinput = day12.demoinput
    dinput2 = day12.demoinput2
    dinput3 = day12.demoinput3
    input1 = day12.input1

    # print(f"{main(dinput, part=1) = }")
    # print(f"{main(dinput2, part=1) = }")
    # print(f"{main(dinput3, part=1) = }")
    # print(f"{main(input1, part=1) = }")
    # print(f"{main(dinput, part=2) = }")
    print(f"{main(input1, part=2) = }")

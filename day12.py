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
    to_explore = set()
    to_explore.add((row, col, 0))
    region = []

    def in_region(neighbour_row: int, neighbour_col: int, perim: int) -> bool:
        for r, c, _ in region:
            if neighbour_row == r and neighbour_col == c:
                return True

    while to_explore:
        current = to_explore.pop()
        if not current:
            continue

        neighbours = get_neighbours(grid=grid, row=current[0], col=current[1])
        for neighbour in neighbours:
            if neighbour[2] == flower and not in_region(*neighbour) and not is_flower_in_any_region(regions, neighbour[0], neighbour[1]):
                to_explore.add(neighbour)

        contributing_perim = 4 - len(neighbours)
        contributing_perim = contributing_perim + sum(1 for neighbour in neighbours if neighbour[2] != flower)
        region.append((current[0], current[1], contributing_perim))

    return flower, region


def get_vertices_count(points: list[tuple[int, int]]) -> int:
    sorted_points = sorted(points)

    lower = []
    for point in sorted_points:
        while len(lower) >= 2:
            a = lower[-2]
            b = lower[-1]

            ab = (b[0] - a[0], b[1] - a[1])
            ac = (point[0] - a[0], point[1] - a[1])
            cross_product = ab[0] * ac[1] - ab[1] * ac[0]

            if cross_product > 0:
                break
            lower[:] = lower[:-1]
        lower.append(point)

    upper = []
    for point in sorted_points[::-1]:
        while len(upper) >= 2:
            a = upper[-2]
            b = upper[-1]

            ab = (b[0] - a[0], b[1] - a[1])
            ac = (point[0] - a[0], point[1] - a[1])
            cross_product = ab[0] * ac[1] - ab[1] * ac[0]

            if cross_product > 0:
                break
            upper[:] = upper[:-1]
        upper.append(point)

    hull = lower[:-1] + upper[:-1]



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
        vertices_count = get_vertices_count([(r, c) for r, c, perim in region[1]])
        total_sum += area * perim_p1

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
    print(f"{main(dinput, part=2) = }")
    # print(f"{main(input1, part=2) = }")

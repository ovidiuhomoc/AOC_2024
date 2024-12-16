import heapq
from dataclasses import dataclass
from typing import Literal, Any

import day16


@dataclass
class Entity:
    """An entity and point in 2D space where the real and imaginary parts are integers and the complex number real represents the x-coordinate and imaginary represents the y-coordinate."""
    entity_type: Literal["agent", "wall", "empty", "end"]
    coord: complex
    orientation_vector: complex | None = None

    @property
    def x(self) -> int:
        return int(self.coord.real)

    @property
    def y(self) -> int:
        return int(self.coord.imag)

    @property
    def as_char(self) -> str:
        match self.entity_type:
            case "agent":
                return "S"
            case "wall":
                return "#"
            case "empty":
                return "."
            case "end":
                return "E"

    def swap(self, other: "Entity" or None):
        if other is None:
            raise ValueError("Cannot swap with None")
        self.coord, other.coord = other.coord, self.coord


class Grid:
    def __init__(self, input_string: str):
        self.width: int = 0
        self.height: int = 0
        self.grid_agent_start: complex = 0 + 0j
        self.grid_end: complex = 0 + 0j
        self.objects: list[Entity] = []

        self.input_string = input_string
        self.parse_input(input_string)

    def parse_input(self, input_string: str):
        # set agent orientation to E
        orientation: complex = 1 + 0j

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
                    case "S":
                        # agent start
                        agent_entity = Entity(coord=ch_index + line_index * 1j, entity_type="agent", orientation_vector=orientation)
                        self.objects.append(agent_entity)
                        self.grid_agent_start = agent_entity.coord
                    case "E":
                        # end
                        end_entity = Entity(coord=ch_index + line_index * 1j, entity_type="end")
                        self.objects.append(end_entity)
                        self.grid_end = end_entity.coord

    @property
    def as_table(self) -> list[list[Entity | None]]:
        table: list[list[Entity | None]] = [[None for _ in range(self.width)] for _ in range(self.height)]
        for obj in self.objects:
            table[obj.y][obj.x] = obj

        return table

    def __str__(self):
        return "\n".join("".join(obj.as_char for obj in row) for row in self.as_table)

    def compute_dijkstra_least_cost(self) -> tuple[list[list[list[float]]], list[list[list[list[Any]]]], float]:
        grid_snapshot = self.as_table

        directions = [1, 1j, -1, -1j]  # E, S, W, N
        start: complex = self.grid_agent_start
        goal: complex = self.grid_end
        start_orientation: int = directions.index(1 + 0j)  # E

        H = self.height
        W = self.width

        # Large cost for initialization
        INF = float('inf')

        # Distance array: dist[x][y][orientation]
        dist = [[[INF for _ in range(4)] for _ in range(W)] for _ in range(H)]

        # Parents array: For each (x,y,o), store a list of (px,py,po) states
        # that lead to (x,y,o) with the optimal known cost.
        parents = [[[[] for _ in range(4)] for _ in range(W)] for _ in range(H)]

        # Priority queue: entries are tuples (cost, x, y, orientation)
        pq = []

        # Initialize distance for the start state
        sx, sy = int(start.real), int(start.imag)
        gx, gy = int(goal.real), int(goal.imag)

        # Here we assume we have a known start_orientation:
        dist[sy][sx][start_orientation] = 0
        heapq.heappush(pq, (0, sx, sy, start_orientation))

        # Dijkstra's algorithm
        while pq:
            current_cost, x, y, orientation = heapq.heappop(pq)

            # If this is not the latest known best cost, skip
            if dist[y][x][orientation] < current_cost:
                continue

            # Check if goal reached (orientation doesn't matter at goal)
            gx, gy = int(goal.real), int(goal.imag)
            if (x, y) == (gx, gy):
                # We don't stop here because we want to ensure we have all equal-cost paths.
                # However, in a standard Dijkstra, we could stop now.
                pass

            # 1. Try moving forward
            orientation_complex = directions[orientation]
            orientation_complex_index = directions.index(orientation_complex)
            nx, ny = x + int(orientation_complex.real), y + int(orientation_complex.imag)

            if 0 <= nx < W and 0 <= ny < H and grid_snapshot[ny][nx].entity_type != "wall":
                new_cost = current_cost + 1
                if new_cost < dist[ny][nx][orientation_complex_index]:
                    dist[ny][nx][orientation_complex_index] = new_cost
                    parents[ny][nx][orientation_complex_index] = [(x, y, orientation)]  # Clear and set new parent
                    heapq.heappush(pq, (new_cost, nx, ny, orientation_complex_index))
                elif new_cost == dist[ny][nx][orientation_complex_index]:
                    parents[ny][nx][orientation_complex_index].append((x, y, orientation))

            # 2. Turn left
            left_orientation_complex = directions[orientation] * -1j
            left_orientation_complex_index = directions.index(left_orientation_complex)
            nx, ny = x + int(left_orientation_complex.real), y + int(left_orientation_complex.imag)

            if 0 <= nx < W and 0 <= ny < H and grid_snapshot[ny][nx].entity_type != "wall":
                new_cost = current_cost + 1000 + 1
                if new_cost < dist[y][x][left_orientation_complex_index]:
                    dist[ny][nx][left_orientation_complex_index] = new_cost
                    parents[ny][nx][left_orientation_complex_index] = [(x, y, orientation)]  # Clear and set new parent
                    heapq.heappush(pq, (new_cost, nx, ny, left_orientation_complex_index))
                elif new_cost == dist[ny][nx][left_orientation_complex_index]:
                    parents[ny][nx][left_orientation_complex_index].append((x, y, orientation))

            # 3. Turn right
            right_orientation_complex = directions[orientation] * +1j
            right_orientation_complex_index = directions.index(right_orientation_complex)
            nx, ny = x + int(right_orientation_complex.real), y + int(right_orientation_complex.imag)

            if 0 <= nx < W and 0 <= ny < H and grid_snapshot[ny][nx].entity_type != "wall":
                new_cost = current_cost + 1000 + 1
                if new_cost < dist[y][x][right_orientation_complex_index]:
                    dist[ny][nx][right_orientation_complex_index] = new_cost
                    parents[ny][nx][right_orientation_complex_index] = [(x, y, orientation)]  # Clear and set new parent
                    heapq.heappush(pq, (new_cost, nx, ny, right_orientation_complex_index))
                elif new_cost == dist[ny][nx][right_orientation_complex_index]:
                    parents[ny][nx][right_orientation_complex_index].append((x, y, orientation))

        # After Dijkstra finishes, find the minimal cost to reach the goal cell in any orientation
        min_cost = min(dist[gy][gx])

        return dist, parents, min_cost


def reconstruct_all_paths(parents, dist, goal):
    """
    Given the parents structure and dist, reconstruct all shortest paths from the start to the goal.
    goal: (gx, gy)
    Returns a list of paths, where each path is a list of (x,y,o) states in order.
    """

    gx, gy = goal
    # Find all orientations that achieve min_cost at goal
    min_cost = min(dist[gy][gx])
    best_orientations = [o for o in range(4) if dist[gy][gx][o] == min_cost]

    # We'll do a backtracking from goal states to start states
    all_paths = []

    def backtrack(x, y, o, current_path):
        # Prepend current node
        current_path.append((x, y, o))
        if len(parents[y][x][o]) == 0:
            # This means we are at the start state(s)
            # Reverse current path to get start->goal order
            all_paths.append(current_path[::-1])
            return
        # Explore all parents
        for (px, py, po) in parents[y][x][o]:
            backtrack(px, py, po, current_path[:])  # Pass a copy so each branch is independent

    for o in best_orientations:
        backtrack(gx, gy, o, [])

    return all_paths


def main(input, part=1, verbosity=False):
    grid = Grid(input)
    dist, parents, min_cost = grid.compute_dijkstra_least_cost()

    if min_cost == float('inf'):
        return None
    else:
        print("Minimal cost:", min_cost)
        all_paths = reconstruct_all_paths(parents, dist, (int(grid.grid_end.real), int(grid.grid_end.imag)))
        all_coords: set[tuple[int, int]] = {(x, y) for path in all_paths for x, y, _ in path}
        print("Number of unique states in all paths:", len(all_coords))

    return min_cost


if __name__ == '__main__':
    dinput = day16.demoinput
    dinput2 = day16.demoinput2
    input1 = day16.input1

    print(f"{main(dinput, part=1, verbosity=True) = }")
    # print(f"{main(dinput2, part=1, verbosity=True) = }")
    # print(f"{main(input1, part=1) = }")

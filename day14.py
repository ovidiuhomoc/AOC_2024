import os
from dataclasses import dataclass
from functools import cache

from PIL import Image

import day14

all_grids = []
pixel_size = 10


def are_grids_equal(grid1, grid2):
    for i in range(len(grid1)):
        if grid1[i] != grid2[i]:
            return False
    return True


@cache
def simulate_one_second_position(coords: tuple[int, int], velocity: tuple[int, int], grid_max: tuple[int, int]) -> tuple[int, int]:
    """Simulate a position of a robot after one second and if the new position should be outside the grid with x and y cells, it will wrap around"""
    grid_width, grid_tall = grid_max
    new_x = coords[0] + velocity[0]
    new_y = coords[1] + velocity[1]

    if new_x < 0:
        new_x = grid_width + new_x
    elif new_x > (grid_width - 1):
        new_x = new_x - grid_width

    if new_y < 0:
        new_y = grid_tall + new_y
    elif new_y > (grid_tall - 1):
        new_y = new_y - grid_tall

    return new_x, new_y


@dataclass
class Robot:
    coords: tuple[int, int]
    velocity: tuple[int, int]
    grid_max: tuple[int, int]

    def simulate_one_second(self):
        self.coords = simulate_one_second_position(self.coords, self.velocity, self.grid_max)


def print_robots_map(robots: list[Robot], grid_max: tuple[int, int], second: int):
    grid = [["." for _ in range(grid_max[0])] for _ in range(grid_max[1])]
    for robot in robots:
        grid[robot.coords[1]][robot.coords[0]] = "#"

    img_folder = 'day_14_images'
    os.makedirs(img_folder, exist_ok=True)
    output_path = os.path.join(img_folder, f'sec{second}.png')

    # Determine the size of the grid
    height = len(grid)
    width = max(len(row) for row in grid)

    # Create a new monochrome image (mode '1') or 'L' for grayscale
    img = Image.new('RGB', (width, height), color='black')  # Start with a black background
    pixels = img.load()

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '#':
                pixels[x, y] = (255, 255, 255)  # White pixel
            elif char == '.':
                pixels[x, y] = (0, 0, 0)  # Black pixel
            else:
                # Handle unexpected characters if necessary
                pixels[x, y] = (0, 0, 0)  # Default to black

        # If you want to scale up the image for better visibility
    if pixel_size > 1:
        img = img.resize((width * pixel_size, height * pixel_size), Image.NEAREST)

        # Save the image in PNG format (widely supported and lossless)
    img.save(output_path)
    print(f"Image saved to {output_path}")


def main(input, grid_max, part=1, seconds=100):
    robots = []
    for line in input.splitlines():
        start_coords = tuple(map(int, line.split(" v=")[0].split("p=")[1].strip().split(",")))
        start_velocity = tuple(map(int, line.split(" v=")[1].strip().split(",")))

        robots.append(Robot(coords=(start_coords[0], start_coords[1]),
                            velocity=(start_velocity[0], start_velocity[1]),
                            grid_max=grid_max))

    for i in range(seconds):
        for robot in robots:
            robot.simulate_one_second()
        if part == 2:
            print_robots_map(robots, grid_max, i)

    quadrant_limits = {1: [0, grid_max[0] // 2, 0, grid_max[1] // 2],
                       2: [grid_max[0] // 2 + 1, grid_max[0], 0, grid_max[1] // 2],
                       3: [0, grid_max[0] // 2, grid_max[1] // 2 + 1, grid_max[1]],
                       4: [grid_max[0] // 2 + 1, grid_max[0], grid_max[1] // 2 + 1, grid_max[1]]}

    quadrant_robots_count = {1: 0,
                             2: 0,
                             3: 0,
                             4: 0}

    for robot in robots:
        for quadrant, limits in quadrant_limits.items():
            if limits[0] <= robot.coords[0] < limits[1] and limits[2] <= robot.coords[1] < limits[3]:
                quadrant_robots_count[quadrant] += 1
                break

    safety_factor = 1
    for quadrant, count in quadrant_robots_count.items():
        print(f"{quadrant = }, {count = }")
        safety_factor *= count

    return safety_factor


if __name__ == '__main__':
    dgrid_max = (11, 7)
    dinput = day14.demoinput

    grid_max = (101, 103)
    input1 = day14.input1

    # print(f"{main(dinput,dgrid_max, part=1) = }")
    # print(f"{main(input1,grid_max, part=1) = }")
    print(f"{main(input1,grid_max, part=2, seconds=10000) = }")

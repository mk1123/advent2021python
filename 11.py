from aocd import lines  # type: ignore
import utils
from typing import Dict, Tuple, cast, List
import collections
import itertools

doing_part_a = False
actually_submit = True
sample = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

if not actually_submit:
    typed_lines = sample.split("\n")
else:
    typed_lines = cast(List[str], lines)

num_steps = 100
flash_count = 0
curr_flash_count = 0
grid = utils.parse_grid(typed_lines, "", int)
flashed: Dict[Tuple[int, int], bool] = collections.defaultdict(bool)


def flash_grid() -> int:
    global curr_flash_count
    curr_flash_count = 0
    for coord, val in grid.items():
        if val > 9:
            grid[coord] = 1
        else:
            grid[coord] += 1
    for coord in grid:
        if grid[coord] > 9 and not flashed[coord]:
            flash(coord)
    return curr_flash_count


def flash(coord: Tuple[int, int]) -> None:
    global curr_flash_count
    curr_flash_count += 1
    flashed[coord] = True
    for neighbor_coord, _ in utils.get_surrounding(coord, grid, True):
        grid[neighbor_coord] += 1
        if grid[neighbor_coord] > 9 and not flashed[neighbor_coord]:
            flash(neighbor_coord)


def a() -> int:
    for _ in range(num_steps):
        global flash_count
        flash_count += flash_grid()
        global flashed
        flashed = collections.defaultdict(bool)
    return flash_count


def b() -> int:
    for step in itertools.count():
        flash_grid()
        if curr_flash_count == len(grid):
            return step + 1
        global flashed
        flashed = collections.defaultdict(bool)
    return -1


utils.submit(a() if doing_part_a else b(), actually_submit)

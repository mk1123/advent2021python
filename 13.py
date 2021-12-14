from aocd import lines  # type: ignore
import utils
from typing import cast, List, Set, Tuple
import itertools

doing_part_a = False
actually_submit = True
sample = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

if not actually_submit:
    typed_lines = sample.split("\n")
else:
    typed_lines = cast(List[str], lines)


def all_dots_seq() -> List[Set[Tuple[int, int]]]:
    sep_idx = 0
    for idx, line in enumerate(typed_lines):
        if line == "":
            sep_idx = idx
            break
    coords, instructions = typed_lines[:sep_idx], typed_lines[sep_idx + 1 :]
    coords_set = set(
        (int((split := coord.split(","))[0]), int(split[1])) for coord in coords
    )
    all_dots = []
    print(coords_set)

    for instruction in instructions:
        instruction_lines = instruction.split()
        axis_type, axis_num = (third_split := instruction_lines[2].split("="))[0], int(
            third_split[1]
        )
        new_coord_set = set()
        if axis_type == "y":
            for x, y in coords_set:
                if y - axis_num > 0:
                    new_coord_set.add((x, axis_num - (y - axis_num)))
                else:
                    new_coord_set.add((x, y))
        else:
            for x, y in coords_set:
                if x - axis_num > 0:
                    new_coord_set.add((axis_num - (x - axis_num), y))
                else:
                    new_coord_set.add((x, y))
        all_dots.append(new_coord_set)
        print(new_coord_set)
        coords_set = new_coord_set

    return all_dots


def print_grid(grid: List[List[str]]) -> None:
    for line in grid:
        print(" ".join(line))


def a() -> int:
    return len(all_dots_seq()[0])


def b() -> str:
    all_dots = all_dots_seq()
    last_dots = all_dots[-1]
    print(last_dots)
    x_coords, y_coords = zip(*last_dots)
    x_max, y_max = max(x_coords) + 1, max(y_coords) + 1
    grid = [[" "] * x_max for _ in range(y_max)]
    for x, y in last_dots:
        grid[y][x] = "X"
    print_grid(grid)
    return "HECRZKPR"


utils.submit(a() if doing_part_a else b(), actually_submit)

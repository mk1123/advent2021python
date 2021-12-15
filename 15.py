from aocd import lines  # type: ignore
import utils
from typing import cast, List, Tuple, Dict
import heapq
import collections

doing_part_a = False
actually_submit = True
sample = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

if not actually_submit:
    typed_lines = sample.split("\n")
else:
    typed_lines = cast(List[str], lines)

rows, cols = len(typed_lines), len(typed_lines[0])
grid = utils.parse_grid(typed_lines, "", int)
goal = (rows - 1, cols - 1)
start = (0, 0)


def dist(coord: Tuple[int, int]) -> int:
    return goal[0] - coord[0] + goal[1] - coord[1]


def astar(grid: Dict[Tuple[int, int], int]) -> int:
    pq = [(dist(start), start)]  # (est_cost, coord)
    cost_so_far = {}
    cost_so_far[start] = 0
    while pq:
        _, curr_coord = heapq.heappop(pq)
        curr_cost = cost_so_far[curr_coord]
        if curr_coord == goal:
            return curr_cost
        for neigh_coord, neigh_val in utils.get_surrounding(curr_coord, grid):
            potential_cost = curr_cost + neigh_val
            if (
                neigh_coord not in cost_so_far
                or potential_cost < cost_so_far[neigh_coord]
            ):
                cost_so_far[neigh_coord] = potential_cost
                heapq.heappush(pq, (potential_cost + dist(neigh_coord), neigh_coord))
    return -1


def a() -> int:
    return astar(grid)


def clock_sum(a: int, b: int) -> int:
    _sum = a + b
    return _sum if _sum < 10 else _sum - 9


def enlarge_grid(grid: Dict[Tuple[int, int], int]) -> Dict[Tuple[int, int], int]:
    new_grid: Dict[Tuple[int, int], int] = {}
    for (x_coord, y_coord), val in grid.items():
        for i in range(5):
            for j in range(5):
                new_grid[(x_coord + i * rows, y_coord + j * cols)] = clock_sum(
                    val, i + j
                )
    global goal
    goal = (5 * rows - 1, 5 * cols - 1)
    return new_grid


def b() -> int:
    large_grid = enlarge_grid(grid)
    return astar(large_grid)


utils.submit(a() if doing_part_a else b(), actually_submit)

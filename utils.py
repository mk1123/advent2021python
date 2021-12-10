from aocd import submit as sbmt  # type: ignore
from typing import List, Any, Tuple


def int_map(lst: List[Any]) -> List[int]:
    return list(map(int, lst))


def get_surrounding(
    i: int, j: int, grid: List[List[Any]]
) -> List[Tuple[Tuple[int, int], Any]]:
    width, height = len(grid), len(grid[0])
    deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    res = []
    for dx, dy in deltas:
        if 0 <= (i + dx) < width and 0 <= (j + dy) < height:
            res.append(((i + dx, j + dy), grid[i + dx][j + dy]))
    return res


def submit(output: int, should_submit: bool = False) -> None:
    if should_submit:
        sbmt(output)
    else:
        print(output)

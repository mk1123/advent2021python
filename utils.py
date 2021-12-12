from aocd import submit as sbmt  # type: ignore
from typing import Callable, Dict, Generator, Generic, List, Any, Tuple, TypeVar
import itertools

T = TypeVar("T")


def int_map(lst: List[Any]) -> List[int]:
    return list(map(int, lst))


def get_surrounding(
    coord: Tuple[int, int], grid: Dict[Tuple[int, int], T], with_diagonal: bool = False
) -> List[Tuple[Tuple[int, int], T]]:
    i, j = coord
    deltas: List[Tuple[int, int]] = (
        [(-1, 0), (1, 0), (0, 1), (0, -1)]
        if not with_diagonal
        else [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, 1), (0, -1)]
    )
    res = []
    for dx, dy in deltas:
        if (new_coord := (i + dx, j + dy)) in grid:
            res.append((new_coord, grid[new_coord]))
    return res


def submit(output: int, should_submit: bool = False) -> None:
    if should_submit:
        sbmt(output)
    else:
        print(output)


def parse_grid(
    input: List[str], sep: str, map_func: Callable[[str], T]
) -> Dict[Tuple[int, int], T]:
    res: Dict[Tuple[int, int], T] = {}
    for i, line in enumerate(input):
        for j, letter in enumerate(line if not sep else line.split(sep)):
            res[(i, j)] = map_func(letter)
    return res


def dimensions_grid(grid: Dict[Tuple[int, int], T]) -> Tuple[int, int]:
    rows = 0
    for i in itertools.count():
        if (i, 0) not in grid:
            break
        rows += 1
    cols = 0
    for j in itertools.count():
        if (0, j) not in grid:
            break
        cols += 1
    return rows, cols


def print_grid(grid: Dict[Tuple[int, int], T]) -> None:
    rows, cols = dimensions_grid(grid)
    for i in range(rows):
        print([grid[(i, j)] for j in range(cols)])

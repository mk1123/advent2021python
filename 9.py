from typing import Deque
from aocd import lines
import utils

# sample = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678"""


def a():
    count = 0
    grid = [utils.int_map(list(line)) for line in lines]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            curr = grid[i][j]
            lowest = True
            for _, neighbor in utils.get_surrounding(i, j, grid):
                if neighbor <= curr:
                    lowest = False
                    break
            if lowest:
                count += curr + 1
    return count


def b():
    grid = [utils.int_map(list(line)) for line in lines]
    sizes = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            curr = grid[i][j]
            lowest = True
            for _, neighbor in utils.get_surrounding(i, j, grid):
                if neighbor <= curr:
                    lowest = False
                    break
            if lowest:
                # bfs
                queue = Deque([(i, j)])
                curr_basin = set()
                while queue:
                    coords = queue.popleft()
                    if coords in curr_basin:
                        continue
                    curr_basin.add(coords)
                    for neighbor_coord, neighbor_val in utils.get_surrounding(
                        coords[0], coords[1], grid
                    ):
                        if neighbor_val != 9:
                            queue.append(neighbor_coord)
                sizes.append(len(curr_basin))

    sizes.sort()
    # print(sizes)
    return sizes[-1] * sizes[-2] * sizes[-3]


utils.submit(b(), True)

from aocd import submit as sbmt


def int_map(lst):
    return list(map(int, lst))


def get_surrounding(i, j, grid):
    width, height = len(grid), len(grid[0])
    deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    res = []
    for dx, dy in deltas:
        if 0 <= (i + dx) < width and 0 <= (j + dy) < height:
            res.append(((i + dx, j + dy), grid[i + dx][j + dy]))
    return res


def submit(output, actually=False):
    if actually:
        sbmt(output)
    else:
        print(output)

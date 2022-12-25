def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        entries = [[i for i in j] for j in entries]
        return entries


def print_grid(g):
    for i in g:
        for j in i:
            print(j, end='')
        print()
    print()


def find_neighbours(grid, current):
    neighbours = []
    cx, cy = current
    current_elevation = ord(grid[cy][cx])
    if cx + 1 < len(grid[0]):
        new_elevation = ord(grid[cy][cx + 1])
        if new_elevation - current_elevation >= -1:
            neighbours.append((cx + 1, cy))
    if cx - 1 >= 0:
        new_elevation = ord(grid[cy][cx - 1])
        if new_elevation - current_elevation >= -1:
            neighbours.append((cx - 1, cy))
    if cy + 1 < len(grid):
        new_elevation = ord(grid[cy + 1][cx])
        if new_elevation - current_elevation >= -1:
            neighbours.append((cx, cy + 1))
    if cy - 1 >= 0:
        new_elevation = ord(grid[cy - 1][cx])
        if new_elevation - current_elevation >= -1:
            neighbours.append((cx, cy - 1))
    return neighbours


# reverse the problem:
# start at the end and then stop as soon as we are at elevation 'a'
def breadth_first_search(grid, target):
    q = []
    dist = [[-1 for i in j] for j in grid]
    # label target as explored
    tx, ty = target
    dist[ty][tx] = 0
    q.append(target)
    while len(q) != 0:
        vx, vy = q.pop(0)
        if grid[vy][vx] == 'a':
            return dist[vy][vx]
        for wx, wy in find_neighbours(grid, (vx, vy)):
            if dist[wy][wx] == -1:
                dist[wy][wx] = dist[vy][vx] + 1
                q.append((wx, wy))


def solve():
    heightmap = process_input()
    start = end = 0, 0
    for y in range(len(heightmap)):
        for x in range(len(heightmap[0])):
            if heightmap[y][x] == 'S':
                start = x, y
                heightmap[y][x] = 'a'
            elif heightmap[y][x] == 'E':
                end = x, y
                heightmap[y][x] = 'z'
    print_grid(heightmap)
    print(breadth_first_search(heightmap, end))


if __name__ == "__main__":
    solve()

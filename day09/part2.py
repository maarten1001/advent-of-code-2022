def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        return entries


def print_position(r, size, st_x, st_y):
    grid = [['.' for i in range(size)] for j in range(size)]
    grid[st_y][st_x] = 's'
    for i in range(len(r) - 1, 0, -1):
        x = r[i][0]
        y = r[i][1]
        # explicit conversion from int to str to make PyCharm shut up
        grid[y][x] = str(i)
    head_x = r[0][0]
    head_y = r[0][1]
    grid[head_y][head_x] = 'H'
    for i in range(size - 1, -1, -1):
        for j in range(size):
            print(grid[i][j], end='')
        print()
    print()


def print_visited(v, st_x, st_y):
    for i in range(len(v) - 1, -1, -1):
        for j in range(len(v[i])):
            if i == st_y and j == st_x:
                print('s', end='')
            elif v[i][j]:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


def follow_the_head(r):
    for i in range(1, len(r)):
        dx = r[i - 1][0] - r[i][0]
        dy = r[i - 1][1] - r[i][1]
        # check if we are already close enough
        if -1 <= dx <= 1 and -1 <= dy <= 1:
            continue
        if dx != 0:
            dx = dx // abs(dx)
        if dy != 0:
            dy = dy // abs(dy)
        r[i][0] += dx
        r[i][1] += dy
    return r


if __name__ == "__main__":
    grid_size = 1000
    rope_length = 10
    start_x = start_y = grid_size // 2
    rope = [[start_x, start_y] for i in range(rope_length)]
    visited = [[False for i in range(grid_size)] for j in range(grid_size)]
    visited[start_y][start_x] = True
    motions = process_input()
    # print("== Initial State ==")
    # print()
    # print_position(rope, grid_size, start_x, start_y)
    for line in motions:
        # print(f"== {line} ==")
        # print()
        direction, steps = line.split()
        for s in range(int(steps)):
            if direction == 'R':
                rope[0][0] += 1
            elif direction == 'L':
                rope[0][0] -= 1
            elif direction == 'U':
                rope[0][1] += 1
            elif direction == 'D':
                rope[0][1] -= 1
            rope = follow_the_head(rope)
            tail_x = rope[-1][0]
            tail_y = rope[-1][1]
            visited[tail_y][tail_x] = True
        # print_position(rope, grid_size, start_x, start_y)

    # print_visited(visited, start_x, start_y)
    print(sum(sum(i for i in j) for j in visited))

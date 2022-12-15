def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        return entries


def print_position(size):
    for i in range(size - 1, -1, -1):
        for j in range(size + 1):
            if Hy == i and Hx == j:
                print('H', end='')
            elif Ty == i and Tx == j:
                print('T', end='')
            elif i == 0 and j == 0:
                print('s', end='')
            else:
                print('.', end='')
        print()
    print()


def print_visited(v):
    for i in range(len(v) - 1, -1, -1):
        for j in range(len(v[i])):
            if i == 0 and j == 0:
                print('s', end='')
            elif v[i][j]:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


def follow_the_head(hx, hy, tx, ty):
    dx = hx - tx
    dy = hy - ty
    # check if we are already close enough
    if -1 <= dx <= 1 and -1 <= dy <= 1:
        return tx, ty
    if dx != 0:
        dx = dx // abs(dx)
    if dy != 0:
        dy = dy // abs(dy)
    return tx + dx, ty + dy


if __name__ == "__main__":
    grid_size = 1000
    Hx = Hy = grid_size // 2
    Tx = Ty = grid_size // 2
    visited = [[False for i in range(grid_size + 1)] for j in range(grid_size)]
    visited[Ty][Tx] = True
    motions = process_input()
    # print("== Initial State ==")
    # print()
    # print_position(grid_size)
    for line in motions:
        # print(f"== {line} ==")
        # print()
        direction, steps = line.split()
        for s in range(int(steps)):
            if direction == 'R':
                Hx += 1
            elif direction == 'L':
                Hx -= 1
            elif direction == 'U':
                Hy += 1
            elif direction == 'D':
                Hy -= 1
            Tx, Ty = follow_the_head(Hx, Hy, Tx, Ty)
            visited[Ty][Tx] = True
            # print_position(grid_size)

    # print_visited(visited)
    print(sum(sum(i for i in j) for j in visited))

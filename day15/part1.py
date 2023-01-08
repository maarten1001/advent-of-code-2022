def process_input():
    with open("test.txt") as f:
        entries = f.read().splitlines()
        coords = []
        for e in entries:
            pos = e.split('=')
            sx = int(pos[1][:pos[1].index(',')]) + 10
            sy = int(pos[2][:pos[2].index(':')]) + 10
            bx = int(pos[3][:pos[3].index(',')]) + 10
            by = int(pos[4]) + 10
            coords.append((sx, sy, bx, by))
        max_value = max(max(i for i in j) for j in coords)
        cave = [['.' for _ in range(2 * max_value + 1)] for _ in range(2 * max_value + 1)]
        for c in coords:
            sx, sy, bx, by = c
            cave[sy][sx] = 'S'
            cave[by][bx] = 'B'
        return cave, coords


def print_grid(g):
    for i in g:
        for j in i:
            print(j, end='')
        print()
    print()


def solve():
    cave, coords = process_input()
    for line in coords:
        sx, sy, bx, by = line
        manhattan = abs(sx - bx) + abs(sy - by)
        for y in range(sy - manhattan, sy + manhattan + 1):
            for x in range(sx - manhattan + abs(sy - y), sx + manhattan + 1 - abs(sy - y)):
                if cave[y][x] == '.':
                    cave[y][x] = '#'
    # print_grid(cave)
    # for x in cave[20]:
    #     print(x, end='')
    # print()
    print(sum([1 for x in cave[20] if x == '#']))


if __name__ == "__main__":
    solve()

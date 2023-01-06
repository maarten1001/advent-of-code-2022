def process_input(s):
    with open("input.txt") as f:
        entries = f.read().splitlines()
        max_value = max(max(max(int(i) for i in j.split(',')) for j in k.split(' -> ')) for k in entries)
        cave = [['.' for _ in range(max_value + 1)] for _ in range(max_value + 1)]
        cave[s[1]][s[0]] = '+'
        for line in entries:
            points = line.split(' -> ')
            for i in range(len(points) - 1):
                start_x, start_y = (int(x) for x in points[i].split(','))
                end_x, end_y = (int(x) for x in points[i + 1].split(','))
                dx = end_x - start_x
                dy = end_y - start_y
                x, y = start_x, start_y
                while (x, y) != (end_x, end_y):
                    cave[y][x] = '#'
                    if dx != 0:
                        x += dx // abs(dx)
                    if dy != 0:
                        y += dy // abs(dy)
                cave[end_y][end_x] = '#'
        return cave, max_value


def print_grid(g):
    for i in g:
        for j in i:
            print(j, end='')
        print()
    print()


def solve():
    sand_start = (500, 0)
    cave, max_value = process_input(sand_start)
    sand_count = 0
    sand_x, sand_y = sand_start
    while True:
        if cave[sand_y + 1][sand_x] == '.':
            sand_y += 1
        elif cave[sand_y + 1][sand_x - 1] == '.':
            sand_x -= 1
            sand_y += 1
        elif cave[sand_y + 1][sand_x + 1] == '.':
            sand_x += 1
            sand_y += 1
        else:
            cave[sand_y][sand_x] = 'o'
            sand_x, sand_y = sand_start
            sand_count += 1
        if sand_y >= max_value - 1:
            # print_grid(cave)
            print(sand_count)
            break


if __name__ == "__main__":
    solve()

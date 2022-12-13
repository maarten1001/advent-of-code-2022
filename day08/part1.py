def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        entries = [[int(i) for i in j] for j in entries]
        return entries


def print_grid(g):
    for i in g:
        for j in i:
            print(j, end='')
        print()
    print()


if __name__ == "__main__":
    trees = process_input()
    visible = [[0 for i in j] for j in trees]
    for i in range(len(trees)):
        # left to right
        h = -1
        for j in range(len(trees[0])):
            if trees[i][j] > h:
                visible[i][j] = 1
                h = trees[i][j]
        # right to left
        h = -1
        for j in range(len(trees[0])-1, -1, -1):
            if trees[i][j] > h:
                visible[i][j] = 1
                h = trees[i][j]
    for j in range(len(trees[0])):
        # top to bottom
        h = -1
        for i in range(len(trees)):
            if trees[i][j] > h:
                visible[i][j] = 1
                h = trees[i][j]
        # bottom to top
        h = -1
        for i in range(len(trees)-1, -1, -1):
            if trees[i][j] > h:
                visible[i][j] = 1
                h = trees[i][j]

    total = sum(sum(i for i in j) for j in visible)
    print(total)

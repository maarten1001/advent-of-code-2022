def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        entries = [[int(ii) for ii in jj] for jj in entries]
        return entries


def print_grid(g):
    for ii in g:
        for jj in ii:
            print(jj, end='')
        print()
    print()


if __name__ == "__main__":
    trees = process_input()
    highest = 0
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            score = 1
            # looking right
            view = 0
            for k in range(j + 1, len(trees[i])):
                view += 1
                if trees[i][k] >= trees[i][j]:
                    break
            score *= view
            # looking left
            view = 0
            for k in range(j - 1, -1, -1):
                view += 1
                if trees[i][k] >= trees[i][j]:
                    break
            score *= view
            # looking down
            view = 0
            for k in range(i + 1, len(trees)):
                view += 1
                if trees[k][j] >= trees[i][j]:
                    break
            score *= view
            # looking up
            view = 0
            for k in range(i - 1, -1, -1):
                view += 1
                if trees[k][j] >= trees[i][j]:
                    break
            score *= view
            if score > highest:
                highest = score

    print(highest)

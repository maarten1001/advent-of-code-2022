with open("input.txt") as f:
    entries = f.read().splitlines()

cleanup = []
for e in entries:
    elves = e.split(',')
    for el in elves:
        x = el.split('-')
        start = int(x[0])
        end = int(x[1]) + 1
        assignment = {x for x in range(start, end)}
        cleanup.append(assignment)

total = 0
for i in range(0, len(cleanup) - 1, 2):
    x = cleanup[i]
    y = cleanup[i + 1]
    if x.issubset(y) or y.issubset(x):
        total += 1
print(total)

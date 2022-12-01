with open("input.txt") as f:
    entries = f.read().splitlines()

most = 0
total = 0
elves = []

for e in entries:
    if e == '':
        elves.append(total)
        total = 0
        continue
    total += int(e)
elves.append(total)

elves.sort()
print(sum(elves[-3:]))

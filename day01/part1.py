with open("input.txt") as f:
    entries = f.read().splitlines()

most = 0
total = 0

for e in entries:
    if e == '':
        if total > most:
            most = total
        total = 0
        continue
    total += int(e)

print(most)

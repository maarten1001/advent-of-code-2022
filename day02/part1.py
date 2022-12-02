with open("input.txt") as f:
    entries = f.read().splitlines()

decrypt = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

score = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
    "lost": 0,
    "draw": 3,
    "won": 6
}

total = 0
for e in entries:
    line = e.split()
    opponent = decrypt[line[0]]
    you = decrypt[line[1]]
    total += score[you]
    if opponent == you:
        total += score["draw"]
    elif opponent == "rock":
        if you == "paper":
            total += score["won"]
        elif you == "scissors":
            total += score["lost"]
    elif opponent == "paper":
        if you == "rock":
            total += score["lost"]
        elif you == "scissors":
            total += score["won"]
    elif opponent == "scissors":
        if you == "rock":
            total += score["won"]
        elif you == "paper":
            total += score["lost"]

print(total)

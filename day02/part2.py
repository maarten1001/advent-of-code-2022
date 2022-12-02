with open("input.txt") as f:
    entries = f.read().splitlines()

decrypt = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

score = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
    "lose": 0,
    "draw": 3,
    "win": 6
}

total = 0
for e in entries:
    line = e.split()
    opponent = decrypt[line[0]]
    action = decrypt[line[1]]
    total += score[action]
    if action == "draw":
        total += score[opponent]
    elif opponent == "rock":
        if action == "win":
            total += score["paper"]
        elif action == "lose":
            total += score["scissors"]
    elif opponent == "paper":
        if action == "win":
            total += score["scissors"]
        elif action == "lose":
            total += score["rock"]
    elif opponent == "scissors":
        if action == "win":
            total += score["rock"]
        elif action == "lose":
            total += score["paper"]

print(total)

def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        sensors = []
        beacons = []
        manhattan = []
        for e in entries:
            pos = e.split('=')
            sx = int(pos[1][:pos[1].index(',')])
            sy = int(pos[2][:pos[2].index(':')])
            bx = int(pos[3][:pos[3].index(',')])
            by = int(pos[4])
            sensors.append((sx, sy))
            beacons.append((bx, by))
            distance_to_closest_beacon = abs(sx - bx) + abs(sy - by)
            manhattan.append(distance_to_closest_beacon)
        return sensors, beacons, manhattan


def can_contain_beacon(sensors, beacons, manhattan, test):
    if test in beacons:
        return True
    for i in range(len(sensors)):
        sx, sy = sensors[i]
        tx, ty = test
        distance_to_closest_beacon = manhattan[i]
        distance_to_test = abs(sx - tx) + abs(sy - ty)
        if distance_to_test <= distance_to_closest_beacon:
            return False
    return True


def solve():
    sensors, beacons, manhattan = process_input()
    total = 0
    target = 2000000
    min_x = max_x = target
    for i in range(len(sensors)):
        sx, sy = sensors[i]
        if sx - manhattan[i] < min_x:
            min_x = sx - manhattan[i]
        if sx + manhattan[i] > max_x:
            max_x = sx + manhattan[i]
    for i in range(min_x, max_x):
        total += not can_contain_beacon(sensors, beacons, manhattan, (i, target))
    print(total)


if __name__ == "__main__":
    solve()

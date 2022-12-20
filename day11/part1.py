def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        monkey_list = []
        for i in range(0, len(entries), 7):
            items = entries[i + 1][18:]
            items = items.replace(',', '').split()
            items = [int(x) for x in items]
            operation = entries[i + 2][19:].split()
            divisible = int(entries[i + 3][21:])
            true = int(entries[i + 4][29:])
            false = int(entries[i + 5][30:])
            monkey_list.append(Monkey(items, operation, divisible, true, false))
        return monkey_list


class Monkey:
    def __init__(self, items, operation, divisible, true, false):
        self.items = items
        self.operation = operation
        self.divisible = divisible
        self.true = true
        self.false = false
        self.inspections = 0

    def inspect(self, i):
        # print(f"  Monkey inspects an item with a worry level of {self.items[i]}.")
        self.inspections += 1
        a = self.operation[0]
        op = self.operation[1]
        b = self.operation[2]
        if a == 'old':
            a = self.items[i]
        else:
            a = int(a)
        if b == 'old':
            # b_text = 'itself'
            b = self.items[i]
        else:
            # b_text = b
            b = int(b)

        if op == '*':
            self.items[i] = a * b
            # print(f"    Worry level is multiplied by {b_text} to {self.items[i]}.")
        elif op == '+':
            self.items[i] = a + b
            # print(f"    Worry level increases by {b_text} to {self.items[i]}.")
        else:
            raise Exception(f"Unknown operation {op}")

    def bored(self, i):
        self.items[i] //= 3
        # print(f"    Monkey gets bored with item. Worry level is divided by 3 to {self.items[i]}.")

    def test(self, i):
        result = self.items[i] % self.divisible
        if result == 0:
            # print(f"    Current worry level is divisible by {self.divisible}.")
            return True
        else:
            # print(f"    Current worry level is not divisible by {self.divisible}.")
            return False

    def throw(self, monkey_list, i, target=None):
        if target is None:
            result = self.test(i)
            if result:
                target = self.true
            else:
                target = self.false
        # print(f"    Item with worry level {self.items[i]} is thrown to monkey {target}.")
        monkey_list[target].catch(self.items[i])
        self.items.pop(i)

    def catch(self, item):
        self.items.append(item)


if __name__ == "__main__":
    monkeys = process_input()
    for ii in range(1, 20 + 1):
        # print(f"Start of round {ii}")
        for m in range(len(monkeys)):
            # print(f"Monkey {m}:")
            while len(monkeys[m].items) > 0:
                monkeys[m].inspect(0)
                monkeys[m].bored(0)
                monkeys[m].throw(monkeys, 0)
        print(f"End of round {ii}")
        for m in range(len(monkeys)):
            strings = [str(x) for x in monkeys[m].items]
            print(f"Monkey {m}: " + ', '.join(strings))
        print()
        for m in range(len(monkeys)):
            print(f"Monkey {m} inspected items {monkeys[m].inspections} times.")
        print()
    monkey_business = []
    for m in range(len(monkeys)):
        monkey_business.append(monkeys[m].inspections)
    monkey_business.sort()
    print(monkey_business[-1] * monkey_business[-2])

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

    def inspect(self):
        # print(f"  Monkey inspects an item with a worry level of {self.items[i]}.")
        self.inspections += 1
        a = self.operation[0]
        op = self.operation[1]
        b = self.operation[2]
        if a == 'old':
            a = self.items[0]
        else:
            a = int(a)
        if b == 'old':
            # b_text = 'itself'
            b = self.items[0]
        else:
            # b_text = b
            b = int(b)

        if op == '*':
            self.items[0] = a * b
            # print(f"    Worry level is multiplied by {b_text} to {self.items[i]}.")
        elif op == '+':
            self.items[0] = a + b
            # print(f"    Worry level increases by {b_text} to {self.items[i]}.")
        else:
            raise Exception(f"Unknown operation {op}")

    def bored(self, lim):
        # self.items[0] //= 3
        self.items[0] %= lim
        # print(f"    Monkey gets bored with item. Worry level is divided by 3 to {self.items[i]}.")

    def test(self):
        result = self.items[0] % self.divisible
        if result == 0:
            # print(f"    Current worry level is divisible by {self.divisible}.")
            return True
        else:
            # print(f"    Current worry level is not divisible by {self.divisible}.")
            return False

    def throw(self, monkey_list, target=None):
        if target is None:
            result = self.test()
            if result:
                target = self.true
            else:
                target = self.false
        # print(f"    Item with worry level {self.items[i]} is thrown to monkey {target}.")
        monkey_list[target].catch(self.items[0])
        self.items.pop(0)

    def catch(self, item):
        self.items.append(item)


if __name__ == "__main__":
    monkeys = process_input()
    limit = 1
    # The LCM of two or more prime numbers is equal to their product
    for monkey in monkeys:
        limit *= monkey.divisible
    for rounds in range(1, 10000 + 1):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                monkey.inspect()
                monkey.bored(limit)
                monkey.throw(monkeys)
        if rounds % 1000 == 0:
            print(f"== After round {rounds} ==")
            for m, monkey in enumerate(monkeys):
                print(f"Monkey {m} inspected items {monkey.inspections} times.")
            print()
    monkey_business = [m.inspections for m in monkeys]
    monkey_business.sort()
    print(monkey_business[-1] * monkey_business[-2])

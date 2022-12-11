def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        return entries


class Node:
    def __init__(self, name, is_file, parent, size=0):
        self.name = name
        self.is_file = is_file
        self.size = size
        self.parent = parent
        self.children = []

    def __str__(self):
        return self.name

    def print(self):
        for listy in self.ls():
            print(listy)

    def ls(self):
        content_list = []
        if self.is_file:
            content_list.append(f"- {self.name} (file, size={self.size})")
        else:
            content_list.append(f"- {self.name} (dir)")
            for c in self.children:
                child_list = c.ls()
                for cl in child_list:
                    content_list.append("  " + cl)
        return content_list

    def cd(self, target):
        if target == '/':
            return root
        elif target == "..":
            return self.parent
        else:
            for c in self.children:
                if c.name == target:
                    return c
            raise Exception(f"Unknown directory {target}, cwd is {cwd}")

    def get_size(self):
        if self.is_file:
            return self.size
        else:
            return sum([c.get_size() for c in self.children])


if __name__ == "__main__":
    root = Node("/", False, None)
    cwd = root
    directory_list = [root]
    terminal = process_input()
    for line in terminal:
        line = line.split()
        if line[0] == '$':
            command = line[1]
            if command == "cd":
                cwd = cwd.cd(line[2])
            elif command == "ls":
                pass
            else:
                raise Exception(f"Unknown command {command}")
        else:
            if line[0] == "dir":
                new_node = Node(line[1], False, cwd)
                directory_list.append(new_node)
            else:
                new_node = Node(line[1], True, cwd, int(line[0]))
            cwd.children.append(new_node)

    root.print()
    print()

    total_disk_space = 70000000
    needed_disk_space = 30000000
    free_disk_space = total_disk_space - root.get_size()
    minimum_directory_size = needed_disk_space - free_disk_space
    if free_disk_space > needed_disk_space:
        print(f"Sufficient disk space available. Need {needed_disk_space}, {free_disk_space} available")
    else:
        size_list = []
        for d in directory_list:
            d_size = d.get_size()
            if d_size >= minimum_directory_size:
                size_list.append(d_size)
        print(min(size_list))

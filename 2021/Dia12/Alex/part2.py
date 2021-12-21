with open("input.dat") as f:
    data = [l.replace("\n", "") for l in f.readlines()]

connections = {}
no_repeat_nodes = []

for item in data:
    splited = item.split("-")
    for i in range(2):
        if splited[i] not in connections.keys():
            connections[splited[i]] = [splited[abs(i - 1)]]
        else:
            connections[splited[i]].append(splited[abs(i - 1)])
        if splited[i].islower() and splited[i] not in no_repeat_nodes:
            no_repeat_nodes.append(splited[i])

counter = 0


def para_alex_con_amor(path: list) -> None:
    global counter
    paths = []
    for item in connections[path[-1]]:
        new_path = [*path, item]
        if is_ended(new_path):
            counter += 1
        else:
            if is_valid(new_path):
                paths.append(new_path)
    for path in paths:
        para_alex_con_amor(path)


def is_valid(path: list) -> bool:
    if path[-1] == "start":
        return False

    twice_visited = False
    for danger in no_repeat_nodes:
        if path.count(danger) > 2:
            return False
        if path.count(danger) == 2:
            if not twice_visited:
                twice_visited = True
            else:
                return False

    return True


def is_ended(path: list) -> bool:
    return path[-1] == "end"


para_alex_con_amor(["start"])
print(counter)

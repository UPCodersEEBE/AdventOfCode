with open("input.dat", "r") as f:
    data = [int(pos) for pos in f.readlines()[0].split(",")]


def calculate_cost(pos: int) -> int:
    res = 0
    for crab in data:
        dist = abs(pos - crab)
        res += (dist * (dist + 1)) // 2
    return res


min_pos = min(data)
max_pos = max(data)
lowest_cost = calculate_cost(min_pos)

for i in range(min_pos + 1, max_pos):
    lowest_cost = min(lowest_cost, calculate_cost(i))

print(lowest_cost)

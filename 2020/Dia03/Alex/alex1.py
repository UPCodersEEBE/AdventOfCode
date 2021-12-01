with open("day3") as f:
    trees = [line.split("\n")[0] for line in f]

size = len(trees[0])


def slopes(mov):
    dx = mov[0]
    dy = mov[1]
    tcount = 0
    for i in range(len(trees) / dy):
        n = i * dx - size * ((dx * i) // size)
        if trees[dy * i][n] == "#":
            tcount += 1
    if dy > 1:
        tcount += 1
    return tcount


slope = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

end = 1

for s in range(len(slope)):
    end *= slopes(slope[s])

print(end)
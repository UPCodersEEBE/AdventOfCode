with open("day3") as f:
    trees = [line.split("\n")[0] for line in f]

size = len(trees[0])

tcount = 0
for i in range(len(trees)):
    n = i * 3 - size * ((3 * i) // size)
    print(n, trees[i][n])
    if trees[i][n] == "#":
        tcount += 1

print(tcount)

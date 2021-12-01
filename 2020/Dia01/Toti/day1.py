def EntityFinder2numsum(report):
    x = 0
    for i in report:
        for j in report:
            if i != j and (i+j == 2020):
                return i*j
            else:
                continue

def EntityFinder3numsum(report):
    x = 0
    for i in report:
        for j in report:
            for k in report:
                if i != j and i != k and k != j and (i+j+k == 2020):
                    return i*j*k
                else:
                    continue

# l= []
# with open("day1list.txt", "r") as f:
#     for line in f:
#         l.append(int(line.split("\n")[0]))

l = [int(line.split("\n")[0]) for line in open("day1list.txt", "r")]

print(EntityFinder2numsum(l))
print(EntityFinder3numsum(l))
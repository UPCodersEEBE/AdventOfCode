def FindPos(l):
    h = 0
    d = 0
    for i in l:
        if i[0] == "forward":
            h += int(i[1])
        elif i[0] == "down":
            d += int(i[1])
        else:
            d -= int(i[1])
    return (h, d)

def FindPos2(l):
    a = 0
    h = 0
    d = 0
    for i in l:
        if i[0] == "down":
            a += int(i[1])
        elif i[0] == "up":
            a -= int(i[1])
        else:
            h += int(i[1])
            d += a*int(i[1])
    return (h, d)
l = [(line.split("\n")[0]).split() for line in open("input2.txt", "r")]

print(FindPos2(l))
print(FindPos2(l)[0] * FindPos2(l)[1])
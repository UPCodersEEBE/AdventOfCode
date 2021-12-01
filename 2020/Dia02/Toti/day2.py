def IsPasswordValid1(line):
    min = int(line.split(" ")[0].split("-")[0])
    max = int(line.split(" ")[0].split("-")[1])
    letter = line.split(" ")[1][0]
    password = line.split(" ")[2]

    count = 0
    for i in password:
        if i == letter:
            count += 1

    return count >= min and count <= max

def IsPasswordValid2(line):
    pos1 = int(line.split(" ")[0].split("-")[0]) - 1
    pos2 = int(line.split(" ")[0].split("-")[1]) - 1
    letter = line.split(" ")[1][0]
    password = line.split(" ")[2]

    return  ((password[pos1] == letter and password[pos2] != letter) or
            (password[pos2] == letter and password[pos1] != letter))
    

    

l = [line.split("\n")[0] for line in open("day2list.txt", "r")]

c1 = 0
c2 = 0
for i in l:
    if IsPasswordValid1(i):
        c1 += 1
    if IsPasswordValid2(i):
        c2 += 1

print(c1, c2)


c = 0

with open("d2pr1.dat") as f:
    for line in f:
        content = line.split()
        minmax = content[0].split("-")
        letter = content[1].split(":")[0]
        password = content[2]
        count = password.count(letter)
        if count >= int(minmax[0]) and count <= int(minmax[1]):
            c += 1
print(c)

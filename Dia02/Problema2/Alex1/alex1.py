c = 0

with open("d2pr2.dat") as f:
    for line in f:
        content = line.split()
        minmax = content[0].split("-")
        letter = content[1].split(":")[0]
        password = content[2]
        count = password.count(letter)
        if bool(password[int(minmax[0]) - 1] == letter) != bool(
            count <= password[int(minmax[1]) - 1] == letter
        ):
            c += 1
print(c)

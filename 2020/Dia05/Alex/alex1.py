seats = [line.split("\n")[0] for line in open("d5p1.dat", "r")]


def seatid(seat):
    row = seat[:7]
    rown = 0
    for i in range(7):
        if row[i] == "B":
            rown += 2 ** (6 - i)
    col = seat[-3:]
    coln = 0
    for i in range(3):
        if col[i] == "R":
            coln += 2 ** (2 - i)
    return rown * 8 + coln


ids = []
for seat in seats:
    ids.append(seatid(seat))

print(max(ids))

for i in range(min(ids), max(ids)):
    if i not in ids:
        print(i)
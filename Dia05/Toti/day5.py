# def getRowAndCol(bp):
#     bin = bp
#     bin = bin.replace("B" , "1")
#     bin = bin.replace("F", "0")
#     bin = bin.replace("L", "0")
#     bin = bin.replace("R", "1")
#     return(int(bin[:7], 2), int(bin[7:], 2))

def getRow(bp):
    l = 0
    u = 127

    for i in bp[:-4]:
        if i == "F":
            u = l + (u - l) // 2
        else:
            l = l + (u - l) // 2  + 1

    return(l if bp[6] == "F" else u)

def getColumn(bp):
    l = 0
    u = 7

    for i in bp[7:-1]:
        if i == "L":
            u = l + (u - l) // 2
        else:
            l = l + (u - l) // 2  + 1

    return(l if bp[9] == "L" else u)

def getSeatID(bp):
    row = getRow(bp)
    column = getColumn(bp)

    return(row * 8 + column)

def getEverything(bp):
    return(f"Row: {getRow(bp)} Column: {getColumn(bp)} ID: {getSeatID(bp)}")

l = [line.split("\n")[0] for line in open("day5input.txt", "r")]

IDs = []
for bp in l:
    IDs.append(getSeatID(bp))
print(max(IDs))

seatsInInput = []
for i in l:
    seatsInInput.append(f"{getRow(i)},{getColumn(i)},{getSeatID(i)}")

allSeats = []
for i in range(128):
    for j in range(8):
        allSeats.append(f"{i},{j},{i*8 +j}")

difSeats = [i for i in allSeats if i not in seatsInInput]

print(difSeats)


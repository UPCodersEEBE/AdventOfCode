def AcomulatorAndPassedLast(l):
    index = 0
    acc = 0
    AlreadySeenIndexes = []
    while True:
        if index not in AlreadySeenIndexes:
            AlreadySeenIndexes.append(index) 
        else: break
        if l[index][0] == "acc":
            if l[index][1][0] == "+":
                acc += int(l[index][1][1:])
            else:
                acc -= int(l[index][1][1:])
            index +=1 
        elif l[index][0] == "jmp":
            if l[index][1][0] == "+":
                index += int(l[index][1][1:])
            else:
                index -= int(l[index][1][1:])
        else:
            index += 1

        if index == len(l):
            return(acc, True)
    return(acc, False)

l = [line.split("\n")[0].split(" ") for line in open("day8input.txt", "r")]
print(AcomulatorAndPassedLast(l)[0])

for i in range(len(l)):
    lcopy = []
    if l[i][0] == "jmp":
        lcopy = l[:i]+ [["nop", l[i][1]]] + l[i+1:]
    elif l[i][0] == "nop":
        lcopy = l[:i]+ [["jmp", l[i][1]]] + l[i+1:]
        
    try:
        if AcomulatorAndPassedLast(lcopy)[1]:
            print(AcomulatorAndPassedLast(lcopy)[0])
    except:
        continue



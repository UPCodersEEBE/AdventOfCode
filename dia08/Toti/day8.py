l = [line.split("\n")[0].split(" ") for line in open("day8input.txt", "r")]

print(l)

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

print(acc)
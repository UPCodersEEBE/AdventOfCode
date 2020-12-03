def TreesEncounters(map, right, down):
    Patternlen = len(map[0])
    TreesEncounters = 0

    ypos = 0
    xpos = 0

    while True:
        if map[ypos][xpos] == "#":
            TreesEncounters +=1
        
        ypos += down
        xpos += right
        
        if xpos >= Patternlen:
            xpos -= Patternlen 

        if ypos >= len(map):
            break

    return TreesEncounters

l = [line.split("\n")[0] for line in open("day3puzzleinput.txt", "r")]

print(TreesEncounters(l,3,1)) #prob1

slopes =    [TreesEncounters(l,1,1), TreesEncounters(l,3,1), TreesEncounters(l,5,1),
            TreesEncounters(l,7,1), TreesEncounters(l,1,2)]
x = 1
for i in slopes:
    x *= i

print(x) #prob2



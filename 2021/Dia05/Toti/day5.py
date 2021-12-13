def FindNoRowsAndCols(lines):
    r = 0
    c = 0
    for i in lines:
        if i[0] == 'v':
            if i[1] > c:
                c = i[1]
            if i[2] > r:
                r = i[2]
            if i[3] > r:
                r = i[3]
        if i[0] == 'h':
            if i[1] > r:
                r = i[1]
            if i[2] > c:
                c = i[2]
            if i[3] > c:
                c = i[3]
    return(r,c)

def CreateEmptyDiagram(r,c):
    diagram = []
    for i in range(r+1):
        row = []
        for j in range(c+1):
            row.append('.')
        diagram.append(row)
    return diagram


def DrawLinesHandV(diagram, line):
    NewDiagram = diagram
    if line[0] == 'h':
        for i in range(abs(line[3]-line[2])+1):
            if line[3]>=line[2]:
                if NewDiagram[line[1]][line[2]+i] == '.':
                    NewDiagram[line[1]][line[2]+i] = 1
                else:
                    NewDiagram[line[1]][line[2]+i] += 1
            else:
                if NewDiagram[line[1]][line[3]+i] == '.':
                    NewDiagram[line[1]][line[3]+i] = 1
                else:
                    NewDiagram[line[1]][line[3]+i] += 1  
    elif line[0] == 'v':
        for i in range(abs(line[3]-line[2])+1):
            if line[3]>=line[2]:
                if NewDiagram[line[2]+i][line[1]] == '.':
                    NewDiagram[line[2]+i][line[1]] = 1
                else:
                    NewDiagram[line[2]+i][line[1]] += 1
            else:
                if NewDiagram[line[3]+i][line[1]] == '.':
                    NewDiagram[line[3]+i][line[1]] = 1
                else:
                    NewDiagram[line[3]+i][line[1]] += 1  
    
    return(NewDiagram)

def DrawLinesD(diagram, line):
    NewDiagram = diagram
    if line[0] == 'd':
        for i in range(abs(line[3]-line[1])+1):
            try:
                if line[4]>=line[2] and line[3]>=line[1]:
                    if NewDiagram[line[1]+i][line[2]+i] == '.':
                        NewDiagram[line[1]+i][line[2]+i] = 1
                    else:
                        NewDiagram[line[1]+i][line[2]+i] += 1
                elif line[4]<=line[2] and line[3]<=line[1]:
                    if NewDiagram[line[3]+i][line[4]+i] == '.':
                        NewDiagram[line[3]+i][line[4]+i] = 1
                    else:
                        NewDiagram[line[3]+i][line[4]+i] += 1
                
                elif line[4]<=line[2] and line[3]>=line[1]:
                    if NewDiagram[line[1]+i][line[2]-i] == '.':
                        NewDiagram[line[1]+i][line[2]-i] = 1
                    else:
                        NewDiagram[line[1]+i][line[2]-i] += 1

                elif line[4]>=line[2] and line[3]<=line[1]:
                    if NewDiagram[line[3]+i][line[4]-i] == '.':
                        NewDiagram[line[3]+i][line[4]-i] = 1
                    else:
                        NewDiagram[line[3]+i][line[4]-i] += 1
            except:
                continue
    
    return(NewDiagram)

def CountIntersections(diagram):
    c = 0
    for i in diagram:
        for j in i:
            if j != '.':
                if j > 1:
                    c += 1
    return c

def LineDef(line):
    x1, y1 = int(line[0].split(',')[0]), int(line[0].split(',')[1])
    x2, y2 = int(line[1].split(',')[0]), int(line[1].split(',')[1])
    if x1 == x2:
        return('v', x1, y1, y2)
    elif y1 == y2:
        return('h', y1, x1, x2)
    else:
        return('d', x1, y1, x2, y2)


lines = [line.split("\n")[0].split(' -> ') for line in open("input5.txt", "r")]
for i in range(len(lines)):
    lines[i] = LineDef(lines[i])

diagram = CreateEmptyDiagram(FindNoRowsAndCols(lines)[0],FindNoRowsAndCols(lines)[1])

for line in lines:
    diagram = DrawLinesHandV(diagram, line)


print('Resultat 1:', CountIntersections(diagram))

for line in lines:
    diagram = DrawLinesD(diagram, line)

print('Resultat 2:',CountIntersections(diagram))










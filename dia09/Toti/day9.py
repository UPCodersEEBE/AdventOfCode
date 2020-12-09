l = [int(line.split("\n")[0]) for line in open("day9input.txt", "r")]

def CheckTwoNumSum(num, preambleList):
    for i in preambleList:
        for j in preambleList:
            if i != j and (i+j ==  num):
                return True
            else:
                continue
    return False

def TrobarSubLlista(num, l):
    for i in range(len(l)):
        tamanyLlista = 2
        while True:
            if sum(l[i:tamanyLlista]) < answer1:
                tamanyLlista +=1
            elif sum(l[i:tamanyLlista]) > answer1:
                break
            else:
                return l[i:tamanyLlista]

notProperty = []
for i in range(25, len(l)):
    if not CheckTwoNumSum(l[i], l[i-25:i]):
        notProperty.append(l[i])

answer1 = notProperty[0]

print(answer1)     

print(max(TrobarSubLlista(answer1, l))+ min(TrobarSubLlista(answer1, l)))





    

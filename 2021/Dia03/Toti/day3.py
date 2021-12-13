def GetGammaAndEpsilonRate(l):
    gamma = ''
    c = 0
    for i in range(len(l[0])):
        for j in l:
            if j[i] == '1':
                c += 1

        if c >= len(l)/2:
            gamma += '1' 
        else:
            gamma += '0'
        c = 0

    epsilon = ''
    for i in gamma:
        if i == '0':
            epsilon += '1'
        else:
            epsilon += '0'

    return epsilon, gamma

def GetOxigenRating(l):
    aux1 = l
    aux2 = []
    a = ''
    c = 0
    
    for i in range(len(l[0])):
        for j in aux1:
            if j[i] == '1':
                c += 1

        if c >= len(aux1)/2:
            a = '1' 
        else:
            a = '0'
        c = 0
        for j in aux1:
            if j[i] == a:
                aux2.append(j)
        aux1 = aux2
        aux2 = []

    return aux1[0]

def GetCO2Rating(l):
    aux1 = l
    aux2 = []
    a = ''
    c = 0
    
    for i in range(len(l[0])):
        for j in aux1:
            if j[i] == '1':
                c += 1

        if c >= len(aux1)/2:
            a = '0' 
        else:
            a = '1'
        c = 0
        for j in aux1:
            if j[i] == a:
                aux2.append(j)
        aux1 = aux2
        aux2 = []

        if len(aux1) == 1:
            return aux1[0]


    return aux1[0]


l = [line.split("\n")[0] for line in open("input3.txt", "r")]

print(int(GetGammaAndEpsilonRate(l)[0],2)*int(GetGammaAndEpsilonRate(l)[1],2))

print(int(GetOxigenRating(l),2)*int(GetCO2Rating(l),2))

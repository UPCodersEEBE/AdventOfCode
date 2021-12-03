with open("input.txt") as n:
    array = []
    for i in n:
        array.append(str(i).rstrip("\n"))

#Parte 1
        
gamma = ''
count =0
for i in range(len(array[0])):
    for j in range(len(array)):
        if array[j][i] =='1':
            count +=1
        if (count/len(array))>0.5:
            gamma +='1'
            count = 0
            break
        elif j==len(array)-1:
            gamma +='0'
            count =0
epsilon=''
for j in gamma:
    if j=='0':
        epsilon +='1'
    else:
        epsilon +='0'
        
print(int(gamma,2)*int(epsilon,2))



#Part 2

count = 0
common ='' +gamma[0]
cuenta =0
number = 0
nova_llista = []
nova_llista +=array


###### CAS PER A TROBAR LLISTA MAXIMA '__'
def actualitzacio(array):
    llista = []
    for s in range(len(array)):
        if array[s][number]==common[-1]:
            llista.append(array[s])
    return llista

for i in range(len(array[0])-1):
    number = i
    nova_llista= actualitzacio(nova_llista)
    for j in range(len(nova_llista)):
        if nova_llista[j][i+1] =='1':
            count +=1
        if (count/len(nova_llista))>=0.5:
            common +='1'
            count = 0
            break
        elif j==len(nova_llista)-1:
            common +='0'
            count =0
    

##CAS PER A TROBAR LLISTA MINIMA( COPY PASTE)

nova_llista_minima = []
nova_llista_minima +=array
not_common ='' +epsilon[0]

def actualitzacio2(array):
    llista = []
    for s in range(len(array)):
        if array[s][number]==not_common[-1]:
            llista.append(array[s])
    return llista

for i in range(len(array[0])-1):
    number = i
    if len(nova_llista_minima)>1:
        nova_llista_minima = actualitzacio2(nova_llista_minima)
        for j in range(len(nova_llista_minima)):
            if nova_llista_minima[j][i+1] =='1':
                count +=1
            if (count/len(nova_llista_minima))>=0.5:
                not_common +='0'
                count = 0
                break
            elif j==len(nova_llista_minima)-1:
                not_common +='1'
                count =0


            
print(max(nova_llista))
print(nova_llista_minima[0])
print(int(max(nova_llista),2) * int(min(nova_llista_minima),2))
            
            

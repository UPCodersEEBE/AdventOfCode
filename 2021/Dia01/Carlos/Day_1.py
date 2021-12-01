
with open("input.txt") as n:
    array = []
    for i in n:
        array.append(int(i))
        
#Part I
        

count = 0
for j in range(1,len(array)):
    if array[j]>array[j-1]:
        count +=1
    else:
        pass
    
print(count)

#Part II
count_2= 0

for k in range(1,len(array)+1):
    if sum(array[k-1:k+2])<sum(array[k:k+3]):
        count_2 +=1
    else:
        pass
print(count_2)
        
        
    
    
    

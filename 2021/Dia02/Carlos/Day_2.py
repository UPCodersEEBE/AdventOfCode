#Read Data
with open("input_2.txt") as n:
    array = []
    for i in n:
        array.append(str(i).split())


#Problem 1

x = 0
y = 0 # Positive integer will increase depth

for i in range(len(array)):
    
    if array[i][0] == 'forward':
        x +=int(array[i][1])
    if array[i][0] == 'down':
        y +=int(array[i][1])
    if array[i][0] == 'up':
        y -=int(array[i][1])
print(x*y)

#Problem 2

x_2 = 0
y_2 = 0
aim = 0

for j in range(len(array)):
    
    if array[j][0] == 'down':
        aim +=int(array[j][1])
    if array[j][0] == 'up':
        aim -=int(array[j][1])
    if array[j][0] == 'forward':
        x_2 +=int(array[j][1])
        y_2 += aim*int(array[j][1])
print(x_2*y_2)





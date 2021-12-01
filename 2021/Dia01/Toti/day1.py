def CountLargerThanPrevoius(l):
    c = 0
    x = l[0]
    for i in l[1:]:
        if i > x:
            c += 1
        x = i
    return c

def CountLargerThreeSum(l):
    c = 0
    x = sum(l[:3])
    for i in range(1,len(l)):
        if sum(l[i:i+3]) > x:
            c += 1
        x = sum(l[i:i+3])
    return c


l = [int(line.split("\n")[0]) for line in open("input1.txt", "r")]

print(CountLargerThanPrevoius(l))
print(CountLargerThreeSum(l))
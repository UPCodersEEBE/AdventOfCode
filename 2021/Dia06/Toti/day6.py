# ineficient

# import math
# import matplotlib.pyplot as plt
# import numpy

# def LanterfishAfterXDays(days, ini):
#     actual = ini
#     next = []
#     for i in range(days):
#         for j in range(len(actual)):
#             if int(actual[j]) > 0:
#                 next.append(int(actual[j])-1)
#             else:
#                 next.append(6)
#                 next.append(8)
#         actual = next
#         next = []
#     return actual

ini = [line.split("\n")[0].split(',') for line in open("input6.txt", "r")][0]

#--------------------------------------------------
# Regressio exponencial (no va :( )

# x = []
# y = []

# for i in range(1,100):
#     x.append(i)
#     y.append(len((LanterfishAfterXDays(i, ini))))

# x1 = numpy.array(x)
# y1 = numpy.array(y)

# r = numpy.polyfit(x1, numpy.log(y1), 1)


# result = numpy.exp(r[1])*numpy.exp(r[0]*256)

# print(int(result))


#plt.plot(x1,y1,'o')
#plt.plot(x1,numpy.exp(r[1])*numpy.exp(r[0]*x1))
#plt.show()
#--------------------------------------------------

# Locura
peixos = [0,0,0,0,0,0,0,0,0]
for i in ini:
    peixos[int(i)] += 1

dies = 256
for i in range(dies-1):
    s = []
    for j in peixos[1:9]:
        if j > 0:
            s.append(j)
        else:
            s.append(0)
    peixos = s + [peixos[0]]
    peixos[7] += peixos[0]

print(sum(peixos))








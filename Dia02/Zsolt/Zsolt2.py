pc = 0
with open("Dia02/Zsolt/input.txt","r") as archivos:
    for passw in archivos:
        minn = passw.split("-")
        maxx = minn[1].split(" ")
        lletra = maxx[1].split(":")
        if (maxx[2])[int(minn[0])-1] == lletra[0] and  (maxx[2])[int(maxx[0])-1] == lletra[0]:
            continue
        elif  (maxx[2])[int(minn[0])-1] == lletra[0] or (maxx[2])[int(maxx[0])-1] == lletra[0]:
            pc += 1
print(pc)
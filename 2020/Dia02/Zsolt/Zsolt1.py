pc = 0
with open("Dia02/Zsolt/input.txt","r") as archivos:
    for passw in archivos:
        minn = passw.split("-")
        maxx = minn[1].split(" ")
        lletra = maxx[1].split(":")
        count = maxx[2].count(lletra[0])
        if count >= int(minn[0]) and count <= int(maxx[0]):
            pc += 1
print(pc)
        

        
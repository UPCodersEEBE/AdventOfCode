with open("Dia01/Zsolt/input1.txt","r") as archivos:
    if archivos.mode == "r":
        numeros = archivos.readlines()

for linea1 in numeros:
    for linea2 in numeros:
        numlinea1 = int(linea1)
        numlinea2 = int(linea2)
        if linea1 != linea2:
            if (numlinea1+numlinea2==2020):
                print("num1= ", numlinea1, "num2= ", numlinea2)
                print("solucion= ",numlinea1*numlinea2)

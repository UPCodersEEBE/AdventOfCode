archivo = open("Dia01/Zsolt/input1.txt","r")

if archivo.mode == "r":
    numeros = archivo.readlines()

for linea1 in numeros:
    for linea2 in numeros:
        for linea3 in numeros:
            numlinea1 = int(linea1)
            numlinea2 = int(linea2)
            numlinea3 = int(linea3)
            if linea1 != linea2 and linea2 != linea3:
                if (numlinea1+numlinea2+numlinea3==2020):
                    print("num1= ", numlinea1, "num2= ", numlinea2, "num3= ", numlinea3)
                    print("solucion= ",numlinea1*numlinea2*numlinea3)

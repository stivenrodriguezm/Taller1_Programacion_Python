
print("Ingresa un número entero: ")
numero1 = int(input())
print("Ingresa otro número entero: ")
numero2 = int(input())
print("Ingresa otro número entero: ")
numero3 = int(input())
print("Ingresa otro número entero: ")
numero4 = int(input())

posicion1 = 0
posicion2 = 0
posicion3 = 0
posicion4 = 0

if numero1<numero2 and numero1<numero3 and numero1<numero4:
    posicion1 = numero1
    if numero2<numero3 and numero2<numero4:
        posicion2 = numero2
        if numero3 < numero4:
            posicion3 = numero3
            posicion4 = numero4
        else:
            posicion3 = numero4
            posicion4 = numero3
    elif numero3<numero2 and numero3<numero4:
        posicion2 = numero3
        if numero2 < numero4:
            posicion3 = numero2
            posicion4 = numero4
        else:
            posicion3 = numero4
            posicion4 = numero2
    elif numero4<numero2 and numero4<numero3:
        posicion2 = numero4
        if numero2 < numero3:
            posicion3 = numero2
            posicion4 = numero3
        else:
            posicion3 = numero3
            posicion4 = numero2
elif numero2<numero1 and numero2<numero3 and numero2<numero4:
    posicion1 = numero2
    if numero1<numero3 and numero1<numero4:
        posicion2 = numero1
        if numero3 < numero4:
            posicion3 = numero3
            posicion4 = numero4
        else:
            posicion3 = numero4
            posicion4 = numero3
    elif numero3<numero1 and numero3<numero4:
        posicion2 = numero3
        if numero1 < numero4:
            posicion3 = numero1
            posicion4 = numero4
        else:
            posicion3 = numero4
            posicion4 = numero1
    elif numero4<numero1 and numero4<numero3:
        posicion2 = numero4
        if numero1 < numero3:
            posicion3 = numero1
            posicion4 = numero3
        else:
            posicion3 = numero3
            posicion4 = numero1
elif numero3<numero1 and numero3<numero2 and numero3<numero4:
    posicion1 = numero3
    if numero1<numero2 and numero1<numero4:
        posicion2 = numero1
        if numero2 < numero4:
            posicion3 = numero2
            posicion4 = numero4
        else:
            posicion3 = numero4
            posicion4 = numero2
    elif numero2<numero1 and numero2<numero4:
        posicion2 = numero2
        if numero1 < numero4:
            posicion3 = numero1
            posicion4 = numero4
        else:
            posicion3 = numero4
            posicion4 = numero1
    elif numero4<numero1 and numero4<numero2:
        posicion2 = numero4
        if numero1 < numero2:
            posicion3 = numero1
            posicion4 = numero2
        else:
            posicion3 = numero2
            posicion4 = numero1
elif numero4<numero1 and numero4<numero2 and numero4<numero3:
    posicion1 = numero4
    if numero1<numero2 and numero1<numero3:
        posicion2 = numero1
        if numero2 < numero3:
            posicion3 = numero2
            posicion4 = numero3
        else:
            posicion3 = numero3
            posicion4 = numero2
    elif numero2<numero1 and numero2<numero3:
        posicion2 = numero2
        if numero1 < numero3:
            posicion3 = numero1
            posicion4 = numero3
        else:
            posicion3 = numero3
            posicion4 = numero1
    elif numero3<numero1 and numero3<numero2:
        posicion2 = numero3
        if numero1 < numero2:
            posicion3 = numero1
            posicion4 = numero2
        else:
            posicion3 = numero2
            posicion4 = numero1

print(str(posicion1)+", "+str(posicion2)+", "+str(posicion3)+", "+str(posicion4))

print("ingresa un caracter:")
caracter = input()

caracter = ord(caracter)

if caracter >= 48 and caracter <= 57:
    print("Es un número")
elif caracter >= 65 and caracter <= 90:
    print("Es letra mayuscula")
elif caracter >= 97 and caracter <= 122:
    print("Es letra minuscula")
else:
    print("No es letra ni número")
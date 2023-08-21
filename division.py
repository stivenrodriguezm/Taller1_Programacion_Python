
print("Ingresa el dividendo")
dividendo = int(input())
print("Ingresa el divisor")
divisor = int(input())

mod = dividendo % divisor

if mod == 0:
    print("la division es exacta")
    print("Cociente: "+divisor)
    print("Residuo: 0")
else:
    print("La division no es exacta")
    print("Cociente: "+str(int(dividendo/divisor)))
    print("Residuo: "+str(mod))

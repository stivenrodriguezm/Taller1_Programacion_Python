
print("Introduce un año")
year=int(input())


if year%100 == 0 and year%400 == 0:
    print(str(year) +" es bisiesto")
elif year%100 == 0 and year%400 != 0:
    print(str(year) +" no es bisiesto")
elif year%4 == 0:
    print(str(year) +" es bisiesto")
else:
    print(str(year) + " no es bisiesto")

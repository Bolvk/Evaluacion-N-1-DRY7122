numero =int(input("Ingrese el numero de la ACL a consultar: "))

if 1 <= numero <= 99:
    print("La ACL es de tipo estandar")
elif 100 <= numero <= 199:
    print("La ACL es de tipo extendida")
else:
    print("Ingrese un numero de ACL correcto")

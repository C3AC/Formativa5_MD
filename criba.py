def criba(n):
    not_prime = set()
    prime = []
    for i in range(2, n+1):
        if i not in not_prime:
            for f in range(i*2, n+1, i):
                not_prime.add(f)
            prime.append(i)
    return prime

check = True
while check:  
    num=(input("Ingrese un número entero positivo: "))
    try:
        num = int(num)
        if num > 0:
            check = False
        else:
            print("El numero ingresado es negativo o cero, asegurese de ingresar un número positivo")
    except:
        print("Asegurese de escribir un número")
print("Los primos menores o iguales a " + str(num) + " son:\n" + str(criba(num)))
    
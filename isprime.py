def criba(n):
    not_prime = set()
    prime = []
    for i in range(2, n+1):
        if i not in not_prime:
            for f in range(i*2, n+1, i):
                not_prime.add(f)
            prime.append(i)
    return prime

def isprime(n):
    if n < 2:
        return False
    list= criba(int(n)-1)
    for i in list:
        if n%i==0:
            return False
    return True

def primedecomposition(n):
    primes = criba(int(n**0.5) + 1)
    prime_factors = []
    for i in primes:
        while n % i == 0:
            prime_factors.append(i)
            n = n // i
    if n > 1:
        prime_factors.append(n)
    return prime_factors

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
if isprime(num):
    print("El número " + str(num) + " es primo")
else:
    print('El numero ' + str(num) + ' no es primo pues lo dividen: ')
    print(primedecomposition(num))

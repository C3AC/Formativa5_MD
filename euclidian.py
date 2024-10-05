def mcd(n,m):
    if n == m or m == 0:
        return n
    aux = m
    m = n % m
    n = aux
    return mcd(n,m)

while True:
    n = input('ingrese un número entero positivo: ')
    m = input('ingrese otro número entero positivo: ')
    try:
        n = int(n)
        m = int(m)
        if n > 0 and m > 0:
            print('El mcd de ' + str(n) + ' y ' + str(m) + ' es ' + str(mcd(n,m)))
            break
        else:
            print('Asegurese de ingresar un número positivo')
    except:
        print('Asegurese de ingresar un número entero positivo')
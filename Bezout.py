import numpy as np

def euclides_extendido(a,b,lista):
    if a == 0 or b == 0:
        return lista
    d = a//b
    r = a%b
    lista.append(d)
    euclides_extendido(b,r,lista)
    
def bezout(a,b):
    if a == 0 or b == 0:
        return "No se puede calcular el coeficiente de Bezout"
    lista = []
    euclides_extendido(a,b,lista)
    flag = False 
    for i in lista:
        if flag == False:
            matrix = np.array([[i,1],
                               [1,0]])
            flag = True
        else:
            matrix = np.dot(matrix,np.array([[i,1],
                                             [1,0]]))
    return int(round(matrix[1][1]*np.linalg.det(matrix),0)),int(round(-matrix[0][1]*np.linalg.det(matrix),0))

flag2 = True 
while flag2:
    try:
        a = int(input('Ingrese un numero entero a: '))
        b = int(input('Ingrese un numero entero b: '))
        flag2 = False
        x,y = bezout(a,b)
        print(f'Los coeficientes de Bezout son: {x} y {y} respectivamente')
        print(f'La ecuacion diofántica es: {a}*{x} + {b}*{y}')
    except ValueError:
        print('Error, el valor ingresado no es un numero entero')
    
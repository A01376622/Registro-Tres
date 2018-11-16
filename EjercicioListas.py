#Autor: Michelle Sánchez


from random import randint     #con * importas todas las funciones


#Crea y regresa una lista con valores aleatorios (0, 255) de longitud n.
def generarLista(n):
    lista = []

    for k in range(n):      #n vueltas
         azar = randint(0,255)
         lista.append(azar)

    #Hasta que el ciclo for termina, regresa la lista
    return lista

def calcularPares(lista):

    numerosPares = 0

    for n in lista:   #iterador, recorre datos uno por uno

        if n%2 == 0:
            numerosPares += 1

    return numerosPares


def calcularMenoresPromedio(lista):
    menores = []

    if len(lista)>0:
        promedio = sum(lista)/len(lista)

        for n in lista:
            if n < promedio:
                menores.append(n)

    return menores


#--------------------------------------------------------------------------------------------------------------------#
#Regresa [0, 1, 2, 3... 99, 100]
def crearLista():
    lista = []
    for i in range(101):
        lista.append(i)

    return lista


#Función que borra múltiplos
def borrarMultiplos(lista, numero):

    for dato in range(numero + 1, len(lista)):

        if dato%numero == 0:
            lista[dato] = 0

    return lista


def extraerDiferentesCero(lista):

    difCero = []

    for k in lista:
        if k != 0:
            difCero.append(k)

    return difCero



l = crearLista()
print(l)

borrarMultiplos(l, 2)
borrarMultiplos(l, 3)
borrarMultiplos(l, 5)
borrarMultiplos(l, 7)
borrarMultiplos(l, 11)

print()
print(l)
print( )

dc = extraerDiferentesCero(l)
print(dc)




"""
a = generarLista(0)
print(a)
np = calcularPares(a)
print(np)
m = calcularMenoresPromedio(a)
print(m)"""
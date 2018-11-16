#Autor: Michelle
#Descripción:

#Diccionario
d = {"chicken":"pollito", "pencil":"lapiz", "pen":"pluma"}


def leerOpcion():
    print("""
    1. Traducir Inglés->Español
    2. Traducir Español->Inglés
    0. Salir
    """)
    opcion = int(input("Teclea tu opción: "))
    print(opcion)
    return opcion


def traducirIE(palabra):
    if palabra in d:
        return d[palabra]
    return "La palabra no existe"


def traducirEI(palabra):

    for llave, valor in d.items():
        if valor == palabra:
            return llave

    return "La palabra no existe"




def main():
    opcion = leerOpcion()

    while opcion != 0:

        if opcion == 1:      #inglés -> español
            palabra = input("Escribe la palabra en inglés: ")
            traduccion = traducirIE(palabra)
            print("En español es: ", traduccion)

        elif opcion == 2:    #español -> inglés
            palabra = input("Escribe la palabra en español: ")
            traduccion = traducirEI(palabra)
            print("En inglés es: ", traduccion)

        else:
            print("Opción incorrecta")

        leerOpcion()


main()
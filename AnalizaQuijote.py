#Autor: Michelle Sánchez
#Descripción: Graficar la frecuencia de aparición de cada letra en el texto del Quijote.

import matplotlib.pyplot as plot

def graficar(contadores):
    datosX = contadores.keys()
    datosY = contadores.values()

    plot.plot(datosX, datosY)

    plot.title("Letras en el Quijote de la Mancha")
    plot.xlabel("Letras")
    plot.ylabel("Frecuencia")

    plot.show()


def procesar(entrada):
    contadores = {}    #Diccionario de contadores "e":231
    contadorLineas = 0

    for linea in entrada:     #Visita linea x linea del archivo
        contadorLineas += 1
        for letra in linea.upper():   #Visita cada letra de la cadena
            if letra.isalpha():
                if letra in contadores:      #Ya existe en el diccionario?
                    contadores[letra] += 1    #Cuenta uno más
                else:
                    contadores[letra] = 1       #Crea una llave nueva

    print(contadores)
    print(contadorLineas)

    graficar(contadores)

def main():
    entrada = open("quijote.txt", "r", encoding="UTF-8")
    procesar(entrada)
    entrada.close()


main()
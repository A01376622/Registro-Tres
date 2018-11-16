#Autor: Michelle Sánchez Guerrero
#Descripición: Procesar archivo

def main():
    entrada = open("calificaciones.csv", "r")

    #Archivo de SALIDA
    salida = open("promedios.txt", "w")

    entrada.readline()   #Lee una línea y la ignora

    for linea in entrada:   #Lee cada línea del archivo
        datos = linea.split(",")    #Regresa una lista completa, separando los datos ej. ["pepito", "100", "85", "75"]
        matricula = datos[1][2:]
        r1 = int(datos[2])
        r2 = int(datos[3])
        r3 = int(datos[4])

        promedio = (r1 + r2 + r3)/3

        mensaje = "Aprobado"

        if promedio < 70:
            mensaje = "NO aprobado"

        #print(matricula, "%.02f" % promedio, mensaje, sep=",")
        print("%s,%.02f,%s" % (matricula, promedio, mensaje))
        salida.write("%s,%.02f,%s\n" % (matricula, promedio, mensaje))

    entrada.close()
    salida.close()



main()

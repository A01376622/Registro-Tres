def main():
    archivo = open("datos.txt", "r", encoding="UTF-8")   #"r" es read
    texto = archivo.read()
    print(texto.title())


main()
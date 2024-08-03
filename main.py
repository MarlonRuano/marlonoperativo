def saludo(nombre):
    if nombre:
        print(f"Hola, {nombre}!")
    else:
        print("¡Hola, mundo!")

nombre = input("¿Cuál es tu nombre? ")
saludo(nombre)

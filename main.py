def saludo(nombre, tipo):
    saludos = {
        "formal": f"Buenos días, {nombre}.",
        "amistoso": f"¡Hola, {nombre}!",
        "despedida": f"Adiós, {nombre}."
    }
    print(saludos.get(tipo, "¡Hola, mundo!"))

nombre = input("¿Cuál es tu nombre? ")
tipo = input("¿Qué tipo de saludo prefieres (formal, amistoso, despedida)? ")
saludo(nombre, tipo)

def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)

participantes = []

while True:
    print("\n## MENU DE OPCIONES ##")
    print("1. Agregar participantes")
    print("2. Mostrar participates ordenados por nombre")
    print("3. Mostrar participantes ordenados por edad")
    print("4. Salir")

    opcion = input("\nIngrese una opcion: ")

    match opcion:
        case "1":
            cantidad = int(input("Ingrese la cantidad de participantes: "))

            for i in range(cantidad):
                numero = int(input(f"Ingrese el numero de dorsal del participante {i+1}: "))

                if numero not in participantes:
                    nombre = input("Ingrese el nombre completo del participante: ")
                    edad = int(input("Ingrese la edad del participante: "))

                    while True:
                        categoria = input("Ingrese la categoria del participante (juvenil/adulto/master): ")
                        if categoria == "juvenil" or categoria == "adulto" or categoria == "master":
                            break

                    nuevo_participante = {
                        "numero": numero,
                        "nombre": nombre,
                        "edad": edad,
                        "categoria": categoria,
                    }

                    participantes.append(nuevo_participante)

                else:
                    print("El participante ya existe")

            for participant in participantes:
                print(participant)

        case "2":
            print("\n## PARTICIPANTES ORDENADOS POR NOMBRE ##")

            nombres_ordenados = quick_sort([p['nombre'] for p in participantes])
            for nombre in nombres_ordenados:
                for p in participantes:
                    if p['nombre'] == nombre:
                        print(f"{p['nombre']} - Dorsal: {p['numero']}")

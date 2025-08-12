def ingreso_participates():
    numero = -1

    while numero < 0:
        while True:
            try:
                numero = int(input(f"Ingrese el numero de dorsal del participante #{i + 1}: "))
                if numero >= 0:
                    break
            except ValueError:
                print("Dato inválido")

        if numero not in participantes:
            nombre = input("Ingrese el NOMBRE COMPLETO del participante: ")
            edad = int(input("Ingrese la edad (años) del participante: "))

            while True:
                categoria = input("Ingrese la categoria del participante (juvenil/adulto/master): ")
                if categoria == "juvenil" or categoria == "adulto" or categoria == "master":
                    break
                else:
                    print("Categoria incorrecta")

            nuevo_participante = {
                "numero": numero,
                "nombre": nombre,
                "edad": edad,
                "categoria": categoria,
            }

            participantes.append(nuevo_participante)

            break
        else:
            print("El participante ya existe")
            numero = -1



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
    print("0. Salir")

    opcion = input("\nIngrese una opcion: ")

    match opcion:
        case "1":
            print("## INGRESO DE PARTICIPANTES ##")
            cantidad = int(input("Ingrese la cantidad de participantes: "))

            for i in range(cantidad):
                ingreso_participates()

        case "2":
            print("\n## PARTICIPANTES ORDENADOS POR NOMBRE ##")

            nombres_ordenados = quick_sort([p['nombre'] for p in participantes])
            for nombre in nombres_ordenados:
                for p in participantes:
                    if p['nombre'] == nombre:
                        print(f"{p['nombre']} - Dorsal: {p['numero']}")

        case "3":
            print("\n## PARTICIPANTES ORDENADOS POR EDAD ##")

            edades_ordenadas = quick_sort([p['edad'] for p in participantes])
            for edad in edades_ordenadas:
                for p in participantes:
                    if p['edad'] == edad:
                        print(f"{p['nombre']} - Edad: {p['edad']} - Dorsal: {p['numero']}")
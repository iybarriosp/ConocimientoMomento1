optimo = []
moderado = []
defectuoso = []

#pedir informacion al usuario
for i in range(5):
    cabina = int(input(f"Ingrese el numero de la cabina a analizar {i + 1}: "))
    puntaje = float(input(f"Ingrese el puntaje dela cabina{cabina} (entre 2,3 o 4): "))

    if puntaje == 4:
        optimo.append(cabina)
    elif puntaje == 3:
        moderado.append(cabina)
    elif puntaje == 2:
        defectuoso.append(cabina)
    else:
        print(f"Puntaje inválido para la cabina {cabina}. Debe ser entre 2, 3 o 4.")

    # Mostrar los pacientes en cada clasificación
print("\nCabinas con funcionamiento optimo: ")
for cabina in optimo:
    print(cabina)

print("\nCabinas con funcionamiento moderado: ")
for cabina in moderado:
    print(cabina)

print("\nCabinas con funcionamiento defectuoso: ")
for cabina in defectuoso:
    print(cabina)
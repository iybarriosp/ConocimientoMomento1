noTiene = []
nivelBajo = []
nivelModerado = []
nivelGrave = []

#pedir informacion al usuario
for i in range(803):
    nombre = input(f"Ingrese el nombre del paciente {i + 1}: ")
    puntaje = float(input(f"Ingrese el puntaje de {nombre}: "))

    if puntaje < 10:
        noTiene.append(nombre)
    elif 11 <= puntaje <= 40:
        nivelBajo.append(nombre)
    elif 41 <= puntaje <= 69:
        nivelModerado.append(nombre)
    elif 70 <= puntaje <= 100:
        nivelGrave.append(nombre)
    else:
        print(f"Puntaje fuera de rango para el paciente {nombre}")

# Mostrar los pacientes en cada clasificación
print("\nPacientes sin leucemia:")
for paciente in noTiene:
    print(paciente)

print("\nPacientes con nivel bajo de leucemia:")
for paciente in nivelBajo:
    print(paciente)

print("\nPacientes con nivel moderado de leucemia:")
for paciente in nivelModerado:
    print(paciente)

print("\nPacientes con nivel grave de leucemia:")
for paciente in nivelGrave:
    print(paciente)
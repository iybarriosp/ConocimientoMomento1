# Inicializar en cero los contadores
conteoNumerosPares = 0
conteoNumerosImpares = 0

todosNumeros = []
numerosClasificados = []  # par o impar

# Bucle para ingresar los números
for i in range(400):  # Cambia a 400 para hacer la versión completa
    numero = int(input(f"Ingrese el número {i + 1}: "))  # Almacenamiento de números ingresados
    todosNumeros.append(numero)

    if numero % 2 == 0:
        numerosClasificados.append("Es par")
        conteoNumerosPares += 1
    else:
        numerosClasificados.append("Es impar")
        conteoNumerosImpares += 1

# Lista de números con su respectiva clasificación
print("\nLista de números con su respectiva clasificación:")
for i in range(400):  # Cambia a 400 para la versión completa
    print(f"El número: {todosNumeros[i]}, está clasificado en la lista como: {numerosClasificados[i]}")

# Cantidad de números pares e impares
print(f"\nLa cantidad de números pares es: {conteoNumerosPares}")
print(f"La cantidad de números impares es: {conteoNumerosImpares}")
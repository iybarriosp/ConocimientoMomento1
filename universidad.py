num1,num2 = 5,8 #primeros dos numeros de la lista

serial = [] #lista para almacenar los numeros en serie

for _ in range(100):
    if num1 != 13: #esto es para omitir el numero 13
        serial.append(num1)
#operacion para calcular la suma entre num1 y num2 y actualizar el siguiente numero
    num1, num2 = num2, num1 + num2

print(serial)
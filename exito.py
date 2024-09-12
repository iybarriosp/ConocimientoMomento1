salarioBasico = float(input("Ingrese el salario básico del empleado: "))
ventas = float(input("Ingrese el totald e ventas hechas por el empleado: "))
comision = float(input("Ingrese la comision del empleado: "))
seguridadSocial = float(input("Ingrese la deducción fija paras eguridad social del empleado: "))

comision = (comision / 100) * ventas #Calcular comision
salarioBruto = salarioBasico + comision #Calcular salario bruto
salarioNeto = salarioBruto - seguridadSocial #Calcular salario neto

#Mostrar resultados
print(f"\nInformación del empleado:")
print(f"Salario Básico: {salarioBasico:.2f}")
print(f"Comisión: {comision:.2f}")
print(f"Salario Bruto: {salarioBruto:.2f}")
print(f"Deducción Seguridad Social: {seguridadSocial:.2f}")
print(f"Salario Neto: {salarioNeto:.2f}")
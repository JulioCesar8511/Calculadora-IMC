def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def validar_numero(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            return int(entrada)
        else:
            print("Por favor, introduce un número válido.")

def validar_texto(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isalpha():
            return entrada
        else:
            print("Por favor, introduce un texto válido.")

nombre = validar_texto("Introduce tu nombre: ")
apellido_paterno = validar_texto("Introduce tu apellido paterno: ")
apellido_materno = validar_texto("Introduce tu apellido materno: ")
edad = validar_numero("Introduce tu edad: ")
peso = validar_numero("Introduce tu peso en kg: ")
estatura = validar_numero("Introduce tu estatura en metros: ")

imc = calcular_imc(peso, estatura)

print("\nDatos personales:")
print("Nombre:", nombre)
print("Apellido Paterno:", apellido_paterno)
print("Apellido Materno:", apellido_materno)
print("Edad:", edad)
print("Peso:", peso, "kg")
print("Estatura:", estatura, "m")
print("Índice de Masa Corporal (IMC):", imc)

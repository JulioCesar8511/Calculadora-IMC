def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def obtener_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, asegúrate de ingresar un valor numérico válido.")

def main():
    nombre = input("Por favor, ingresa tu nombre: ")
    apellido_paterno = input("Ingresa tu apellido paterno: ")
    apellido_materno = input("Ingresa tu apellido materno: ")

    edad = obtener_numero("Ingresa tu edad: ")
    peso = obtener_numero("Ingresa tu peso en kg: ")
    estatura = obtener_numero("Ingresa tu estatura en metros: ")

    imc = calcular_imc(peso, estatura)

    print("\nDatos personales:")
    print("Nombre:", nombre)
    print("Apellido paterno:", apellido_paterno)
    print("Apellido materno:", apellido_materno)
    print("Edad:", edad)
    print("Peso:", peso, "kg")
    print("Estatura:", estatura, "m")
    print("Índice de Masa Corporal (IMC):", imc)

if __name__ == "__main__":
    main()

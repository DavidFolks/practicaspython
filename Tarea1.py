# Pedimos al usuario que ingrese sus datos
nombre = input("Por favor, ingresa tu nombre: ")
apellido_paterno = input("Ingresa tu apellido paterno: ")
apellido_materno = input("Ingresa tu apellido materno: ")
edad = input("Ingresa tu edad: ")
peso = input("Ingresa tu peso en kg: ")
estatura_cm = input("Ingresa tu estatura en centímetros: ")

# Verificamos que ningún campo esté vacío y que edad, peso y estatura_cm sean números
if nombre and apellido_paterno and apellido_materno and edad and peso and estatura_cm:
    if edad.isdigit() and peso.isdigit() and estatura_cm.isdigit():
        # Convertimos los datos de entrada en números para poder calcular el IMC
        edad = int(edad)
        peso = int(peso)
        estatura_m = float(estatura_cm) / 100

        # Calculamos el IMC
        imc = peso / (estatura_m ** 2)

        # Mostramos los datos y el IMC al usuario
        print("Tu nombre completo es:", nombre, apellido_paterno, apellido_materno)
        print("Tienes", edad, "años")
        print("Tu peso es de", peso, "kg y tu estatura es de", estatura_cm, "cm")
        print("Tu índice de masa corporal es de", imc)
    else:
        print("Por favor, ingresa una edad, peso y estatura válidos (números enteros o decimales)")
else:
    print("Por favor, asegúrate de ingresar todos tus datos")
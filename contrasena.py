# PROGRAMA QUE COMPARE DOS CADENAS DE CARACTERES IGNORANDO MAYÚSCULAS Y MINÚSCULAS
# variables
password = "coNdiciOnaL"
passIntroducida = ""
contador = 0

# bucle que se ejecutará hasta que el usuario introduzca bien la contraseña o hasta que llegue a 3 intentos
while contador < 3 and passIntroducida.lower() != password.lower():
    # pedimos al usuario que introduzca la password
    passIntroducida = (input("Introduce la password  -> "))

    # si la password introducida pasada a minúsculas es igual a nuestra pass en minúsculas
    if password.lower() == passIntroducida.lower():
        print("La contraseña introducida es correcta")
    contador = contador + 1


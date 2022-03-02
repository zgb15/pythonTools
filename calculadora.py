# CALCULADORA REALIZA CON PYTHON
# variables
num1 = 0
num2 = 0
opcion = 0  # inicializamos variable opcion a 0

# bucle que funcionará como menú que se ejecutará mientras no elija la opción 5 (salir)
while True and (opcion != 5):
    print(" ")
    # pedimos al usuario que introduzca los dos dígitos para operar
    num1 = float(input("Introduce el primer dígito  -> "))
    num2 = float(input("Introduce el segundo dígito -> "))

    # imprimimos por consola el menú
    print("""
        Seleccione una opción:
    
        1 SUMA
        2 RESTA
        3 MULTIPLICACIÓN
        4 DIVISIÓN
        5 SALIR
    
    """)
    opcion = int(input("Eliges -> "))  # el usuario introduce lo que quiere hacer

    if opcion == 1:  # suma
        print(" ")
        print("= La suma de", num1, "+", num2, "es igual a", num1 + num2)
    elif opcion == 2:  # resta
        print(" ")
        print("RESULTADO: La resta de", num1, "-", num2, "es igual a", num1 - num2)
    elif opcion == 3:  # multiplicación
        print(" ")
        print("RESULTADO: El producto de", num1, "*", num2, "es igual a", num1 * num2)
    elif opcion == 4:  # división
        print(" ")
        print("RESULTADO: La división de", num1, "/", num2, "es igual a", num1 / num2)

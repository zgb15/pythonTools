# PROGRAMA QUE PERMITE CREAR Y MODIFICAR UNA LISTA
# variables
lista = []
palabra = ""
opcion = int(0)

# bucle for para que el usuario introduzca 5 elementos en la lista
for i in range(0, 5):

    palabra = (input("Introduzca una palabra: "))
    lista.append(palabra)

print()
print("Su lista de elementos contiene: ")
print(lista)

# bucle que funcione como menú para que el usuario inserte o elimine
while opcion != 3:
    print()
    opcion = int(input("Pulse 1 si quiere insertar más palabras, 2 si quiere eliminar o 3 si desea salir: "))

    if opcion == 1:
        palabra = (input("Introduzca la palabra que desea añadir: "))
        lista.append(palabra)
        print()
        print("Su lista ahora: ")
        print(lista)
    elif opcion == 2:
        palabra = (input("Introduzca la palabra que desea eliminar: "))
        lista.remove(palabra)
        print()
        print("Su lista ahora: ")
        print(lista)
    else:
        print("Adiós!")


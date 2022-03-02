# PROGRAMA PARA SABER SI UN EMPLEADO TIENE QUE PAGAR IMPUESTOS O NO EN BASE A SU SUELDO, usando herencia - polimorfismo
# CLASE PERSONA
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"{self.nombre !r} {self.edad !r} "


# CLASE EMPLEADO QUE HEREDA DE PERSONA
class Empleado(Persona):
    def __init__(self, sueldo):
        name = input("Ingrese su nombre: ")
        age = int(input("Ingrese su edad: "))
        Persona.__init__(self, name, age)
        self.sueldo = sueldo

    def __repr__(self):
        if self.sueldo >= 3000:
            return f"{self.nombre !r} {self.edad !r} debe pagar renta porque su sueldo excede los 3000"
        else:
            return f" {self.nombre !r} {self.edad !r} no debe pagar la renta pues su sueldo es menor a 3000"


# creamos el objeto empleado
empleado1 = Empleado(1000)

# imprimimos lo que nos devuelve la función
print(empleado1.__repr__())

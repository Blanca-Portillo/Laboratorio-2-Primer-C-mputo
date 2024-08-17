class Perro:
    def __init__(self, nombre, edad, raza, color, peso, Dueño, direccion, telefono):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.color = color
        self.peso = peso
        self.Dueño = Dueño
        self.direccion = direccion
        self.telefono = telefono
        self.estado = "No atendido"
        self.tamano = "Pequeño" if peso < 10 else "Grande"
    
    def registrar(self):
        self.estado = "Atendido"

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Raza: {self.raza}")
        print(f"Color: {self.color}")
        print(f"Peso: {self.peso} kg")
        print(f"Tamaño: {self.tamano}")
        print(f"Dueño: {self.Dueño}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Estado: {self.estado}")


class Veterinaria:
    def __init__(self):
        self.perros = []

    def registrar_perro(self, perro):
        perro.registrar()
        self.perros.append(perro)

    def mostrar_los_perros_atendidos(self):
        for perro in self.perros:
            perro.mostrar_informacion()
            print("------------------------------------------------------------------" )



veterinaria = Veterinaria()


perro1 = Perro(
    nombre="Firulais", 
    edad=2, 
    raza="Aguacatero", 
    color="Negro", 
    peso=12, 
    Dueño="pepe", 
    direccion="Roma", 
    telefono="123456789"
)
perro2 = Perro(
    nombre="Canelo", 
    edad=4, 
    raza="mestiza", 
    color="Marrón", 
    peso=10, 
    Dueño="Juanita", 
    direccion="Gerardo Barrios", 
    telefono="987654321"
)
veterinaria.registrar_perro(perro1)
veterinaria.registrar_perro(perro2)

veterinaria.mostrar_los_perros_atendidos()

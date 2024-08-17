class Automovil:
    def __init__(self, marca, modelo, año, tipo, color, motor, transmisión, combustible, kilometraje, precio_compra):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.tipo = tipo  # puede ser nacional o importado
        self.color = color
        self.motor = motor
        self.transmisión = transmisión  # manual o automática
        self.combustible = combustible  # su combustible puede ser: gasolina, diesel o súper.
        self.kilometraje = kilometraje
        self.precio_compra = precio_compra
        self.margen_ganancia = 1.4
        self.precio_venta = round(precio_compra * self.margen_ganancia, 2)
        self.ruedas = 4
        self.capacidad_pasajeros = 5

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Tipo: {self.tipo}")
        print(f"Color: {self.color}")
        print(f"Motor: {self.motor}")
        print(f"Transmisión: {self.transmisión}")
        print(f"Combustible: {self.combustible}")
        print(f"Kilometraje: {self.kilometraje} km")
        print(f"Precio de compra: ${self.precio_compra}")
        print(f"Precio de venta: ${self.precio_venta}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad de pasajeros: {self.capacidad_pasajeros}")
        print("----------------------------------------------------------" )


class Concesionario:
    def __init__(self):
        self.autos = []

    def registrar_auto(self, auto):
        self.autos.append(auto)

    def mostrar_todos_los_autos(self):
        for auto in self.autos:
            auto.mostrar_informacion()


concesionario = Concesionario()


auto1 = Automovil(
    marca="Toyota", 
    modelo="Corolla", 
    año=2022, 
    tipo="Nacional", 
    color="Blanco", 
    motor="2.0L", 
    transmisión="Automática", 
    combustible="Gasolina", 
    kilometraje=0, 
    precio_compra=20000
)

auto2 = Automovil(
    marca="Mitsubishi", 
    modelo="L200", 
    año=2023, 
    tipo="Importado", 
    color="Rojo", 
    motor="5.0L V8", 
    transmisión="Manual", 
    combustible="Diesel", 
    kilometraje=0, 
    precio_compra=40000
)

concesionario.registrar_auto(auto1)
concesionario.registrar_auto(auto2)

concesionario.mostrar_todos_los_autos()

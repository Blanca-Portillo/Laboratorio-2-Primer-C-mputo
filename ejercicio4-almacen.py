class Dispositivo:
    def __init__(self, tipo, modelo, especificaciones, precio_compra):
        self.tipo = tipo  # El tipo puede ser Celular, Tablet, o Portátil según lo pedido en el ejercicio
        self.marca = "PHR"
        self.modelo = modelo
        self.especificaciones = especificaciones  
        self.precio_compra = precio_compra
        self.margen_ganancia = 1.7
        self.precio_venta = round(precio_compra * self.margen_ganancia, 2)
        self.origen = "Importado"

    def mostrar_informacion(self):
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print("Especificaciones:")
        for i, espec in enumerate(self.especificaciones, start=1):
            print(f"  {i}. {espec}")
        print(f"Precio de compra: ${self.precio_compra}")
        print(f"Precio de venta: ${self.precio_venta}")
        print(f"Origen: {self.origen}")
        print("---------------------------------------------------------------------------------")


class Almacen:
    def __init__(self):
        self.dispositivos = []

    def registrar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

    def mostrar_todos_los_dispositivos(self):
        for dispositivo in self.dispositivos:
            dispositivo.mostrar_informacion()



almacen = Almacen()


celular = Dispositivo(
    tipo="Celular", 
    modelo="PHR X100", 
    especificaciones=["Pantalla 6.5''", "128GB almacenamiento", "4GB RAM", "Cámara 12MP", "Batería 4000mAh", "Dual SIM"],
    precio_compra=300
)

tablet = Dispositivo(
    tipo="Tablet", 
    modelo="PHR Tab10", 
    especificaciones=["Pantalla 10''", "64GB almacenamiento", "3GB RAM", "Cámara 8MP", "Batería 6000mAh", "WiFi + 4G"],
    precio_compra=250
)

portatil = Dispositivo(
    tipo="Portátil", 
    modelo="PHR ProBook", 
    especificaciones=["Pantalla 15.6''", "256GB SSD", "8GB RAM", "Procesador Intel i5", "Batería 5000mAh", "Teclado retroiluminado"],
    precio_compra=700
)

almacen.registrar_dispositivo(celular)
almacen.registrar_dispositivo(tablet)
almacen.registrar_dispositivo(portatil)

almacen.mostrar_todos_los_dispositivos()

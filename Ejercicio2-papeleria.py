class Articulos:
    def __init__(self, tipo, detalle, precio_compra):
        self.tipo = tipo
        self.detalle = detalle
        self.precio_compra = precio_compra
        self.margen_ganancia = 1.30
        self.precio_venta = round(precio_compra * self.margen_ganancia, 2)
        self.marca = "Hojitas" if tipo == "Cuaderno" else "Rayas"

    def mostrar_informacion(self):
        print(f"Tipo: {self.tipo}")
        print(f"Detalle: {self.detalle}")
        print(f"Marca: {self.marca}")
        print(f"Precio de compra: ${self.precio_compra}")
        print(f"Precio de venta: ${self.precio_venta}")
        print("--------------------------------------------------------------")


class Papeleria:
    def __init__(self):
        self.articulos = []

    def registrar_articulo(self, articulo):
        self.articulos.append(articulo)

    def mostrar_todos_los_articulos(self):
        for articulo in self.articulos:
            articulo.mostrar_informacion()



papeleria = Papeleria()


cuaderno50 = Articulos(tipo="Cuaderno", detalle="50 hojas", precio_compra=2.50)
cuaderno100 = Articulos(tipo="Cuaderno", detalle="100 hojas", precio_compra=4.00)
lapiz_grafito = Articulos(tipo="Lápiz", detalle="Grafito", precio_compra=0.50)
lapiz_colores = Articulos(tipo="Lápiz", detalle="Colores", precio_compra=1.00)

papeleria.registrar_articulo(cuaderno50)
papeleria.registrar_articulo(cuaderno100)
papeleria.registrar_articulo(lapiz_grafito)
papeleria.registrar_articulo(lapiz_colores)


papeleria.mostrar_todos_los_articulos()


#SITUACIÓN PROBLEMÁTICA EN MI ENTORNO:
#EN LA IGLESIA CADA DOMINGO 
# SE REQUIERE RECOLECTAR DATOS DE
#  LAS PERSONAS QUE INGRESAN DIEZMOS COMO
#  POR EJEMPLO: NOMBRE, SI ES MIEMBRO EN PROPIEDAD O NO,
#  SI ES LIDER DE ALGUN DEPARTAMENTO Y EN CUÁL Y DE CUÁNTO ES SU DIEZMO


class Diezmo_iglesia: #En esta linea esta definiendo el nombre de la clase 

    def __init__(self, nombre, es_miembro, es_lider, departamento, monto_diezmo):#con este método damos inicio a la clase y pues le llamamos constructor
        self.nombre = nombre #aqui tenemos los atributos de nuestra clase 
        self.es_miembro = es_miembro#aqui tenemos los atributos de nuestra clase 
        self.es_lider = es_lider#aqui tenemos los atributos de nuestra clase 
        self.departamento = departamento if es_lider else "N/A"#aqui tenemos los atributos de nuestra clase 
        self.monto_diezmo = monto_diezmo#aqui tenemos los atributos de nuestra clase 

#comenté cada uno para que se sepa que todos esos son los atributos



    def mostrar_informacion(self): # este método nos dejará ver los detalles de un objeto y en este caso es Diezmo_iglesia
        print(f"Nombre: {self.nombre}") 
        print(f"Es miembro en propiedad: {'Si' if self.es_miembro else 'No'}")
        print(f"Es líder de algún departamento: {'Si' if self.es_lider else 'No'}")
        if self.es_lider:
            print(f"Departamento: {self.departamento}")
        print(f"Monto del diezmo: ${self.monto_diezmo}")
        print("-----------------------------------------------------------------------------------")


class Registro_Diezmos: # esta es una nueva clase
    def __init__(self):
        self.registros = [] #con este metodo le damos inicio a la clase 

    def registrar_diezmo(self, diezmo):
        self.registros.append(diezmo) # Este método toma un objeto, en este caso "diezmo" como argumento y lo añade a la lista "registros"

    def mostrar_los_registros(self):
        for diezmo in self.registros:
            diezmo.mostrar_informacion() #Para cada objeto en la lista llama al método "mostrar_informacion"


def datos(): # solicitamos la informacón 
    nombre = input("Ingrese el nombre: ")
    es_miembro = input("¿Es miembro en propiedad? (si/no): ").strip().lower() == 'si'
    es_lider = input("¿Es líder de algún departamento? (si/no): ").strip().lower() == 'si'
    departamento = input("¿En qué departamento? ") if es_lider else "N/A"
    monto_diezmo = float(input("Ingrese el monto del diezmo: $"))

    return Diezmo_iglesia(nombre, es_miembro, es_lider, departamento, monto_diezmo)



registro_diezmos = Registro_Diezmos() # creamos una instancia 

print("Registro de Diezmos:")
for _ in range(2): # aqui hacemos un bucle que se ejecuta dos veces o las que el usuario requiera, lo que significa que se recopilarán datos para dos diezmos. 
    diezmo = datos()
    registro_diezmos.registrar_diezmo(diezmo)

print("\nDatos de Diezmos Registrados:")
registro_diezmos.mostrar_los_registros()


#EL PROBLEMA QUE ESTA RESOLVIENDO ES EL RECOPILAR Y GESTIONAR DE MANERA MÁS FACIL LOS DIEZMOS DE MI IGLESIA,
#ACTUALMENTE ESO SE HACE DE MANERA MANUAL ES DECIR, A MANO POR ASI DECIRLO, LO QUE OCURRE ES QUE AL HACERLO MANUAL 
#HAY UN MAYOR RIESGO DE COMETER ERRORES Y ASI PERDER DATOS FINANCIEROS. ES POR ESO QUE HE HECHO ESTE EJERCICIO EN BASE A
#ESE PROBLEMA EN MI ENTORNO PARA QUE ASI SE PUDIESE LLEVAR DE MANERA ORDENADA. 
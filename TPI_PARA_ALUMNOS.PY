from ast import Delete, Num
from importlib.util import module_for_loader
import sqlite3

class ProgramaPrincipal:

    def menu(self):
        while True:
            print("Menu de opciones Concesionaria")
            print("2- Modificar Automovil")
            print("1- Cargar Automovil")
            print("3- Borrar Automovil")
            print("4- Cargar Disponibilidad")
            print("5- Listado de Automoviles")
            print("0- Salir de menu")
            
            nro = int(input("Por favor ingrese un número"))
            if nro == 1:
                marca = input("Por favor ingrese la marca del automovil: ")
                modelo = input("Por favor ingrese el modelo del automovil: ")
                precio = input("Por favor ingrese el precio del automovil: ")
                cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                nuevo_automovil = Automovil(marca,modelo,precio,cantidadDisponibles)
                nuevo_automovil.cargar_automovil()
            if nro ==2:
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre del modelo: ")
                precio = input("Por favor ingrese el nuevo precio: ")
                automovil_a_modificar=Automovil(marca,modelo,precio)
                automovil_a_modificar.modificar_automovil()
            if nro ==3:
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre del modelo: ")
                automovil_a_borrar=Automovil(marca,modelo)
                automovil_a_borrar.borrar_automovil()
            if nro ==4:
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre del modelo: ")
                automovil_a_cargar=Automovil(marca,modelo)
                automovil_a_cargar.disponibilidad_automovil()
            if nro ==5:
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre del modelo: ")
                lista_automovil=Automovil(marca,modelo,cantidadDisponibles)
                lista_automovil.listadoAutomovil()
            if nro==0:
                break
    
    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES")
        conexion.miCursor.execute("CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")    
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

class Automovil:
    def __init__(self, marca, modelo,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.modelo = modelo
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles

        
    def cargar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            
            conexion.miCursor.execute("INSERT INTO AUTOMOVILES(marca,modelo,precio,cantidadDisponibles) VALUES('{}', '{}','{}','{}')".format(self.marca, self.modelo,self.precio,self.cantidadDisponibles))
            conexion.miConexion.commit()
            print("Automovil cargado exitosamente")
        except:
            print("Error al agregar un automovil")
        finally:
            conexion.cerrarConexion()
    
    
    def modificar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET modelo='{}' where marca='{}' and precio='{}' ".format(self.modelo,self.marca,self.precio))
            conexion.miConexion.commit()
            print("Automovil modificado correctamente")
        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()  

    def borrar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM AUTOMOVILES where marca='{}' and modelo='{}'".format(self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil Eliminado correctamente")
        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()

    def disponibilidad_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()

        
        
        try:
            conexion.miCursor.execute("SELECT cantidadDisponibles='{}' FROM AUTOMOVILES".format(self.cantidadDisponibles))
            conexion.miConexion.commit()
            cantidadDisponibles=conexion.miCursor.fetchall()
            print(cantidadDisponibles)
           
        except:
            print('No se puede mostrar Automoviles')
        finally:
            conexion.cerrarConexion()        
        

    def listadoAutomovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miConexion.execute("SELECT marca,modelo,precio,cantidadDisponibles FROM AUTOMOVILES".format(self.marca,self.modelo,self.precio,self.cantidadDisponibles) )
            autos=conexion.miCursor.fetchall()
            print(autos)
        finally:
            conexion.cerrarConexion()

    def valida_precio(self):
        while True:
            try:
                precio1 =float(input("por favor ingrese precio: "))
            except ValueError:
                print("Debe ingresar un valor numerico positivo.")
            else:
                if precio1<0:
                    print("El precio debe ser un valor positivo")
                if precio1>0:
                    return precio1



       
       

    
class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Concesionaria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()   


            
programa = ProgramaPrincipal()
programa.crearTablas()
programa.menu()
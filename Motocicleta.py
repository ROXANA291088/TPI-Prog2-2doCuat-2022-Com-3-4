from ast import Delete, Num
from importlib.util import module_for_loader
import sqlite3
from turtle import color


class ProgramaPrincipal:
    def menu(self):
        while True:
            print("Menu de opciones Motocicleta")
            print("1- Cargar Motocicleta")
            print("2- Motocicleta Precio Actualizado")
            print("3- Salir del Menu")
            
            nro = int(input("Por favor ingrese un número"))
            if nro == 1:
                marca = input("Por favor ingrese la marca de la Motocicleta: ")
                modelo = input("Por favor ingrese el modelo de la Motocicleta: ")
                precio = input("Por favor ingrese el precio de la Motocicleta: ")
                color  = input ("ingrese el color de la motocicleta")
                Motocicleta_nueva=Motocicleta(marca,modelo,precio,color)
                Motocicleta_nueva.cargar_Motocicleta()
            if nro == 2:
                marca = input("Por favor ingrese la marca de la Motocicleta: ")
                modelo = input("Por favor ingrese el modelo de la Motocicleta: ")
                precio_actualizado=Motocicleta(marca,modelo,precio=precio)
                precio_actualizado.actualizar_precio()
            if nro==0:
                break  

    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS MOTOCICLETA")
        conexion.miCursor.execute("CREATE TABLE MOTOCICLETA (id_moto INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),cilindrada VARCHAR(30),color VARCHAR(30),fechaUltimoPrecio(datetime),Precio INTEGER NOT NULL")    
        conexion.miConexion.commit()  
        conexion.miCursor.fetchall()     
        conexion.cerrarConexion()    

    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS HISTORICO_MOTOCICLETA")
        conexion.miCursor.execute("CREATE TABLE HISTORICO_MOTOCICLETA ("id_moto INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),cilindrada VARCHAR(30),color VARCHAR(30),fechaUltimoPrecio(datetime),Precio INTEGER NOT NULL")           




class Motocicleta:
    def __init__(self,marca, modelo,precio=None,color,cilindrada=True):
        self.marca = marca
        self.modelo = modelo
        self.precio=precio
        self.color=color
        self.cilindrada=True

    def cargar_Motocicleta(self):
        conexion =Conexiones()
        conexion.abrirConexion()
        try:
            
            conexion.miCursor.execute("INSERT INTO MOTOCICLETA(marca,modelo,precio,color,cilintrada) VALUES('{}', '{}','{}','{}','{}' )".format(self.marca, self.modelo,self.precio,self.color))
            conexion.miConexion.commit()
            print("Motocicleta cargada exitosamente")
        except:
            print("Error al agregar un Motocicleta")
        finally:
            conexion.cerrarConexion()   



       
class Conexiones:
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("MOTOCICLETA")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()   


            
programa = ProgramaPrincipal()
programa.crearTablas()
programa.menu()
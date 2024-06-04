from model.Conexion_db import conexionDB
from tkinter import messagebox as mb

def create_table():
	
    conexion = conexionDB()
      
    CONTROL = ("""CREATE TABLE IF NOT EXISTS "Control" (
	"ID"	INTEGER UNIQUE,
	"Cuenta"	TEXT NOT NULL COLLATE RTRIM,
	"Clave_Reaccion"	TEXT NOT NULL COLLATE RTRIM,
	"Fecha"	TEXT NOT NULL,
	"Tipo_de_Documento"	TEXT NOT NULL,
	"Material"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("Clave_Reaccion") REFERENCES "Investigacion"("Clave_Reaccion"),
	FOREIGN KEY("Cuenta") REFERENCES "Identificacion"("Cuenta"))""")


    INDENTIFICACION = ("""CREATE TABLE IF NOT EXISTS "Identificacion" (
	"Cuenta"	INTEGER UNIQUE,
	"Correo"	TEXT,
	"Numero Celular"	TEXT,
	"Nombre"	TEXT UNIQUE,
	"Carrera "	TEXT,
	"Posgrado "	TEXT,
	PRIMARY KEY("Cuenta"))""")

    INVESTIGACION = ("""CREATE TABLE IF NOT EXISTS "Investigacion" (
	"Clave_Reaccion"	INTEGER UNIQUE,
	"Nombre " TEXT UNIQUE,
	"Inicio_Fin" TEXT,
	"Estatus "	TEXT,
	PRIMARY KEY("Clave_Reaccion"))""")

    Login_datos = ("""CREATE TABLE IF NOT EXISTS "Login_datos" (
	"ID"	INTEGER,
	"Cuenta"	INTEGER,
	"Password"	INTEGER,
	PRIMARY KEY("ID" AUTOINCREMENT),
    FOREIGN KEY("Cuenta") REFERENCES "Identificacion"("Cuenta"))""")

    conexion.cursor.execute(CONTROL)
    conexion.cursor.execute(INDENTIFICACION)
    conexion.cursor.execute(INVESTIGACION)
    conexion.cursor.execute(Login_datos)

    conexion.cerrar()

create_table()

class Control_Nuevo:
    def __init__(self, Clave_Reaccion, Cuenta, Fecha, Tipo_de_Documento):
        self.ID = None
        self.Clave_Reaccion = Clave_Reaccion
        self.Cuenta = Cuenta
        self.Fecha = Fecha 
        self.Tipo_de_Documento = Tipo_de_Documento
    def __str__(self):
        return f'CNTRL[{self.Clave_Reaccion},{self.Cuenta}, {self.Fecha}, {self.Tipo_de_Documentos}]'


def Nuevo(control_nuevo):
    conexion = conexionDB()
    CONTROL = f"""INSERT INTO Control (Clave_Reaccion, Cuenta, Fecha, Tipo_de_Documento)
    VALUES('{control_nuevo.Clave_Reaccion}','{control_nuevo.Cuenta}','{control_nuevo.Fecha}','{control_nuevo.Tipo_de_Documento}')"""

    try:    
        conexion.cursor.execute(CONTROL)
        titulo = 'Conexion a la base de datos'
        mensaje = 'El registro fue exitoso' 
        mb.showinfo(titulo,mensaje)
        conexion.cerrar()

    except:
        titulo = 'Conexion a la base de datos'
        mensaje = 'Error de registro' 
        mb.showwarning(titulo,mensaje)
        

def listar():
    conexion = conexionDB()

    Lista_Control = []
    sql='SELECT * FROM Control'

    conexion.cursor.execute(sql)
    Lista_Control = conexion.cursor.fetchall()
    conexion.cerrar() 

    return Lista_Control

def editar(control_nuevo, ID):
    conexion = conexionDB ()

    sql = f"""UPDATE Control
    SET Clave_Reaccion = '{control_nuevo.Clave_Reaccion}', Cuenta = '{control_nuevo.Cuenta}', 
    Fecha = '{control_nuevo.Fecha}', Tipo_de_Documento = '{control_nuevo.Tipo_de_Documento}'
    WHERE ID = {ID}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Editar registro'
        mensaje = 'Se ha editado el registro'
        mb.showerror(titulo,mensaje)
    except: 
        titulo = 'Editar registro'
        mensaje = 'No se ha podido editar el registro'
        mb.showerror(titulo,mensaje)
        

def eliminar(ID):
    conexion = conexionDB()
    sql = f"""DELETE FROM Control WHERE ID = {ID}"""
    


    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo='Eliminar registro'
        mensaje = 'Se ha eliminado el registro'
        mb.showerror(titulo,mensaje)
        
    except: 
        titulo = 'Eliminar registro'
        mensaje = 'No se ha podido eliminar el registro'
        mb.showerror(titulo,mensaje)
       
def busca_users(users):
        conexion = conexionDB()
        sql = "SELECT * FROM login_datos WHERE cuenta = {}".format(users)
        conexion.cursor.execute(sql)
        usersx = conexion.cursor.fetchall()
        conexion.cerrar()     
        return usersx 

def busca_password(password):
        conexion = conexionDB()
        sql = "SELECT * FROM login_datos WHERE Password = {}".format(password) #
        conexion.cursor.execute(sql)
        passwordx = conexion.cursor.fetchall()
        conexion.cerrar()     
        return passwordx
        



         
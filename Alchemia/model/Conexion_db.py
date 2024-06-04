import sqlite3

class conexionDB:
    def __init__(self):
        self.bade_datos ='/Users/topo/Desktop/Alchemia#4/Alchemia/BDLAB224.db'
        self.conexion = sqlite3.connect(self.bade_datos)
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()

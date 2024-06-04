import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk, Image
import sqlite3
from GUI.GUI_app import Fr, barra_menu
from tkmacosx import Button

# Configuración de la ventana Principal

def main():
    Root = tk.Tk()
    Root.title("Base de Datos")
    Icono = tk.PhotoImage(file="/Users/topo/Desktop/Alchemia#4/Alchemia/Image/FQ.png")
    Root.iconphoto(True, Icono)
    Root.resizable(0,0)
    barra_menu(Root)

    app = Fr(Root = Root)


    app.mainloop()

if __name__ == '__main__':
    main()

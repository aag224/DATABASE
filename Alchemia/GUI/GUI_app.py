import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk, Image
import sqlite3
from tkinter import Canvas
from tkmacosx import Button
from tkinter import ttk
from model.Control_dao import Control_Nuevo, Nuevo, listar, editar, eliminar, busca_password, busca_users
from model.Conexion_db import conexionDB
from tkinter import filedialog
from tkinter import Canvas




class Fr(tk.Frame):
    def __init__(self,Root = None):
        super().__init__(Root, width=840, height=430)
        self.Root = Root
        self.pack()
        self.ID = None
        self.config(bg="white")  
        self.campos_control()
        self.tabla_Control()

    def campos_control(self):
        #Etiquetas
        self.label_CI = tk.Label(self, text = 'Clave Investigador: ')
        self.label_CI.config(bg="white",fg="black",font=("Open Sans",16, 'bold'))
        self.label_CI.grid(row=0,column=0, padx=2, pady=10)

        self.label_PW = tk.Label(self, text = 'Contraseña: ')
        self.label_PW.config(bg="white",fg="black",font=("Open Sans",16, 'bold'))
        self.label_PW.grid(row=1,column=0, padx=2, pady=10)
        
        self.CR = tk.Label(self, text = 'Clave Reaccion: ')
        self.CR.config(bg="white",fg="black",font=("Open Sans",16, 'bold'))
        self.CR.grid(row=2,column=0, padx=2, pady=10)

        self.label_DT = tk.Label(self, text = 'Fecha: ')
        self.label_DT.config(bg="white",fg="black",font=("Open Sans",16, 'bold'))
        self.label_DT.grid(row=3,column=0, padx=2, pady=10)

        self.label_TD = tk.Label(self, text = 'Tipo de documento: ')
        self.label_TD.config(bg="white",fg="black",font=("Open Sans",16, 'bold'))
        self.label_TD.grid(row=4,column=0, padx=2, pady=10)

        self.label_D = tk.Label(self, text = 'Material de investigación: ')
        self.label_D.config(bg="white",fg="black",font=("Open Sans",16, 'bold'))
        self.label_D.grid(row=5,column=0, padx=2, pady=10)

        
        
        #Entradas
        self.CI = tk.StringVar()
        self.entry_CI = tk.Entry(self, textvariable = self.CI)
        self.entry_CI.config(width=55, bg="White",fg="black",font=("Open Sans",16), cursor='hand2')
        self.entry_CI.grid(row=0, column=1, padx=5, pady=5, columnspan=3)

        
        self.PW = tk.StringVar()
        self.entry_PW = tk.Entry(self, textvariable = self.PW)
        self.entry_PW.config(width=55, bg="white",fg="black",font=("Open Sans",16), cursor='hand2')
        self.entry_PW.grid(row=1, column=1, padx=5, pady=5, columnspan=3)
        self.entry_PW['show']='*'
        
        
        self.CR = tk.StringVar()
        self.entry_CR = tk.Entry(self, textvariable = self.CR)
        self.entry_CR.config(width=55, bg="white",fg="black",font=("Open Sans",16), cursor='hand2')
        self.entry_CR.grid(row=2, column=1, padx=5, pady=5, columnspan=3)

        self.DT = tk.StringVar()
        self.entry_DT = tk.Entry(self, textvariable = self.DT)
        self.entry_DT.config(width=55, bg="white",fg="black",font=("Open Sans",16), cursor='hand2')
        self.entry_DT.grid(row=3, column=1, padx=5, pady=5, columnspan=3)

        self.TD = tk.StringVar()
        self.entry_TD = tk.Entry(self, textvariable = self.TD)
        self.entry_TD.config(width=55, bg="white",fg="black",font=("Open Sans",16), cursor='hand2')
        self.entry_TD.grid(row=4, column=1, padx=5, pady=5, columnspan=3)

        self.D = tk.StringVar()
        self.entry_D = tk.Entry(self, textvariable = self.D)
        self.entry_D.config(width=55, bg="white",fg="black",font=("Open Sans",16), cursor='hand2')
        self.entry_D.grid(row=5, column=1, padx=0, pady=5, columnspan=3)


        #Botones
        self.boton_actualizar = Button(self,text="Actualizar", command = self.editar_datos)
        self.boton_actualizar.config(width=150, font=('Open Sans', 16,'bold'), fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.boton_actualizar.grid(row=8, column=1, pady=30, padx=15)
        
        self.boton_Nuevo = Button(self,text="Nuevo", command = self.verificacion_Nuevo)
        self.boton_Nuevo.config(width=170, font=('Open Sans', 16,'bold'), fg='#DAD5D6', bg='#1658A2', cursor='hand2',activebackground='#3586DF')
        self.boton_Nuevo.grid(row=8, column=0, pady=30, padx=0)

        self.boton_Ver_Material = Button(self,text="Ver Material")
        self.boton_Ver_Material.config(width=150, font=('Open Sans', 16,'bold'), fg='#DAD5D6', bg='#F28D0D', cursor='hand2',activebackground='#F3BF7D')
        self.boton_Ver_Material.grid(row=8, column=2, pady=30, padx=15)

        self.boton_Eliminar = Button(self,text="Eliminar", command = self.verificacion_Eliminar)
        self.boton_Eliminar.config(width=150, font=('Open Sans', 16,'bold'), fg='#DAD5D6', bg='#BD152E', cursor='hand2',activebackground='#E15370')
        self.boton_Eliminar.grid(row=8, column=3, pady=30, padx=0)

        self.boton_Examinar = Button(self,text="Buscar", command= self.OpenFile)
        self.boton_Examinar.config(width=180, font=('Open Sans', 16,'bold'), fg='#434343', bg='#E9E6E3', cursor='hand2',activebackground='#F8F8F8')
        self.boton_Examinar.grid(row=5, column=3, pady=5, padx=0)

    def habilitar(self):
        self.entry_CI.config(state='normal')
        self.entry_CR.config(state='normal')
        self.entry_DT.config(state='normal')
        self.entry_TD.config(state='normal')

        self.boton_actualizar.config(state='normal')
        self.boton_Nuevo.config(state='normal')
        self.boton_Ver_Material.config(state='normal')
        self.boton_Eliminar.config(state='normal')
    
    def deshabilitar(self):
        self.entry_CI.config(state='disabled')
        self.entry_CR.config(state='disabled')
        self.entry_DT.config(state='disabled')
        self.entry_TD.config(state='disabled')

        self.boton_actualizar.config(state='disabled')
        self.boton_Nuevo.config(state='disabled')
        self.boton_Ver_Material.config(state='disabled')
        self.boton_Eliminar.config(state='disabled')
   
    def Nuevos_Datos(self):
        control_nuevo= Control_Nuevo(
            self.CR.get(),
            self.CI.get(),
            self.DT.get(),
            self.TD.get(),
        )
        if self.ID == None:
            Nuevo(control_nuevo)
        else:
            editar(control_nuevo, self.ID)

        self.reset_inputs()
        self.tabla_Control()
        self.reset_ID()
    
    def reset_inputs(self):
        self.CI.set('')
        self.CR.set('') 
        self.DT.set('') 
        self.TD.set('')
        self.PW.set('')   
        self.D.set('')  

    def tabla_Control(self): 
        self.lista = listar()
        self.lista.reverse()
        self.tabla = ttk.Treeview(self,
        column=('Clave Reacción', 'Cuenta', 'Fecha', 'Tipo de Documento', 'Material'))
        self.tabla.grid(row=9, column=0, columnspan=4, sticky='nse')

        #Screllbar 
        self.scroll = ttk.Scrollbar(self,
                                    orient = 'vertical', command = self.tabla.yview)
        self.scroll.grid(row = 9, column =4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.column('#0',width=80)
        self.tabla.column('#1',width=120)
        self.tabla.column('#2',width=100)
        self.tabla.column('#3',width=100)
        self.tabla.column('#4',width=150)
        self.tabla.column('#5',width=250)
        
        
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Cuenta')
        self.tabla.heading('#2', text='Clave Reaccion')
        self.tabla.heading('#3', text='Fecha')
        self.tabla.heading('#4', text='Tipo de Documento')
        self.tabla.heading('#5', text='Material')

        #Iterar la lista de cotrol con un For 

        for p in self.lista:
            self.tabla.insert('',0, text=p[0], 
                              values=(p[1], p[2], p[3], p[4], p[5]))

    def reset_ID(self):
        self.ID = None

    def editar_datos(self):
        try:
            self.reset_inputs()
            self.ID = self.tabla.item(self.tabla.selection())['text']
            self.Clave_Reaccion = self.tabla.item(self.tabla.selection())['values'][2]
            self.Cuenta = self.tabla.item(self.tabla.selection())['values'][0]
            self.Fecha = self.tabla.item(self.tabla.selection())['values'][3]
            self.Tipo_de_Documento = self.tabla.item(self.tabla.selection())['values'][4]

            self.entry_CR.insert(2, self.Clave_Reaccion)
            self.entry_CI.insert(0, self.Cuenta)
            self.entry_DT.insert(3, self.Fecha)
            self.entry_TD.insert(4, self.Tipo_de_Documento)
            #self.ID = None

            

        except:
            titulo = 'Editar registro'
            mensaje = 'No se ha seleccionado el registro'
            mb.showerror(titulo,mensaje)
            self.ID = None

    def eliminar_datos(self):

        try:
            self.ID = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.ID)

            self.tabla_Control()
            self.ID = None
            self.reset_inputs()
        

        except:
            titulo = 'Eliminar registro'
            mensaje = 'No se ha seleccionado el registro'
            mb.showerror(titulo,mensaje)
            self.ID = None

    def OpenFile(self):
        filepath = filedialog.askopenfilename()
        file = open(filepath,'r')
        self.mensaje = file.read()
        mb.showerror(self.mensaje)

    def verificacion_Eliminar(self):
        users_entry = self.CI.get()
        password_entry = self.PW.get()
        
        
        users_entry = str("'" + users_entry + "'")
        password_entry = str("'" + password_entry + "'")
            
        dato1 = busca_users(users_entry)
        dato2 = busca_password(password_entry)
             
            
        if dato1 == dato1:	
            if dato1 == [] and dato2 ==[]:
                self.titulo = 'Error'
                self.mensaje = 'Usuario o contraseña erroneas'
                mb.showerror(self.titulo,self.mensaje)
            else:
                    
                if dato1 ==[]:
                    self.titulo = 'Error'
                    self.mensaje = 'Usuario o contraseña erroneas'
                    mb.showerror(self.titulo,self.mensaje)
                else:
                    dato1 = dato1[0][1]
                    
                if dato2 ==[]:
                    self.titulo = 'Error'
                    self.mensaje = 'Usuario o contraseña erroneas'
                    mb.showerror(self.titulo,self.mensaje)
                else:
                    dato2 = dato2[0][2]
                    
                if dato1 != [] and dato2 != []:
                    self.eliminar_datos()
        else:
            self.titulo = 'Error'
            self.mensaje = 'Usuario o contraseña erroneas'
            mb.showerror(self.titulo,self.mensaje)

    def verificacion_Actualizar(self):
        users_entry = self.CI.get()
        password_entry = self.PW.get()
        
        
        users_entry = str("'" + users_entry + "'")
        password_entry = str("'" + password_entry + "'")
            
        dato1 = busca_users(users_entry)
        dato2 = busca_password(password_entry)
             
            
        if dato1 == dato1:	
            if dato1 == [] and dato2 ==[]:
                self.titulo = 'Error'
                self.mensaje = 'Usuario o contraseña erroneas'
                mb.showerror(self.titulo,self.mensaje)
            else:
                    
                if dato1 ==[]:
                    self.titulo = 'Error'
                    self.mensaje = 'Usuario o contraseña erroneas'
                    mb.showerror(self.titulo,self.mensaje)
                else:
                    dato1 = dato1[0][1]
                    
                if dato2 ==[]:
                    self.titulo = 'Error'
                    self.mensaje = 'Usuario o contraseña erroneas'
                    mb.showerror(self.titulo,self.mensaje)
                else:
                    dato2 = dato2[0][2]
                    
                if dato1 != [] and dato2 != []:
                    self.editar_datos()
        else:
            self.titulo = 'Error'
            self.mensaje = 'Usuario o contraseña erroneas'
            mb.showerror(self.titulo,self.mensaje)
    
    def verificacion_Nuevo(self):
        users_entry = self.CI.get()
        password_entry = self.PW.get()
        
        
        users_entry = str("'" + users_entry + "'")
        password_entry = str("'" + password_entry + "'")
            
        dato1 = busca_users(users_entry)
        dato2 = busca_password(password_entry)
             
            
        if dato1 == dato1:	
            if dato1 == [] and dato2 ==[]:
                self.titulo = 'Error'
                self.mensaje = 'Usuario o contraseña erroneas'
                mb.showerror(self.titulo,self.mensaje)
            else:
                    
                if dato1 ==[]:
                    self.titulo = 'Error'
                    self.mensaje = 'Usuario o contraseña erroneas'
                    mb.showerror(self.titulo,self.mensaje)
                else:
                    dato1 = dato1[0][1]
                    
                if dato2 ==[]:
                    self.titulo = 'Error'
                    self.mensaje = 'Usuario o contraseña erroneas'
                    mb.showerror(self.titulo,self.mensaje)
                else:
                    dato2 = dato2[0][2]
                    
                if dato1 != [] and dato2 != []:
                    self.Nuevos_Datos()
        else:
            self.titulo = 'Error'
            self.mensaje = 'Usuario o contraseña erroneas'
            mb.showerror(self.titulo,self.mensaje)
            
    
   




img1 = None
def VentanaDiagrama():
    global img1
    VentanaDiagrama = tk.Toplevel()
    VentanaDiagrama.title("Diagrama Relacional")
    VentanaDiagrama.geometry("1000x1000+50+100")
    VentanaDiagrama.config(bg = "white")
 
    canvas = Canvas(VentanaDiagrama, width=1000,height=770)  # Ajusta las dimensiones según sea necesario
    canvas.pack()
    canvas.config(bg="white") #Mismo color de fondo que la ventna para no notarse 
    canvas.config(borderwidth=0, relief="solid", highlightbackground="white") 

    # Carga la imagen 
    if img1 is None:
        img1 = Image.open("/Users/topo/Desktop/Alchemia#4/Alchemia/Image/Diagrama Relacional.png")
        img1 = ImageTk.PhotoImage(img1)

    canvas.create_image(60, 60, anchor=tk.NW, image=img1)  

def LoginSU():
    LoginSU = tk.Toplevel()
    LoginSU.title("Inicio de sesión")
    LoginSU.geometry("300x177+860+50")
    LoginSU.config(bg = "white")

    Label(LoginSU, text="Cuenta : ", bg="white", font=("Open Sans", 15), fg="black").pack()
    caja3 = Entry(LoginSU, bg="white", fg="black")
    caja3.pack()

    Label(LoginSU, text="Contraseña : ", bg="white", font=("Open Sans", 15), fg="black").pack()
    caja4 = Entry(LoginSU, bg="white", fg="black")
    caja4.pack()

    def verificacion():
        users_entry=caja3.get()
        password_entry=caja4.get() 		

        users_entry = str("'" + users_entry + "'")
        password_entry = str("'" + password_entry + "'")

        dato1 = busca_users(users_entry)
        dato2 = busca_password(password_entry)
        
        if dato1 == dato2:	
                if dato1 == [] and dato2 ==[]:
                    titulo = 'Error'
                    mensaje = 'Usuario o contraseña erroneas'
                    mb.showerror(titulo,mensaje)
                else:

                    if dato1 ==[]:
                        titulo = 'Error'
                        mensaje = 'Usuario o contraseña erroneas'
                        mb.showerror(titulo,mensaje)
                    else:
                        dato1 = dato1[0][1]

                    if dato2 ==[]:
                        titulo = 'Error'
                        mensaje = 'Usuario o contraseña erroneas'
                        mb.showerror(titulo,mensaje)
                    else:
                        dato2 = dato2[0][2]

                    if dato1 != [] and dato2 != []:
                        SuperUsuario()
                        
                        
        else:
            titulo = 'Error'
            mensaje = 'Usuario o contraseña erroneas'
            mb.showerror(titulo,mensaje)


    Button(LoginSU, text= 'Iniciar Sesion', command=verificacion, width=192, activebackground='#3586DF', bg='#E9E6E3',fg='#434343',font=('Open Sans', 16,'bold')).pack(pady=25)
    estilo = ttk.Style()
    estilo.configure("TProgressbar", foreground='red', background='black',troughcolor='DarkOrchid1',bordercolor='#970BD9',lightcolor='#970BD9', darkcolor='black')



def barra_menu(Root):
    barra_menu = tk.Menu(Root)
    Root.config(menu = barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu) 
    barra_menu.add_cascade(label="Opciones", menu = menu_inicio)
    menu_inicio.add_command(label="salir", command = Root.destroy)
    
    menu_ayuda = tk.Menu(barra_menu)
    barra_menu.add_cascade(label="Ayuda", menu = menu_ayuda)
    menu_ayuda.add_command(label="Diagrama Relacional", command= VentanaDiagrama)

    menu_SuperUsuario = tk.Menu(barra_menu)
    barra_menu.add_cascade(label="Administrador", menu = menu_SuperUsuario)
    menu_SuperUsuario.add_command(label="Iniciar Sesion", command = LoginSU)



#OPCIONES DE SUPER USUARIO
img2 = None
def SuperUsuario():
        global img2
        SuperUsurario= tk.Toplevel()
        SuperUsurario.title("Opciones de super usuaraio")
        SuperUsurario.geometry("1000x500+50+50")
        SuperUsurario.config(bg="white")
        Icono = tk.PhotoImage(file="/Users/topo/Desktop/Alchemia#4/Alchemia/Image/FQ.png")
        SuperUsurario.iconphoto(True, Icono)
        labelExample = tk.Label(SuperUsurario, text="Seleccione tabla : ", bg="white", font=("Open Sans", 16), fg="black").pack(side="top")

        canvas = Canvas(SuperUsurario, width=1000,height=770)  # Ajusta las dimensiones según sea necesario
        canvas.pack()
        canvas.config(bg="white") #Mismo color de fondo que la ventna para no notarse 
        canvas.config(borderwidth=0, relief="solid", highlightbackground="white") 

        # Carga la imagen 
        if img2 is None:
            img2 = Image.open("/Users/topo/Desktop/Alchemia#4/Alchemia/Image/diagrama relacional.jpg")
            img2 = ImageTk.PhotoImage(img2)

        canvas.create_image(60, 40, anchor=tk.NW, image=img2)  


        # Botones

        boton1=Button(SuperUsurario,text="Identificacion",font=("Open Sans",22), fg="black")
        boton1.place(x = 640, y = 170, width=200, height=30)

        boton2=Button(SuperUsurario,text="Control",font=("Open Sans",22), fg="black")
        boton2.place(x = 640, y = 370, width=200, height=30)

        boton3=Button(SuperUsurario,text="Investigacion",font=("Open Sans",22), fg="black")
        boton3.place(x = 640, y = 70, width=200, height=30)

        boton4=Button(SuperUsurario,text="Login Datos",font=("Open Sans",22), fg="black")
        boton4.place(x = 640, y = 270, width=200, height=30)



 
 
 
 
 

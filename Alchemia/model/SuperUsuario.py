



def VentanaControl():
	global img1
	global img2 
	global img3  
	VentanaControl = tk.Toplevel(ventana)
	VentanaControl.title("Control")
	VentanaControl.geometry("940x400+50+50")
	VentanaControl.config(bg = "white")


	#Creamos un Canvas para poder adjuntar las imagenes, por ser una ventana TopLevel no se pueden adjuntar como labels 

	canvas = Canvas(VentanaControl, width=940,height=300)  # Ajusta las dimensiones según sea necesario
	canvas.pack()
	canvas.config(bg="white") #Mismo color de fondo que la ventna para no notarse 
	canvas.config(borderwidth=0, relief="solid", highlightbackground="white") 

    # Carga la imagen 
	if img1 is None:
		img1 = Image.open("/Users/topo/Desktop/INSERT.jpg")
		img1 = ImageTk.PhotoImage(img1)

	canvas.create_image(60, 60, anchor=tk.NW, image=img1)  

	if img2 is None:
		img2 = Image.open("/Users/topo/Desktop/UPDATE.jpg")
		img2 = ImageTk.PhotoImage(img2)

	canvas.create_image(370, 60, anchor=tk.NW, image=img2)  

	if img3 is None:
		img3 = Image.open("/Users/topo/Desktop/DELETE.jpg")
		img3 = ImageTk.PhotoImage(img3)

	canvas.create_image(690, 60, anchor=tk.NW, image=img3)   
	
	boton1=Button(VentanaControl,text="REGISTRO",command=nuevaVentanaCon,font=("Open Sans",22), fg="black")
	boton1.place(x = 60, y = 310, width=200, height=30)

	boton2=Button(VentanaControl,text="ACTUALIZAR",command=nuevaVentana2Con,font=("Open SansS",22), fg="black")
	boton2.place(x = 370, y = 310, width=200, height=30)

	boton3=Button(VentanaControl,text="ELIMINAR",command=nuevaVentana3Con,font=("Open Sans",22), fg="black")
	boton3.place(x = 690, y = 310, width=200, height=30)


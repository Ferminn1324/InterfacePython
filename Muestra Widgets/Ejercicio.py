from tkinter import *
from tkinter import ttk
from tkinter import messagebox

raiz = Tk()

raiz.title("Muestra Widgets")

Nombre = StringVar()
APaterno = StringVar()
AMaterno = StringVar()
Correo = StringVar()
movil = StringVar()
estado = StringVar()


mainFrame = ttk.Frame(raiz,padding=" 15 15 15 15")
mainFrame.grid(column=0,row=0)

mainFramee = ttk.Frame(mainFrame,padding="15 15 15 15",relief="raised")
mainFramee.grid(column=0,row=0,sticky=(W))

mainFrame3 = ttk.Frame(mainFrame,padding="38 15 38 15",relief="raised")
mainFrame3.grid(column=0,row=1,pady=20,sticky=(W))

mainFrame4 = ttk.Frame(mainFrame,padding="15 15 15 15")
mainFrame4.grid(column=1,row=0,sticky=(W))

#Framee
Nombre = ttk.Entry(mainFramee, width=40, textvariable=Nombre)
Nombre.grid(column=1,row=0)
APaterno = ttk.Entry(mainFramee, width=40, textvariable=APaterno)
APaterno.grid(column=1,row=1)
AMaterno = ttk.Entry(mainFramee, width=40, textvariable=AMaterno)
AMaterno.grid(column=1, row=2)
Correo = ttk.Entry(mainFramee, width=40,textvariable=Correo)
Correo.grid(column=1,row=3)
movil = ttk.Entry(mainFramee,width=40,textvariable=movil)
movil.grid(column=1,row=4)

ttk.Label(mainFramee, text="Nombre:").grid(column=0, row=0,pady=20)
ttk.Label(mainFramee, text="A.Paterno:").grid(column=0, row=1,pady=20)
ttk.Label(mainFramee, text="A.Materno:").grid(column=0, row=2,pady=20)
ttk.Label(mainFramee, text="Correo:").grid(column=0, row=3,pady=20)
ttk.Label(mainFramee, text="Movil:").grid(column=0, row=4,pady=20)
#MAINFRAME3
ttk.Label(mainFrame3,text="Aficiones:").grid(column=0,row=0,sticky=(W))

ttk.Checkbutton(mainFrame3,text="Leer:").grid(column=0, row=1, sticky=(W),padx=10)
ttk.Checkbutton(mainFrame3,text="Musica:").grid(column=1,row=1,sticky=(W),padx=10)
ttk.Checkbutton(mainFrame3,text="Videojuegos:").grid(column=2,row=1,sticky=(W),padx=10)

ttk.Button(mainFrame,text="Guardar").grid(column=0,row=2,sticky=(W))
ttk.Button(mainFrame,text="Cancelar").grid(column=0,row=2,pady=20,sticky=(W),padx=100)

ttk.Radiobutton(mainFrame4,text="Estudiante").grid(column=0,row=0,sticky=(W),padx=30)
ttk.Radiobutton(mainFrame4,text="Empleado").grid(column=0,row=1,sticky=(W),padx=30)
ttk.Radiobutton(mainFrame4,text="Desempleado").grid(column=0,row=2,sticky=(W),padx=30)

comboboxestados = ttk.Combobox(mainFrame,textvariable=estado)
comboboxestados.grid(column=1,row=1)
comboboxestados['values'] = ("Aguascalientes",
                            "Baja California","Baja California Sur", "Campeche","Coahuila",
                            "Colima","Chiapas","Chihuahua","Durango","Distrito Federal","Guanajuato",
                            "Guerrero","Hidalgo","Jalisco","México","Michoacán","Morelos", "Nayarit", 
                            "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", 
                            "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", 
                            "Zacatecas")
















raiz.mainloop()
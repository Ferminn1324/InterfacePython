from tkinter import *
from tkinter import ttk
from tkinter import messagebox



class Sesion:
    def __init__(self,raiz):
        raiz.title("Inicio de sesion")


        self.usuario = StringVar()
        self.Contraseña = StringVar()

        mainFrame = ttk.Frame(raiz,padding="10 10 12 12")
        mainFrame.grid(column=1, row=0)

        self.usuarioEntry = ttk.Entry(mainFrame, width=25, textvariable=self.usuario)
        self.usuarioEntry.grid(column=1,row=0,pady=10)
        
        self.ContraseñaEntry = ttk.Entry(mainFrame,width=25,textvariable=self.Contraseña)
        self.ContraseñaEntry.grid(column=1,row=2,pady=10)


        ttk.Label(mainFrame, text= "Usuario:").grid(column=0,row=0,pady=10)
        #ttk.Label(mainFrame,text="").grid(column=0,row=1)
        #ttk.Label(mainFrame,text="").grid(column=0,row=3)
        ttk.Label(mainFrame,text ="Contraseña:").grid(column=0,row=2,pady=10)
        #ttk.Label(mainFrame,text="").grid(column=0,row=3)
        
        ttk.Button(mainFrame,text= "Ingresar").grid(column=1,row=4,sticky=(E,S),pady=10)


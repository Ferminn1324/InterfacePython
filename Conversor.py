#Conversor de pies a metros 

from tkinter import *
# * significa con todos los elementos 
from tkinter import ttk
from tkinter import messagebox

class Conversor:
    def __init__(self,raiz):
        raiz.title("Pies a Metros")

        self.pies = StringVar()
        self.metros = StringVar()

        mainFrame = ttk.Frame(raiz, padding="10 10 30 30")#Padding(Izquierda,Arriba, Derecha, Abajo)
        mainFrame.grid(column=1, row=0)
        
        self.PiesEntry = ttk.Entry(mainFrame, width=12, textvariable=self.pies)
        self.PiesEntry.grid(column=1, row=0,sticky=(W,E))

        ttk.Label(mainFrame, text= "pies").grid(column=2,row=0)
        ttk.Label(mainFrame,text ="Son equivalentes a").grid(column=0,row=1)
        ttk.Label(mainFrame,textvariable=self.metros).grid(column=1,row=1)
        ttk.Label(mainFrame,text ="Metros").grid(column=2,row=1)

        ttk.Button(mainFrame,text= "Convertir",command=self.Calcular).grid(column=2,row=2)
        self.PiesEntry.focus()
        #Hacer la operacion haciendo enter
        raiz.bind("<Return>",self.Calcular)

    def Calcular(self,*args):

        print("Boton Presionado") 
        piesUsuario =self.pies.get() #Siempre devuelve cadena.
        print("Pies Ingresados",piesUsuario)
        try:
           piesFlotante = float(piesUsuario)#Conversion de cadena a flotante
           metros = piesFlotante * 0.3048
           print("Metros:", metros)
           self.metros.set(metros)
        except:
            messagebox.showinfo("Error")
            print("No es un dato valido.")
            self.pies.set("")



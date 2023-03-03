#Conversor de pies a metros 

from tkinter import *
# * significa con todos los elementos 
from tkinter import ttk

class Conversor:
    def __init__(self,raiz):
        raiz.title("Pies a Metros")

        self.pies = StringVar()
        self.metros = StringVar()

        mainFrame = ttk.Frame(raiz)
        mainFrame.grid(column=1, row=0)
        
        PiesEntry = ttk.Entry(mainFrame, textvariable=self.pies)
        PiesEntry.grid(column=1, row=0)
        ttk.Label(mainFrame, text= "pies").grid(column=2,row=0)
        ttk.Label(mainFrame,text ="Son equivalentes a").grid(column=0,row=1)
        ttk.Label(mainFrame,textvariable=self.metros).grid(column=1,row=1)
        ttk.Label(mainFrame,text ="Metros").grid(column=2,row=1)

        ttk.Button(mainFrame,text= "Convertir",command=self.Calcular).grid(column=2,row=2)
        #Hacer la operacion haciendo enter
        raiz.bind("<Return>",self.Calcular)

    def Calcular(self,*args):

        print("Boton Presionado") 
        piesUsuario =self.pies.get() #Siempre devuelve cadena.
        print("Pies Ingresados",piesUsuario)
        piesFlotante = float(piesUsuario)#Conversion de cadena a flotante
        metros = piesFlotante * 0.3048
        print("Metros:", metros)
        self.metros.set(metros)
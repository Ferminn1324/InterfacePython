from tkinter import *
from tkinter import ttk
import tkinter as ttk

raiz = Tk()
boton = ttk.Button(raiz, text="Boton solo texto")
boton.grid()

imagen = PhotoImage(file="perrito.png")

btnImagen = ttk.Button(raiz)
btnImagen.grid()
btnImagen['image'] = imagen

btnCombinada = ttk.Button(raiz, text="Boton Combinado", compound="bottom",)
btnCombinada.grid()
btnCombinada['image'] = imagen

chkBoton = ttk.Checkbutton(raiz, text="Opcion 1")
chkBoton.grid()

raiz.mainloop()
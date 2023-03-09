from tkinter import *
from tkinter import ttk

raiz = Tk()
etqTexto  = ttk.Label(raiz, text="Etiqueta solo texto")
etqTexto.grid()

imagen = PhotoImage(file="bicho1.png")

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen['image'] = imagen

raiz.mainloop()
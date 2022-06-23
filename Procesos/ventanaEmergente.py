from tkinter import *
from Procesos.ProcesosGui import *


class VentanaEmergente:
    def __init__(self, aviso,nombre1, nombre2, mensaje, funcion=None):
        # Requisitos ----
        self.nameop1=nombre1
        self.nameop2=nombre2
        self.msgAviso=aviso
        self.funcion=funcion
        self.mensaje=mensaje
        # Ventana Emergente ---
        self.ventana=Toplevel()
        self.ventana.overrideredirect(1)
        # Instancias ---
        self.objGui=ProcesosGui()
        self.objGui.center(self.ventana, 250, 150)

        self.getFrame()
        self.getLabel()
        self.getButtons()
    
    def getFrame(self):
        self.contAviso=Frame(self.ventana, bg="#0C3652")
        self.contAviso.place(relx=0, rely=0, relwidth=1, relheight=.15)

        self.contMensaje=Frame(self.ventana, bg="#fff")
        self.contMensaje.place(relx=0, rely=.15, relwidth=1, relheight=.60)

        self.contButtons=Frame(self.ventana)
        self.contButtons.config(bg="#000")
        self.contButtons.place(relx=0, rely=.75, relwidth=1, relheight=1)

        self.extra=Frame(self.contButtons)
        self.extra.pack(pady=5)


    def getLabel(self):
        aviso=Label(self.contAviso, text=self.msgAviso)
        aviso.config(bg="#0C3652")
        aviso.pack( )

        mensaje=Text(self.contMensaje, width=200, height=100)
        mensaje.insert("end", self.mensaje)
        mensaje.config(state="disabled")

        mensaje.config(bg="white")
        mensaje.place(x=0, y=0)

    
    def getButtons(self):
        x=10
        y=2
        opcion1=Button(self.extra, text=self.nameop1, command=lambda:self.cerrar())
        opcion1.config(bg="#fff")
        opcion1.grid(row=0, column=0, ipadx=x, ipady=y)

        opcion2=Button(self.extra, text=self.nameop2, command=lambda:[self.funcion(), self.cerrar()])
        opcion2.config(bg="#fff")
        opcion2.grid(row=0, column=1, ipadx=x, ipady=y)
        
    def cerrar(self):
        self.ventana.destroy()
        

   

# root=Tk()

# def saludar():
#     print("Hola")

# test=VentanaEmergente("ADVERTENCIA","NO", "SI", "Desea continuar con los cambios", saludar)

# root.mainloop()

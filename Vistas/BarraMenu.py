from tkinter import *
from Procesos.ProcesosGui import *
from Procesos.ventanaEmergente import *
from Vistas.Login import *
from Impl.inicio import *

class BarraMenu:
    def __init__(self, contenedor, raiz, fm3):
        self.objGui=ProcesosGui()
        # Contadores para los generar elementos de los items del menu----------
        # Se agrega un contador por cada item de la barra de menu
        self.contenedor=contenedor
        self.raiz=raiz
        self.contenedorTabla=fm3
        # self.contador1=0
        self.contador2=0
        self.contador3=0

        # Contador cambio de color
        self.contadorModo=0

        # Contenedor barra menu
        self.cBM=Frame(contenedor)
        # self.cBM.place(relx=0, rely=0) -- Buena
        self.cBM.pack(side="right", anchor="center")
        # self.cBM.place(relx=.7, rely=.02)


        # Contenedor Opciones de menu ----------------- 
        # Se agrega un frame por cada Item del Menu

        # Opcion 1
        # self.fm_opcion1=Frame(contenedor)
        # self.fm_opcion1.config(bg="#c7c7c7")
        # self.fm_opcion1.update()
        # self.fm_opcion1.bind("<Leave>", self.cerrarOpciones)

        # Opcion 2
        self.fm_opcion2=Frame(raiz)
        self.fm_opcion2.config(bg="#c7c7c7")
        self.fm_opcion2.update()
        self.fm_opcion2.bind("<Leave>", self.cerrarOpciones)

        # Opcion 3
        self.fm_opcion3=Frame(raiz)
        self.fm_opcion3.config(bg="#c7c7c7")
        self.fm_opcion3.update()
        self.fm_opcion3.bind("<Leave>", self.cerrarOpciones)


        # Orden de los Items
        self.item_1=BotonRGB_Grid(self.cBM, "Expandir", 0, 0, self.expandir) 
        self.item_2=BotonRGB_Grid(self.cBM, "Informacion", 0, 1, self.opcion_2) 
        self.item_3=BotonRGB_Grid(self.cBM, "Configuraciones", 0, 2, self.opcion_3) 

        # Opciones de los Items 

    
    def expandir(self):
        self.fm_opcion2.place(x=0, y=-10000)
        self.fm_opcion3.place(x=0, y=-10000)

        self.raiz.overrideredirect(True)
        self.raiz.state("zoomed")
        self.item_1=BotonRGB_Grid(self.cBM, "Reducir", 0, 0, self.reducir) 


    def reducir(self):
        self.fm_opcion2.place(x=0, y=-10000)
        self.fm_opcion3.place(x=0, y=-10000)

        self.raiz.overrideredirect(False)
        self.raiz.state("normal")
        self.objGui.center(self.raiz,1200,700)
        self.item_1=BotonRGB_Grid(self.cBM, "Expandir", 0, 0, self.expandir) 



    def opcion_2(self):
        self.fm_opcion3.place(x=0, y=-10000)
        self.fm_opcion2.place(x=0, y=0)

        x=.75
        y=.15
        self.fm_opcion2.place(relx=x, rely=y)

        if self.contador2==0:
            self.contador2=1
            bt1=Button(self.fm_opcion2, text="¿Como funciona?")
            bt1.config(bg="#c7c7c7", font=("Consolas", 10), relief="flat", command=self.msg1)
            bt1.grid(row=0, column=0, ipadx=20)

            bt2=Button(self.fm_opcion2, text="Desarrolladores" , command=self.msg2)
            bt2.config(bg="#c7c7c7", font=("Consolas", 10), relief="flat")
            bt2.grid(row=1, column=0, ipadx=20)

            bt3=Button(self.fm_opcion2, text="Version del programa", command=self.msg3)
            bt3.config(bg="#c7c7c7", font=("Consolas", 10), relief="flat")
            bt3.grid(row=2, column=0, ipadx=20)


            self.fm_opcion2.place(relx=x, rely=y)


    def msg1(self):
        VentanaEmergente("Como funciona", "ACEPTAR", "CONTINUAR", "Todos los datos \nAgredados, modificados,\n Eliminados, \nse ven reflejados al \nactualizar la tabla", lambda:print("Como Funciona"))

    def msg2(self):
        VentanaEmergente("DESARROLLADORES", "ACEPTAR", "CONTINUAR", "EFREN GALARZA\nErick Fernandez\nKaterine Cruz", lambda:print("Desarrolladores"))

    def msg3(self):
        VentanaEmergente("Version", "ACEPTAR", "CONTINUAR", "version 0.0.1", lambda:print("Version"))


    def opcion_3(self):
        self.fm_opcion2.place(x=0, y=-10000)
        self.fm_opcion3.place(x=0, y=0)

        x=.83
        y=.15
        self.fm_opcion3.place(relx=x, rely=y)



        if self.contador3==0:
            self.contador3=1
            
            bt1=Button(self.fm_opcion3, text="Cambiar a modo D/N", command=self.modeDark)
            bt1.config(bg="#c7c7c7", font=("Consolas", 10), relief="flat")
            bt1.grid(row=0, column=0, ipadx=20)


            
            # bt2=Button(self.fm_opcion3, text="Actualizar")
            # bt2.config(bg="#c7c7c7", font=("Consolas", 10), relief="flat")
            # bt2.grid(row=1, column=0, ipadx=20)

            bt3=Button(self.fm_opcion3, text="Cerrar Session", command=lambda:[self.raiz.destroy()])
            bt3.config(bg="#c7c7c7", font=("Consolas", 10), relief="flat")
            bt3.grid(row=2, column=0, ipadx=20)

            self.fm_opcion3.place(relx=x, rely=y)



    def modeDark(self):
        if self.contadorModo==0:
            self.contenedorTabla.config(bg="#000")
            self.contadorModo=1

        else:
            self.contenedorTabla.config(bg="#ffffff")
            self.contadorModo=0
            
        




    


    def cerrarOpciones(self, enter):
        # Desapecer Frame despues de sacar el mouse
        self.fm_opcion2.place(x=0, y=-10000)
        self.fm_opcion3.place(x=0, y=-10000)
        
        # Reiniciar contadores
        # self.contador1=0
        self.contador2=0
        self.contador3=0

    
    def saludar(self):
        print("Hola")
     



    

# root=Tk()
# root.geometry("600x600")
# fm=Frame(root)
# fm.pack()
# test=BarraMenu(root, )

# root.mainloop()
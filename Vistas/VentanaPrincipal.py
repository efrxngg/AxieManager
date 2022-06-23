from tkinter import *
from Procesos.ProcesosGui import *
from Figuras.setImage import *


from Vistas.BarraMenu import *
from Vistas.TablaMaestra import *



class VentanaPrincipal:
    def __init__(self):


        self.objGui=ProcesosGui()
        self.getWindows()
        self.getFrames()

        self.getLabels()
        self.getButtons()
        self.getBM()


        # -- Fin


# +-------------------------+
# +      Ventana Padre      +
# +-------------------------+

    def getWindows(self):
        self.ventanaPrincipal=Tk()
        # self.ventanaPrincipal.resizable(0, 0)
        self.ventanaPrincipal.title("Axie Manager")

        ruta="C:/Users/efren/Escritorio/Efren/Proyecto 2/logo.ico"
        self.ventanaPrincipal.iconbitmap(ruta)

        self.objGui.center(self.ventanaPrincipal, 1200, 700)


# +------------------------+
# +      Contenedores      +
# +------------------------+

    def getFrames(self):

        # +--------+
        # +  Head  +
        # +--------+
        self.fm1=Frame(self.ventanaPrincipal)
        self.fm1.config(bg="#000000")
        self.fm1.place(relx=0, rely=0, relwidth=1, relheight=.15)


        # # +-------------------------+
        # # +      Barra Lateral      +
        # # +-------------------------+
        self.fm2=Frame(self.ventanaPrincipal)
        self.fm2.config(bg="#0C3652")
        self.fm2.place(relx=0, rely=.15, relwidth=.1, relheight=1)


        # # +--------+
        # # +  Body  +
        # # +--------+
        self.fm3=Frame(self.ventanaPrincipal)
        self.fm3.config(bg="#ffffff")
        self.fm3.place(relx=.1, rely=.15, relwidth=.9, relheight=1)
        self.getTablaStandar()


# +-------------+
# +   Widgets   +
# +-------------+

    def getLabels(self):
        # Head
        # lb1_img=Label(self.fm1, image=self.img_logo, bg="#000")
        # lb1_img.place(relx=0.01, rely=0.03)
        # --------------Texto Logo---------------
        lb1_head=Label(self.fm1, text="Axie Manager")
        lb1_head.config(font=("Consolas", 20, "bold"), fg="#ffffff", bg="#000000")
        lb1_head.place(relx=.13, rely=.3)


        footer=Label(self.fm3, text="Todos los derechos reservados @copyright 2022")
        footer.config(fg="#fff", bg="#000")
        footer.place(y=638, relwidth=1, relheight=.02)


# +-------------+
# +   Botones   +
# +-------------+
    def getButtons(self):
        pass


    def getBM(self):
        BarraMenu(self.fm1, self.ventanaPrincipal, self.fm3)

    def getTablaStandar(self):
        x=TablaEstandar(self.fm3, "persona")

        

    







# if __name__=="__main__":
#     test=VentanaPrincipal()
#     ruta="Figuras\\Axie_Logo.png"
#     logo=setImage(test.ventanaPrincipal, ruta, .01, 0.03)
#     test.ventanaPrincipal.mainloop()







from Vistas.Login import *
from Vistas.VentanaPrincipal import *
from Figuras.setImage import *

class Inicio:
    def __init__(self):
        while 1:
            x=Login()
            if x.estado==1:
                # x=CrudRonin()
                # ls=x.getAllRonins("dataxie", "select * from ronin")
                # updt=UpdateInfoInv(ls)
                # print(updt.updateInvRonin())

                test=VentanaPrincipal()
                ruta="C:/Users/efren/Escritorio/Efren/Proyecto 2/Figuras/Axie_Logo.png"
                xd=setImage(test.ventanaPrincipal, ruta, .01, 0.03)
                test.ventanaPrincipal.mainloop()
                
            else:
                break
            


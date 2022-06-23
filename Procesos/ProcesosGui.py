from tkinter import *



class ProcesosGui:

    def center(self,obj,ancho, alto):
        alto_ven = alto
        ancho_ven = ancho
        ancho_panta = obj.winfo_screenwidth()
        alto_panta = obj.winfo_screenheight()
        x_coord = int((ancho_panta/2)-(ancho_ven/2))
        y_coord = int((alto_panta/2)-(alto_ven/2))
        obj.geometry("{}x{}+{}+{}".format(ancho_ven,alto_ven,x_coord,y_coord))


    def swapState(self, lista, estado):
        if estado==0:
            for i in lista:
                i.config(state="disabled")
        if estado==1:
            for i in lista:
                i.config(state="normal")
            


# root = Tk()
# objC=ProcesosGui()
# objC.center(root, 500, 200)
# root.mainloop()


class BotonRGB_Grid():

    def __init__(self, contenedor, texto, fila, columna, funcion=None):
        self.boton=Button(contenedor, text=texto, command=funcion)
        self.boton.config(fg="#ffffff",bg="#000000", relief="flat", font=("Consolas", 10, "bold"))
        self.boton.update()
        self.boton.grid(row=fila, column=columna, ipadx=25, ipady=25)
        self.boton.bind("<Enter>", self.dentro)
        self.boton.bind("<Leave>", self.fuera)

        
    def dentro(self, event):
        colores=[
        "#FD0303", 
        "#FB9018", 
        "#F5FB18", 
        "#52FB18", 
        "#18FB38", 
        "#18FBB0", 
        "#18F3FB",
        "#188BFB",
        "#181EFB",
        "#7318FB",
        "#B618FB",
        "#FB18BB"
        ]
        from random import randint
        self.boton.config(fg=colores[randint(0, (len(colores)-1))])

    def fuera(self, enter):
        self.boton.config(fg="#ffffff")









# x="b200"
# test= Cadenas()
# print(test.getStringNumber(x))





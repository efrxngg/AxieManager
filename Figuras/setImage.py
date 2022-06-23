from tkinter import *


class setImage():
    def __init__(self,contenedor, ruta, x, y):
        self.x=x
        self.y=y
        self.contenedor=contenedor
        self.ruta=ruta
        self.imageL()
        self.getLabel()

    def imageL(self):
        self.logo=PhotoImage(file=self.ruta).subsample(4)

    def getLabel(self):
        self.lb=Label(self.contenedor, image=self.logo)
        self.lb.config(bg="#000000")
        self.lb.place(relx=self.x, rely=self.y)
from tkinter import *


class ValidaDatosEntry:
    def __init__(self):
        pass
    # VALIDA TEXTO ------------------
    def validarStr(self, accion, caracter, texto):
        if accion !="1":
            return True
        return caracter.isalpha() and len(texto)<25


    def validarEdad(self, accion, caracter, texto):
        if accion !="1":
            return True
        return caracter.isnumeric() and len(texto)<2


    def validarContacto(self,accion,  texto):
        if accion !="1":
            return True
        return len(texto)<15


    def validarRonin(self, accion, texto):
        if accion !="1":
            return True
        return len(texto)<50




    def validarCedula(self, accion, car, texto):
        if accion !="1":
            return True

        return car in "1234567890" and len(texto)<10








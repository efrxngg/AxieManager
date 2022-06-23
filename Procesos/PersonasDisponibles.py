from Dao.CrudPersona import *
from Dao.CrudRonin import *


class PersonasDisponibles:
    def __init__(self):
        self.objCP=CrudPersona()
        self.objCR=CrudRonin()

    def getData(self):
        lista1=[]
        lp=self.objCP.getAllPersonas("dataxie", "select * from persona where estado='A'")
        for i in lp:
            lista1.append(i.cedula)
        lista2=[]
        lr=self.objCR.getAllRonins("dataxie", "select * from ronin")
        for i in lr:
            lista2.append(i.becado)
        lista=[]
        for i in lista1:
            if i not in lista2:
                lista.append(i)
        # print(lista)
        return lista





# test=PersonasDisponibles()
# test.getData()

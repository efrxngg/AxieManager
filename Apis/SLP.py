from Dominio.Entidades import *
from Dao.CrudRonin import *
import requests
import json

class UpdateInfoInv:
    def __init__(self, listaRonins):
        self.objCR=CrudRonin()
        self.listaRonins=listaRonins

    def updateInvRonin(self):
        for i in range(len(self.listaRonins)):
            slp=self.infoInv(self.listaRonins[i].ronin)
            id=self.listaRonins[i].id
            datos=(slp, id)

            print(datos)                
            print(self.objCR.updateInvRonin("dataxie", datos))

        return "El proceso ha finalizado"

    def infoInv(self, ronin):
        url="https://game-api.axie.technology/api/v1/"+ronin
        try:
            response=requests.get(url)
            info_inve=None
            if response.status_code==200:
                info=json.loads(response.text)
                info_inve=info["in_game_slp"]
        except:
            info_inve=0
            print("ronin no encontrada")
            
        return info_inve

    



# x=CrudRonin()
# ls=x.getAllRonins("dataxie", "select * from ronin")
# x=UpdateInfoInv(ls)
# print(x.updateInvRonin())


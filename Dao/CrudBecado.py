from Dao.Conexion import * 
from Dominio.Entidades import *

class CrudBecado:
    def __init__(self):
        self.con=Conexion()

    def getAllBecados(self, base, query)->list:
        """"Devuelve una lista con los requerimientos del query"""

        lista=[]
        cone=self.con.conectar(base)

        cursor1=cone.cursor()
        cursor1.execute(query)
        result=cursor1.fetchall()

        for i in range(len(result)):
            objB=Becado(
                        result[i][0],
                        result[i][1],
                        result[i][2],
                        result[i][3],
                        result[i][4]
                        )
            lista.append(objB)

        cone.close()
        return lista

# Insertar Becado ----------------------
# Inserta los datos del becado del dia ---

    def insertBecado(self, base, datos):
        """datos=(id_beca, id_persona, total_slp, copas, top)"""

        cone=self.con.conectar(base)
        cursor1=cone.cursor()
        query="insert into becado(id_beca, id_persona) values(%s, %s, %s, %s, %s)"
        cursor1.execute(query, datos)
        cone.commit()
        cone.close()
        return str(cursor1.rowcount)+" Registro[s] exitosos."

# Modificar Becado ---------------------------------
    def modifyBecado(self, base, datos):
        """datos=(id_beca new, id_becado new, id_beca de la beca asignada)"""

        cone=self.con.conectar(base)
        cursor1=cone.cursor()
        query="update becado set id_beca=%s, id_persona=%s where id_beca=%s"
        cursor1.execute(query, datos)
        cone.commit()
        cone.close()
        return str(cursor1.rowcount)+" Registro[s] exitosos."


# Eliminar Becado -----------------------------------------
    def deleteBecado(self, base, dato):
        """"dato=(id_beca,)"""
        cone=self.con.conectar(base)
        cursor1=cone.cursor()
        query="delete from becado where id_beca=%s"
        cursor1.execute(query, dato)
        cone.commit()
        cone.close()
        return str(cursor1.rowcount)+" Registro[s] exitosos."

        





# TEST ==========================================
# test=CrudBecado()
# x=test.getAllBecados("dataxie", "select * from becado")
# print(x[0].getData())


# datos=(1, "0954943114")
# try:
#     print(test.insertBecado("dataxie", datos))
# except:
#     print("Usurio Invalido")


# datos=(1, "0954943114", 1)
# print(test.modifyBecado("dataxie", datos))


# dato=(1,)
# print(test.deleteBecado("dataxie", dato))

        
from Dao.Conexion import *
from Dominio.Entidades import *


class CrudRonin:
    def __init__(self):
        self.con=Conexion()

# Muestra todas las Ronin "no sus stats"
    def getAllRonins(self, base, query):
        lista=[]
        cone=self.con.conectar(base)

        cursor1=cone.cursor()
        cursor1.execute(query)
        result=cursor1.fetchall()
        for i in range(len(result)):
            objB=Ronin(
                    result[i][0],
                    result[i][1],
                    result[i][2],
                    result[i][3],
                    result[i][4],
                    result[i][5]
                    )

            lista.append(objB)
        cone.close()
        return lista
# ------------------------- Modificaciones ------------------------------
# Insert Ronin -----------------------
    def insertRonin(self, base, dato):
        """dato=(Ronin, )"""
        
        cone=self.con.conectar(base)
        cursor1=cone.cursor()
        query="insert into ronin(ronin, porcentaje_becado) values(%s,%s)"
        cursor1.execute(query, dato)
        cone.commit()
        cone.close()

        return str(cursor1.rowcount)+" Registro[s] exitosos."

# Modificar ------------------------------------------------------

    def updateInvRonin(self, base, datos):
        """"Dato(Ronin Nueva, Identificador)"""

        cone=self.con.conectar(base)
        cursor1=cone.cursor()
        query="update ronin set total_slp=%s where id=%s"
        cursor1.execute(query, datos)
        cone.commit()
        cone.close()
        
        return str(cursor1.rowcount)+" Registro[s] exitosos."


    def modifyRonin(self, base, datos):
        """"Dato(Ronin Nueva, Identificador)"""

        cone=self.con.conectar(base)
        cursor1=cone.cursor()
        query="update ronin set ronin=%s, porcentaje_becado=%s where id=%s"
        cursor1.execute(query, datos)
        cone.commit()
        cone.close()

        return str(cursor1.rowcount)+" Registro[s] exitosos."

    def asignarBecado(self, base ,dato):
        cone=self.con.conectar(base)
        cursor1=cone.cursor()
        query="update ronin set becado=%s where id=%s"
        cursor1.execute(query, dato)
        cone.commit()
        cone.close()
        return str(cursor1.rowcount)+" Registro[s] exitosos."

    def removerBecado(self, base, datos):
        cone=self.con.conectar(base)
        cursor1=cone.cursor()
        query="update ronin set becado=Null where id=%s"
        cursor1.execute(query, datos)
        cone.commit()
        cone.close()
        return str(cursor1.rowcount)+" Registro[s] exitosos."


    def deleteRonin(self, base, dato):
        """Dato(id de la cuenta, )"""

        cone=self.con.conectar(base)
        cursor1=cone.cursor()
        query="delete from ronin where id=%s"
        cursor1.execute(query, dato)
        cone.commit()
        cone.close()

        return str(cursor1.rowcount)+" Registro[s] exitosos."

    def validarRonin(self, base, dato):
        """dato=(ronin, )"""
        objR=None
        cone=self.con.conectar(base)
        cursor1=cone.cursor()
        query="select * from ronin where ronin=%s"
        cursor1.execute(query, dato)
        result=cursor1.fetchall()
        cone.close()
        if len(result)>0:
            objR=Ronin(
                    result[0][0],
                    result[0][1],
                    result[0][2],
                    result[0][3],
                    result[0][4],
                    result[0][5]
                    )
        return objR

    def validarRoninBusqueda(self, base, dato):
        """dato=(ronin, )"""
        objR=None
        cone=self.con.conectar(base)
        cursor1=cone.cursor()
        query="select * from ronin where id=%s"
        cursor1.execute(query, dato)
        result=cursor1.fetchall()
        cone.close()
        if len(result)>0:
            objR=Ronin(
                    result[0][0],
                    result[0][1],
                    result[0][2],
                    result[0][3],
                    result[0][4],
                    result[0][5]
                    )
        return objR

    def infoTabla(self, base):
        lista=[]
        cone=self.con.conectar(base)
        cursor1=cone.cursor()
        querys=(
                "select count(*) from ronin",
                "select count(*) from ronin where becado is not null",
                "select count(*) from ronin where becado is null",
                "select sum(total_slp) from ronin",
                "select round(avg(porcentaje_becado), 2) from ronin where becado is not null"
                )

        for i in range(len(querys)):
            cursor1.execute(querys[i])
            result=cursor1.fetchall()
            lista.append(result)
        cone.close()
        return lista




# TEST====================================== Funcionamiento 4/4 
# Falta test de errores ---

# test=CrudRonin()
# x=test.infoTabla("dataxie")
# for i in range(5):
#     print(x[i][0][0])


# x=test.getAllRonin("dataxie", "select * from ronin")
# print(x[0].getData())


# dato=("ronin:FKHALDHFSAKLJFLSAKJFDLASKFASFKASLDF", )
# print(test.insertRonin("dataxie",dato))


# datos=("ronin:test", 2)
# print(test.modifyRonin("dataxie", datos))


# dato=(2,)
# print(test.deleteRonin("dataxie", dato))



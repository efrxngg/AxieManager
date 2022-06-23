from Dao.Conexion import * 
from Dominio.Entidades import *

class CrudPersona:
    def __init__(self):
        self.con=Conexion()

# --------------- Datos Generales de las personas -----------------
    def getAllPersonas(self, base, query):
        lista=[]
        cone=self.con.conectar(base)

        cursor1=cone.cursor()
        cursor1.execute(query)
        result=cursor1.fetchall() #Resultado de la consulta
        for i in range(len(result)):
            objU=Persona(
                result[i][0], 
                result[i][1], 
                result[i][2], 
                result[i][3], 
                result[i][4], 
                result[i][5], 
                result[i][6], 
                result[i][7],
                result[i][8],
                result[i][9]
                        )

            lista.append(objU)
        
        cone.close()
        return lista


# ------------------------- Modificaciones ------------------------------
#Insertar Persona -----------------------------------------------

    def insertPersona(self, base, datos):
        cone=self.con.conectar(base)
        cursor1=cone.cursor()
        sql="insert into persona(cedula, nombre, apellido, edad, nacionalidad, contacto, depo_ronin) values(%s, %s, %s, %s, %s, %s, %s)"
        cursor1.execute(sql, datos)
        cone.commit() #Afirmacion 
        cone.close()
        return str(cursor1.rowcount)+" Registro[s] exitosos."


# Modificar Persona------------------------------------------------
    def modificarPersona(self, base, datos):
        """datos= nombre, apellido, edad, nacionalidad, contacto, depo_ronin , cedula a modificar"""
        cone=self.con.conectar(base)
        cursor1=cone.cursor()

        query="update persona set nombre=%s, apellido=%s, edad=%s, nacionalidad=%s, contacto=%s, depo_ronin=%s where cedula=%s"
        cursor1.execute(query, datos)
        cone.commit()
        cone.close()
        return str(cursor1.rowcount)+" Registro[s] exitosos."


# Eliminar Persona------------------
    def cambiarEstadoPersona(self, base, datos):
        """datos=(estado=[Activo=A/Inactivo=I], cedula a modificar)"""
        cone=self.con.conectar(base)
        cursor1=cone.cursor()

        query="update persona set estado=%s, fecha_salida=current_timestamp() where cedula=%s"
        cursor1.execute(query, datos)
        cone.commit() 
        cone.close()
        return str(cursor1.rowcount)+" Registro[s] exitosos."



    # VALIDA QUE LA CEDULA NO ESTE REGISTRADA
    def validarCedula(self, base, dato) ->str:
        """dato=(cedula,)"""
        objP=None
        cone=self.con.conectar(base)
        cursor1=cone.cursor()
        query="select * from persona where cedula=%s"
        cursor1.execute(query, dato)
        result=cursor1.fetchall() #Resultado de la consulta
        cone.close()
        if len(result)>0:
            objP=Persona(
                result[0][0], 
                result[0][1], 
                result[0][2], 
                result[0][3], 
                result[0][4], 
                result[0][5], 
                result[0][6], 
                result[0][7],
                result[0][8],
                result[0][9]
                        )

        return objP
       
    
# test=CrudPersona()
# dato=("0000000001",)
# info=test.validarCedula("dataxie", dato)
# print(info.getData())


    def infoTabla(self, base):
        lista=[]
        cone=self.con.conectar(base)
        cursor1=cone.cursor()
        querys=(
                "select count(*) from persona",
                "select count(distinct nacionalidad) from persona where estado='A';",
                "select count(*) from persona where estado='A'",
                "select round(avg(edad),2) from persona where estado='A'",
                "select count(depo_ronin) from persona where estado='A'",
                "select count(*) from persona where estado='I'"

                )

        for i in range(len(querys)):
            cursor1.execute(querys[i])
            result=cursor1.fetchall()
            lista.append(result)
        cone.close()
        return lista




        
        



# TEST=============================================
# Lista usuarios----

# test=CrudPersona()
# x=test.getAllPersonas("dataxie", "select * from persona")
# print(x[0].getData())

# 1 ---
# datos=("0954943112", "Daniel", "Galarza", 16, "Ecuatoriana", "0997188086", "ronin:77e44a4d265c51751b2db841ea665c6e9bb4ec0b")
# print(test.insertPersona("dataxie", datos))

# 2 ---
# datos=("Patricio", "Galarza", "19", "Ecuatoriana", "@efrengg", "Null", "0954943114")
# print(test.modificarPersona("dataxie", datos))


# 3 ---
# dato=("I","0954943114")
# print(test.cambiarEstadoPersona("dataxie", dato))


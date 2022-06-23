from Dao.Conexion import * 
from Dominio.Entidades import *

class CrudUsuario:
    def __init__(self):
        self.con=Conexion()

    def validarUsuario(self, base, dato) ->str:
        """dato=(id_usuario,)"""
        objU=None
        cone=self.con.conectar(base)
        cursor1=cone.cursor()
        query="select * from usuario where id_usuario=%s"
        cursor1.execute(query, dato)
        result=cursor1.fetchall()
        cone.close()
        if len(result)>0:
            objU=Usuario(
                result[0][0],
                result[0][1],
                result[0][2],
                result[0][3],
                result[0][4],
                result[0][5],
                result[0][6]
                )
            print("Usuario Encontrado")
        else:
            print("Usuario No Encontrado")

        return objU



    def insertUsuario(self, base, datos):
        cone=self.con.conectar(base)
        cursor1=cone.cursor()
        query="insert into usuario(id_usuario, contraseña, nombre, apellido, cedula, correo) values (%s,%s,%s,%s,%s,%s)"
        cursor1.execute(query, datos)
        cone.commit()
        cone.close()
        return str(cursor1.rowcount)+" Registro[s] exitosos."
        
    


# test=CrudUsuario()
# datos=("ElPepe", "1234", "Pepe", "None", "000000003", "correo@none")
# print(test.insertUsuario("dataxie", datos))



# dato=("EfrxnGG",)
# x=test.validarUsuario("dataxie", dato)
# print(x.id_usuario)
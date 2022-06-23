import mysql.connector



class Conexion:
    def conectar(self, base):

        credenciales={
            "host":"localhost",
            "port":"3307",
            "user":"root",
            "password":"root1234",
            "database": base
        }

        try:
            cone=mysql.connector.connect(**credenciales)
        except:
            cone=None

        return cone


# test=Conexion()
# print(test.conectar("proyecto2"))
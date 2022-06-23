# Entidades
class Persona:
    def __init__(self, cedula, nombre, apellido, edad, nacionalidad, contacto, depo_ronin, fecha_ingreso=None, fecha_salida=None, estado=None):
        self.cedula=cedula
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.nacionalidad=nacionalidad
        self.depo_ronin=depo_ronin
        self.contacto=contacto
        self.fecha_ingreso=fecha_ingreso
        self.fecha_salida=fecha_salida
        self.estado=estado

    def getData(self):
        return (self.cedula, self.nombre, self.apellido, self.edad, self.nacionalidad, self.depo_ronin, self.contacto, self.fecha_ingreso, self.fecha_salida, self.estado)


        
class Ronin:
    def __init__(self, id, ronin, becado, total_slp, por_becado, fecha_ingreso):
        self.id=id
        self.ronin=ronin
        self.becado=becado
        self.total_slp=total_slp
        self.por_becado=por_becado
        self.fecha_ingreso=fecha_ingreso

    def getData(self):
        return (self.id, self.ronin, self.becado, self.total_slp, self.fecha_ingreso)


class Becado:
    def __init__(self, id_beca, id_persona, total_slp, copas, top):
        self.id_beca = id_beca
        self.id_persona=id_persona
        self.total_slp = total_slp
        self.copas = copas
        self.top = top

    def getData(self):
        return (self.id_beca, self.id_persona, self.total_slp, self.copas, self.top)
        



class Usuario:
    def __init__(self, id_usuario, contraseña, nombre, apellido, cedula, correo, fecha_ingreso):
        self.id_usuario=id_usuario 
        self.contraseña=contraseña
        self.nombre=nombre
        self.apellido=apellido
        self.cedula=cedula
        self.correo=correo
        self.fecha_ingreso=fecha_ingreso

        

        

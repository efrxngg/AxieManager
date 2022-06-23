from tkinter import *
from Procesos.ProcesosGui import *
from Procesos.validadorEntry import *
from Procesos.ventanaEmergente import *
from Dao.CrudUsuario import *

class RegistrarUsuario:
    def __init__(self):

        self.objCrudU=CrudUsuario()

        self.validador=ValidaDatosEntry()

        self.bg="#000"

        self.objGui=ProcesosGui()
        self.getWindows()
        self.getFrames()
        self.getLabels()
        self.getEntrys()
        self.getButtons()

    def getWindows(self):
        self.ven_register=Toplevel()
        self.ven_register.title("Registro Usuarios")
        ruta="C:/Users/efren/Escritorio/Efren/Proyecto 2/Figuras/favicon.ico"
        self.ven_register.iconbitmap(ruta)
        self.ven_register.config(relief="solid", bd=5, bg=self.bg)
        self.objGui.center(self.ven_register, 650, 450)
        self.ven_register.overrideredirect(1)

    def getFrames(self):
        self.contenedorPadre=Frame(self.ven_register)
        self.contenedorPadre.config(bg=self.bg)
        self.contenedorPadre.pack(pady=35)

        self.fm1=Frame(self.contenedorPadre)
        self.fm1.config(bg=self.bg)
        self.fm1.pack()

        self.fm2=Frame(self.contenedorPadre)
        self.fm2.config(bg=self.bg)
        self.fm2.pack(pady=10)

        self.fm3=Frame(self.contenedorPadre)
        self.fm3.config(bg=self.bg)
        self.fm3.pack()

    def getLabels(self):
        # TITULO
        Label(self.fm1, text="Datos del Usuario", bg=self.bg, fg="#fff", font=("Consolas", 20, "bold")).pack()

        # DATOS ---
        # USUARIO
        espacioy=10
        espaciox=10
        Label(self.fm2, text="Usuario", bg=self.bg, fg="#fff", font=("Consolas", 12,)).grid(row=0, column=0, sticky="e", padx=espaciox)
        # CONTRASEÑA
        Label(self.fm2, text="Contraseña", bg=self.bg, fg="#fff", font=("Consolas", 12,)).grid(row=1, column=0, sticky="e", pady=espacioy, padx=espaciox)

        # NOMBRE
        Label(self.fm2, text="Nombre", bg=self.bg, fg="#fff", font=("Consolas", 12,)).grid(row=2, column=0, sticky="e", padx=espaciox)

        # APELLIDO
        Label(self.fm2, text="Apellido", bg=self.bg, fg="#fff", font=("Consolas", 12,)).grid(row=3, column=0, sticky="e", pady=espacioy, padx=espaciox)

        # CEDULA
        Label(self.fm2, text="Cedula", bg=self.bg, fg="#fff", font=("Consolas", 12,)).grid(row=4, column=0, sticky="e", padx=espaciox)

        # CORREO
        Label(self.fm2, text="Correo", bg=self.bg, fg="#fff", font=("Consolas", 12,)).grid(row=5, column=0, sticky="e", pady=espacioy, padx=espaciox)


    def getEntrys(self):
        # USUARIO
        self.var_usuario=StringVar()
        var_vali1=self.fm2.register(self.validador.validarContacto)
        Entry(self.fm2, textvariable=self.var_usuario, relief="flat", width=25, font=("Consolas", 10), justify="center", validate="key", validatecommand=(var_vali1, "%d", "%s")).grid(row=0, column=1, ipady=5)
        # CONTRASEÑA
        self.var_contraseña=StringVar()
        var_vali1=self.fm2.register(self.validador.validarContacto)
        Entry(self.fm2, textvariable=self.var_contraseña, relief="flat", width=25, font=("Consolas", 10), justify="center", validate="key", validatecommand=(var_vali1, "%d", "%s")).grid(row=1, column=1, ipady=5)

        # NOMBRE
        self.var_nombre=StringVar()
        var_vali1=self.fm2.register(self.validador.validarStr)
        Entry(self.fm2, textvariable=self.var_nombre, relief="flat", width=25, font=("Consolas", 10), justify="center", validate="key", validatecommand=(var_vali1, "%d","%S", "%s")).grid(row=2, column=1, ipady=5)
        # APELLIDO
        self.var_apellido=StringVar()
        var_vali1=self.fm2.register(self.validador.validarStr)
        Entry(self.fm2, textvariable=self.var_apellido, relief="flat", width=25, font=("Consolas", 10), justify="center", validate="key", validatecommand=(var_vali1, "%d","%S", "%s")).grid(row=3, column=1, ipady=5)

        # CEDULA
        self.var_cedula=StringVar()
        var_vali1=self.fm2.register(self.validador.validarCedula)
        Entry(self.fm2, textvariable=self.var_cedula, relief="flat", width=25, font=("Consolas", 10), justify="center", validate="key", validatecommand=(var_vali1, "%d","%S", "%s")).grid(row=4, column=1, ipady=5)

        # CORREO
        self.var_correo=StringVar()
        var_vali1=self.fm2.register(self.validador.validarRonin)
        Entry(self.fm2, textvariable=self.var_correo, relief="flat", width=25, font=("Consolas", 10), justify="center", validate="key", validatecommand=(var_vali1, "%d", "%s")).grid(row=5, column=1, ipady=5)



    def getButtons(self):
        Button(self.fm3, text="Regresar ", font=("Consolas", 12,), command=lambda:self.ven_register.destroy()).grid(row=0, column=0)
        Button(self.fm3, text="Registrar", font=("Consolas", 12,), command=self.validarCampos).grid(row=0, column=1)


    def validarCampos(self):
        dato=(self.var_usuario.get(), )
        result=self.objCrudU.validarUsuario("dataxie", dato)
        msg=""

        if result!=None:
            msg+="Usuario Registrado\n"

        if len(self.var_usuario.get())<3:
            msg+="Usuario Invalido\n"
        if len(self.var_contraseña.get())<3:
            msg+="Contraseña Invalida\n"
        if len(self.var_nombre.get())<3:
            msg+="Nombre Invalido\n"
        if len(self.var_apellido.get())<3:
            msg+="Apellido Invalida\n"
        if len(self.var_cedula.get())<3:
            msg+="Cedula Invalida\n"
        if len(self.var_correo.get())<3:
            msg+="Correo Invalido\n"

        if msg=="":
            print("pasa")
            self.registrarUsuario()
            VentanaEmergente("Datos Registrados", "Volver", "Aceptar", "Todos sus datos\nHan sido registrados \nCorrectamente", lambda:self.ven_register.destroy() )

        else:
            VentanaEmergente("ERROR", "  VER  ", "EDITAR", msg, lambda:print("None"))



    def registrarUsuario(self):
        datos=(self.var_usuario.get(), self.var_contraseña.get(), self.var_nombre.get(), self.var_apellido.get(), self.var_cedula.get(), self.var_correo.get())
        print(datos)
        print(self.objCrudU.insertUsuario("dataxie", datos))



# root=Tk()
# RegistrarUsuario()
# root.mainloop()

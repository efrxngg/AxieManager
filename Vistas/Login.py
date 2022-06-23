from tkinter import *
from Procesos.ProcesosGui import *
from Procesos.validadorEntry import *
from Dao.CrudUsuario import *
from Vistas.RegistrarUsuario import *



class Login:
    def __init__(self):
        self.contador=0

        self.estado=0

        self.objCrudU=CrudUsuario()

        self.validador=ValidaDatosEntry()

        self.bg="#000"

        self.objGui=ProcesosGui()

        self.getWindows()
        self.getFrames()
        self.getLabels()
        self.getEntrys()
        self.getButtons()
        self.ventanaLogin.mainloop()

    def getWindows(self):
        self.ventanaLogin=Tk()
        self.ventanaLogin.title("Axie Manager")
        self.ventanaLogin.iconbitmap("C:/Users/efren/Escritorio/Efren/Proyecto 2/Figuras/favicon.ico")
        self.ventanaLogin.config(relief="flat", bg=self.bg)
        self.objGui.center(self.ventanaLogin, 600, 400)
        
    def getFrames(self):
        self.contenedorPadre=Frame(self.ventanaLogin)
        self.contenedorPadre.config(bg=self.bg)
        self.contenedorPadre.pack(pady=50)
        # TITULO
        self.fm1=Frame(self.contenedorPadre)
        self.fm1.config(bg=self.bg)
        self.fm1.pack(pady=20)

        # CENTRO
        self.fm2=Frame(self.contenedorPadre)
        self.fm2.config(bg=self.bg)
        self.fm2.pack()

        # BOTONES
        self.fm3=Frame(self.contenedorPadre)
        self.fm3.config(bg=self.bg)
        self.fm3.pack()


    def getLabels(self):
        Label(self.fm1, text="LOGIN AND REGISTER", bg="#fff", fg="#000", font=("Consolas", 20, "bold")).pack(pady=10)

        Label(self.fm2, text="Usuario", bg=self.bg, fg="#fff", font=("Consolas", 15, "bold")).grid(row=0, column=0, sticky="e")

        Label(self.fm2, text="Contraseña", bg=self.bg, fg="#fff", font=("Consolas", 15, "bold")).grid(row=2, column=0, sticky="e")



    def getEntrys(self):
        # MAXIMO 15 CRT
        vali_contra=self.fm2.register(self.validador.validarContacto)
        self.var_usuario=StringVar()
        Entry(self.fm2, 
        textvariable=self.var_usuario, 
        relief="flat", 
        width=25,
        justify="center", 
        font=("Consolas", 12),
        validate="key",
        validatecommand=(vali_contra, "%d", "%s")
        ).grid(row=0, column=1, ipady=4)

        self.var_contraseña=StringVar()
        Entry(self.fm2, 
            textvariable=self.var_contraseña, 
            relief="flat", 
            width=25, 
            justify="center", 
            font=("Consolas", 12),
            validate="key",
            validatecommand=(vali_contra, "%d", "%s"),
            show=" "

        ).grid(row=2, column=1, ipady=4 , pady=35)


    def getButtons(self):
        Button(self.fm3, 
            text="Registrarse",
            font=("Consolas", 12),
            command=self.register


        ).grid(row=0, column=0)

        Button(self.fm3, 
            text="Iniciar Session",
            font=("Consolas", 12),
            command=self.validarCamposLogin
        ).grid(row=0, column=1)

        Button(self.ventanaLogin, text="Clear", command=self.limpiar, bg="#000", fg="#fff", relief="flat").place(x=0, y=0)

    # FUNCIONES
    def limpiar(self):
        self.var_usuario.set("")
        self.var_contraseña.set("")

        
           


    # LOGIN 
    def validarCamposLogin(self):
        validador=0
        if len(self.var_usuario.get())<3:
            # msg+="Usuario invalido"
            Label(self.fm2, 
                text="x",
                bg="#ff0000",
                font=("Consolas", 10, "bold")

                ).grid(row=0, column=2, columnspan=2, ipady=5)

            validador+=1

        if len(self.var_contraseña.get())<3:
            Label(self.fm2, 
                text="x",
                bg="#ff0000",
                font=("Consolas", 10, "bold")

            ).grid(row=2, column=2, ipady=5)
            validador+=1

        if validador==0:
            print("Busqueda")
            dato=(self.var_usuario.get(),)
            result=self.objCrudU.validarUsuario("dataxie", dato)
            if result != None:
                Label(self.fm2, 
                        text=" ",
                        bg="#00ff00",
                        font=("Consolas", 10, "bold")

                        ).grid(row=0, column=2, ipady=5)

                print(result.nombre)
                if result.contraseña==self.var_contraseña.get():
                    print("Bienvenido")
                    self.estado=1
                    self.ventanaLogin.destroy()

                else:
                    Label(self.fm2, 
                        text="x",
                        bg="#ff0000",
                        font=("Consolas", 10, "bold")

                        ).grid(row=2, column=2, ipady=5)

            else:
                Label(self.fm2, 
                    text="x",
                    bg="#ff0000",
                    font=("Consolas", 10, "bold")

                    ).grid(row=0, column=2, columnspan=2, ipady=5)


    def register(self):
        RegistrarUsuario()



        








    # def callVentPrim(self):
    #     pass

# Login()


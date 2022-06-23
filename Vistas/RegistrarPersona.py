from tkinter import *
from Dao.CrudPersona import *
from Procesos.ProcesosGui import *
from Procesos.validadorEntry import *
from Procesos.ventanaEmergente import *


class InsertPersona:
    def __init__(self, lista):
        self.valida=ValidaDatosEntry()
        self.objCrudP=CrudPersona()
        self.vip=Toplevel()
        self.vip.config(relief="groove", bd=10)
        self.objGui=ProcesosGui()
        self.objGui.center(self.vip, 600, 400)
        self.vip.resizable(0,0)
        self.vip.config(bg="#DDE7C7")
        self.vip.overrideredirect(1)

        self.listaspm=lista
        self.objGui.swapState(self.listaspm, 0)

        self.getFrames()
        self.getLabels()
        self.getEntrys()
        self.getButton()

    def getFrames(self):
        self.cont_title=Frame(self.vip)
        self.cont_title.pack(pady=25)

        self.cont=Frame(self.vip)
        self.cont.pack()

        self.cont_bottons=Frame(self.vip)
        self.cont_bottons.pack()


    def getLabels(self):
        # Titulo
        Label(self.cont_title,
            text="REGISTRO USUARIOS",
            bg="#6F7464",
            font=("Consolas", 20, "bold")
            ).pack(side="top")


        # TEXTO
        tml=15
        Label(self.cont, text="Nombre: ", font=("Consolas", tml, "bold")).grid(row=0, column=0, sticky="e")
        Label(self.cont, text="Apellido: ", font=("Consolas", tml, "bold")).grid(row=1, column=0, sticky="e")
        Label(self.cont, text="Edad: ", font=("Consolas", tml, "bold")).grid(row=2, column=0, sticky="e")
        Label(self.cont, text="Nacionalidad: ", font=("Consolas", tml, "bold")).grid(row=3, column=0, sticky="e")
        Label(self.cont, text="Nro Cedula: ", font=("Consolas", tml, "bold")).grid(row=4, column=0, sticky="e")
        Label(self.cont, text="Contacto: ", font=("Consolas", tml, "bold")).grid(row=5, column=0, sticky="e")
        Label(self.cont, text="Cuenta de Ronin: ", font=("Consolas", tml, "bold")).grid(row=6, column=0, sticky="e")


    def getEntrys(self):
        tml=12

        # NOMBRE ---
        vali1=self.cont.register(self.valida.validarStr)
        self.var_nombre=StringVar()
        Entry(self.cont, 
            textvariable=self.var_nombre, 
            font=("Consolas", tml ),
            validate="key",
            validatecommand=(vali1, "%d", "%S", "%s")
        ).grid(row=0, column=1)


        # APELLIDO  ---
        vali2=self.cont.register(self.valida.validarStr)
        self.var_apellido=StringVar()
        Entry(self.cont, 
            textvariable=self.var_apellido, 
            font=("Consolas", tml ),
            validate="key",
            validatecommand=(vali2, "%d", "%S", "%s")
        
        ).grid(row=1, column=1)


        # EDAD  ---
        vali3=self.cont.register(self.valida.validarEdad)
        self.var_edad=StringVar()
        Entry(self.cont, 
            textvariable=self.var_edad, 
            font=("Consolas", tml ),
            validate="key",
            validatecommand=(vali3,"%d","%S","%s")

        ).grid(row=2, column=1)


        # NACIONALIDAD  ---
        vali4=self.cont.register(self.valida.validarStr)
        self.var_nacionalidad=StringVar()
        Entry(self.cont, 
            textvariable=self.var_nacionalidad, 
            font=("Consolas", tml ),
            validate="key",
            validatecommand=(vali4, "%d","%S", "%s")
            ).grid(row=3, column=1)


        # CEDULA    ---
        var_vali=self.cont.register(self.valida.validarCedula)
        self.var_cedula=StringVar()
        cedula=Entry(self.cont,
            textvariable=self.var_cedula,
            font=("Consolas", tml ),
            validate="key",
            validatecommand=(var_vali,"%d","%S","%s")
        )
        cedula.grid(row=4, column=1)


        # CONTACTO ---
        vali5=self.cont.register(self.valida.validarContacto)
        self.var_contacto=StringVar()
        Entry(self.cont, 
            textvariable=self.var_contacto, 
            font=("Consolas", tml ),
            validate="key",
            validatecommand=(vali5,"%d", "%s")

        ).grid(row=5, column=1)


        # RONIN ---
        vali6=self.cont.register(self.valida.validarRonin)
        self.var_depo_ronin=StringVar()
        Entry(self.cont, 
            textvariable=self.var_depo_ronin, 
            font=("Consolas", tml ),
            validate="key",
            validatecommand=(vali6,"%d", "%s")

        ).grid(row=6, column=1)


    def getButton(self):

        # Opciones----------
        self.objGui.swapState(self.listaspm, 0)
        self.option_1=Button(self.cont_bottons, text="Cerrar", command=lambda:[self.vip.destroy(), self.objGui.swapState(self.listaspm, 1)])
        self.option_1.grid(row=0, column=0)

        self.option_2=Button(self.cont_bottons, text="Agregar", command=lambda:[self.validarCampos()])
        # self.option_2.config(state="disabled")
        self.option_2.grid(row=0, column=1)



    def validarCampos(self):
        msg=""

        # Cedula ---
        cedula=(self.var_cedula.get(),)
        consultaCedula=self.objCrudP.validarCedula("dataxie", cedula)

        if (consultaCedula!=None):
            msg+=" Cedula Registrada\n"

        if len(self.var_cedula.get())==0:
            msg+=" Cedula Invalida\n"

        if len(self.var_nombre.get())<3:
            msg+=" Nombre Invalido\n"

        if len(self.var_apellido.get())<3:
            msg+=" Apellido Invalido\n"

        if len(self.var_edad.get())!=2:
            msg+=" edad Invalido\n"

        if len(self.var_nacionalidad.get())<3:
            msg+=" Nacionalidad Invalida\n"

        if len(self.var_contacto.get())<3:
            msg+=" Contacto Invalido\n"

        if len(self.var_depo_ronin.get())<6:
            msg+=" Ronin Invalida\n"

        if msg=="":
            print("Pasas")
            self.addPersona()
            self.vip.destroy()
        else:
            VentanaEmergente("DATOS ERRONEOS","Cancelar", "  Ver  ", msg, self.saludar)

        # INSTRUCCIONES CUANDO LA VALIDACION ES EXITOSA
        
    def saludar(self):
        pass



    def addPersona(self):
        datos=(self.var_cedula.get(), 
            self.var_nombre.get(), 
            self.var_apellido.get(), 
            self.var_edad.get(), 
            self.var_nacionalidad.get(), 
            self.var_contacto.get(), 
            self.var_depo_ronin.get()
            )
        # print(datos)
        self.objCrudP.insertPersona("dataxie", datos)
        self.objGui.swapState(self.listaspm, 1)




# root= Tk()
# lista=()
# test=InsertPersona(lista)

# root.mainloop()


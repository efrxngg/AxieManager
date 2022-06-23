from tkinter import *
from Dao.CrudRonin import *
from Procesos.ProcesosGui import *
from Procesos.validadorEntry import *



class RegistrarRonin:
    def __init__(self, lista):

        self.entrada=0
        self.validador=ValidaDatosEntry()
        self.objCR=CrudRonin()
        self.objGui=ProcesosGui()
        
        self.listapd=lista
        self.objGui.swapState(self.listapd, 0)

        self.getWindows()
        self.getFrames()
        self.getLabels()
        self.getEntrys()
        self.getButtons()

    def getWindows(self):
        self.vr=Toplevel()
        self.vr.config(bg="#000", relief="groove", bd=5)
        self.objGui.center(self.vr, 500, 160)
        self.vr.overrideredirect(1)

    def getFrames(self):
        # titulo ---
        self.titulo=Frame(self.vr)
        # self.titulo.config(bg="#fff")
        self.titulo.pack(pady=10)

        self.contenedorEntry=Frame(self.vr)
        # self.contenedorEntry.config(relief="groove", bd=3)
        self.contenedorEntry.pack(pady=10)

        self.botones=Frame(self.vr)
        self.botones.pack(pady=10)


    def getLabels(self):
        Label(self.titulo, text="Añadir Ronin", font=("Consolas", 20, "bold"), bg="#0C3652", fg="#fff").pack(side="left")

        Label(self.contenedorEntry, text="Ronin:", font=("Consolas", 15, "bold"), bg="#0C3652", fg="#fff").grid(row=0, column=0)

        Label(self.contenedorEntry, text="%", font=("Consolas", 15, "bold"), bg="#0C3652", fg="#fff").grid(row=0, column=2)


    def getEntrys(self):
        vali_ronin=self.contenedorEntry.register(self.validador.validarRonin)
        self.var_ronin=StringVar()

        self.ronin=Entry(self.contenedorEntry, 
            width=50, 
            textvariable=self.var_ronin,
            validate="key",
            validatecommand=(vali_ronin, "%d", "%s"),
            relief="flat",
            bg="#fff",
            selectbackground="#c7c7c7",
            selectforeground="#000",
            justify="center",
            font=("Consolas", 10)
            
            )
        self.var_ronin.set("Ingresar Ronin")
        self.ronin.bind("<Enter>", self.limpiarEntry)
        self.ronin.grid(row=0, column=1, ipady=5)

        # PORCENTAJE BECADO
        vali_por_beca=self.contenedorEntry.register(self.validador.validarEdad)
        self.var_por=StringVar()
        Entry(self.contenedorEntry, 
            textvariable=self.var_por,
            validate="key",
            validatecommand=(vali_por_beca,"%d","%S","%s"),
            relief="flat",
            bg="#fff",
            selectbackground="#c7c7c7",
            selectforeground="#000",
            justify="center",
            font=("Consolas", 10),
            width=4
            ).grid(row=0, column=4)

        self.var_por.set(0)

    def limpiarEntry(self, event):
        if self.entrada==0:
            self.entrada=1
            self.ronin.delete(0, "end")

        


    def getButtons(self):
        Button(self.botones, text="Cancelar", command=lambda:[self.vr.destroy(), self.objGui.swapState(self.listapd, 1)], bg="#fff").grid(row=0, column=0)
        Button(self.botones, text="Registrar", command=lambda:[self.validarCampo()], bg="#fff").grid(row=0, column=1)
    
    def validarCampo(self):
        ronin=self.var_ronin.get()
        if len(ronin)>6 and ronin!="Ingresar Ronin":
            dato=(ronin,)
            result=self.objCR.validarRonin("dataxie", dato)
            if result is None:
                print("LISTO")
                datoadd=(ronin, self.var_por.get())
                print(self.objCR.insertRonin("dataxie", datoadd))
                self.vr.destroy()
                self.objGui.swapState(self.listapd, 1)

            else:
                Label(self.vr, text="Ronin Invalida").place(x=0, y=0)
        else:
            Label(self.vr, text="Ronin Invalida").place(x=0, y=0)





# root=Tk()
# lista=[]
# test=RegistrarRonin(lista)

# root.mainloop()
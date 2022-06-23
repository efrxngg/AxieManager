from Dominio.Entidades import *
from Procesos.ProcesosGui import *

from Dao.CrudPersona import *
from Dao.CrudRonin import *
from Dao.CrudBecado import *

from Procesos.validadorEntry import *
from Procesos.ventanaEmergente import *
from Vistas.RegistrarPersona import *
from Procesos.PersonasDisponibles import *
from Vistas.RegistrarRonin import *

# UPDATE INVE RONIN SLP 
from Apis.SLP import *

import pyperclip as pc
from tkinter import *
from tkinter import ttk



class TablaEstandar:
    def __init__(self, contenedor, tp):
        # DEFINIDOR TIPO TABLA
        self.tipoTabla=None

        # VALIDADOR ENTRYS
        self.validador=ValidaDatosEntry()

        self.contenedor=contenedor
        # PROCESOS GUI
        self.objGui=ProcesosGui()
        

        # LISTA PERSONAS ---
        self.objCP=CrudPersona()
        self.listaRegistrosPersona=self.objCP.getAllPersonas("dataxie", "select * from persona where estado='A'")
        
        # LISTA RONIN ----
        self.objCR=CrudRonin()
        self.listaRegistrosRonin=self.objCR.getAllRonins("dataxie", "select * from ronin")
        # TEST ---
        


        # LISTA BECADO --- PENDIENTE API
        # self.objBecado=CrudBecado()
        # self.listaRegistrosBecado=self.objBecado.getAllBecados("dataxie", "select * from becado")
        self.getFrames()

        # TEST --- TABLA INICIO
        if tp=="persona":
            self.tablaPersona()
        elif tp=="ronin":
            self.tablaRonin()
        
    def getFrames(self):
        self.contenedorPrincipal=Frame(self.contenedor)
        self.contenedorPrincipal.config(bg="#000")
        self.contenedorPrincipal.pack(pady=25, anchor=CENTER)
  

        self.fm_Details=Frame(self.contenedorPrincipal, width=1000, height=400)
        self.fm_Details.grid_propagate(0)
        self.fm_Details.pack_propagate(0)
        self.fm_Details.config(bg="#000")
        self.fm_Details.grid(row=0,column=0, columnspan=2)

        # RELLENO
        

        # FM DETAILS: BARRA LATERAL IZQ
        self.DetailsLeft=Frame(self.fm_Details)
        self.DetailsLeft.config(bg="#fff")
        self.DetailsLeft.place(relx=0, rely=.2)
        self.details_left()
        
        # FM DETAILS: BARRA LATERAL DER
        self.DetailsRight=Frame(self.fm_Details)
        self.DetailsRight.config(bg="#000")
        self.DetailsRight.place(relx=.88, rely=.2)
        

        # FM DETAILS: PARTE BAJA ---
        self.DetailsBottom=Frame(self.fm_Details)
        self.DetailsBottom.config(bg="#000")
        self.DetailsBottom.place(relx=0, rely=.91, relwidth=1, relheight=.1)
        self.details_bottom()
    

    # FM DETAILS: BARRA LATERAL IZQ ---
    def details_left(self):
        self.br=BotonRGB_Grid(self.DetailsLeft, "   REFRESH", 0, 0, self.reload)
        self.bp=BotonRGB_Grid(self.DetailsLeft, "ADD PERSON", 1, 0, self.registrarPersona)
        self.bron=BotonRGB_Grid(self.DetailsLeft, " ADD RONIN", 2, 0, self.registrarRonin)


    def registrarRonin(self): 
        lista=(self.br.boton, self.bp.boton)
        RegistrarRonin(lista)
        

        

    def cambiarEstadoADD(self):
        self.botonAgregar=0



    def reload(self):
        self.contenedorPrincipal.pack_forget()
        self.contenedorPrincipal.destroy()
        TablaEstandar(self.contenedor, self.tipoTabla)
        
        

    # FM DETAILS: BARRA LATERAL DER ---
    def details_right(self):
        if self.tipoTabla=="persona":
            self.ep=BotonRGB_Grid(self.DetailsRight, "VALIDAR", 0, 0, self.validarCambiosPersona)
            self.ep=BotonRGB_Grid(self.DetailsRight, "CAMBIAR \nESTADO", 1, 0, self.confModificacion)

            
        
        elif self.tipoTabla=="ronin":
            self.er=BotonRGB_Grid(self.DetailsRight, "EDITARR", 0, 0, self.confGuardadoR)
            self.er=BotonRGB_Grid(self.DetailsRight, "UPDATE DTS", 1, 0, self.confUpdateInvRonin)
            self.er=BotonRGB_Grid(self.DetailsRight, "DELETE", 2, 0, self.confDelete)        

    def confUpdateInvRonin(self):
        VentanaEmergente("Aviso", "Cancelar", "Aceptar", "Los datos actualizados \n se veran reflejados\nal actualizar la tabla", self.updateIR)

    def updateIR(self):
        dato=(self.var_id,)
        obj=self.objCR.validarRoninBusqueda("dataxie", dato)
        ls=[]
        ls.append(obj)
        x=UpdateInfoInv(ls)
        print(x.updateInvRonin())

        


    # FM DETAILS: PARTE BAJA ---
    def details_bottom(self):
        # BOTONES DE SELECCIONDE TABLA ---
        # CONTENEDOR BOTONES
        fm1=Frame(self.DetailsBottom)
        fm1.pack(side="left", anchor="s")
        Button(fm1, text="Tabla Personas", command=lambda:[self.tablaPersona(), self.reload()]).grid(row=0, column=0)
        Button(fm1, text="Tabla Ronin", command=lambda:[self.tablaRonin(), self.reload()]).grid(row=0, column=1)
        # Button(fm1, text="Tabla Becado", command=self.tablaBecado).grid(row=0, column=2)

        # BUSCADOR --- 
        # CONTENEDOR BUSCADOR ---
        fm2=Frame(self.DetailsBottom)
        fm2.pack(side="right")

        # ENTRY BUSCAR ---
        vali=fm2.register(self.validador.validarCedula)
        self.var_buscar=StringVar()
        self.buscar=Entry(fm2,
            textvariable=self.var_buscar,
            validate="key",
            validatecommand=(vali,"%d","%S","%s"),
            justify=CENTER,
            relief="flat"
            )
        self.buscar.grid(row=0, column=0)

        # BOTON BUSCAR ----
        Button(fm2, 
            text="Buscar",
            command=lambda:self.Search()
        ).grid(row=0, column=1)




    # SELECCIONAR TABLA
    def tablaPersona(self):
        self.tipoTabla="persona"
        # INFORMACION GENERAL PERSONA ---
        self.infoGeneralPersona()
        self.lc=("CEDULA", "NOMBRE", "DEPO RONIN", "CONTACTO", "NACIONALIDAD")
        self.showTabla(self.lc, self.listaRegistrosPersona, "persona")

    def tablaRonin(self):
        self.tipoTabla="ronin"
        # INFORMACION GENERAL RONIN ---
        self.infoGeneralRonin()
        self.lc=("ID", "RONIN", "BECADO", "SLP", "PORCENTAJE BECA")
        self.showTabla(self.lc, self.listaRegistrosRonin, "ronin")

    def tablaBecado(self):
        self.tipoTabla="becado"
        # INFORMACION GENERAL BECADO ---
        self.infoGeneralBecado()
        self.lc=("ID BECA", "ID PERSONA", "TOTAL SLP", "COPAS", "TOP")
        self.showTabla(self.lc, self.listaRegistrosBecado, "becado")

    # BUSCADOR ---
    def Search(self):
        if self.tipoTabla=="persona":
            dato=(self.var_buscar.get(),)
            # print(dato)
            obj=self.objCP.validarCedula("dataxie", dato)
            self.lista=[]
            if obj!=None:
                self.lista.append(obj)
                self.showTabla(self.lc, self.lista, self.tipoTabla)
                self.buscar.delete(0, "end")
            else:
                print("Nada")
                self.tablaPersona()


        elif self.tipoTabla=="ronin":
            dato=(self.var_buscar.get(),)
            obj=self.objCR.validarRoninBusqueda("dataxie", dato)
            lista=[]
            if obj!=None:
                lista.append(obj)
                self.showTabla(self.lc, lista, self.tipoTabla)
                self.buscar.delete(0, "end")
            else:
                self.tablaRonin()


        

    # Informacion General Tablas
    def infoGeneralPersona(self):
        fm=Frame(self.fm_Details)
        fm.config(bg="#f0f0f0")
        fm.place(x=140, y=50, width=750 , height=300)

        Label(fm, 
        text="INFORMACION GENERAL PERSONAS",
        font=("Consolas", 20, "bold"),
        fg="#000"
        ).pack(pady=10)

        # Fila 1
        fm1=Frame(fm)
        ancho=200
        alto=60
        x1=65
        y1=85
        bg_fms="#000"
        fm1.config(bg=bg_fms)
        fm1.place(x=x1, y=y1, width=ancho , height=alto)
        # Texto ---
        Label(fm1, text="Cant Personas Registradas:",
            bg=bg_fms, 
            fg="#C9C9C9", 
            font=("Consolas", 10),
        ).pack()
        # Info  ---
        lista=self.objCP.infoTabla("dataxie")
        Label(fm1, text=lista[0][0][0],
            bg=bg_fms, 
            fg="#fff", 
            font=("Consolas", 10, "bold"),
            justify="center"
        ).pack()

        fm2=Frame(fm)
        fm2.config(bg="#000")
        fm2.place(x=x1+210, y=y1, width=ancho , height=alto)

        Label(fm2, text="Cant Nacionalidades:",
            bg=bg_fms, 
            fg="#C9C9C9", 
            font=("Consolas", 10)
        ).pack()
        # Info  ---
        Label(fm2, text=lista[1][0][0],
            bg=bg_fms, 
            fg="#fff", 
            font=("Consolas", 10, "bold"),
            justify="center"
        ).pack()


        fm3=Frame(fm)
        fm3.config(bg="#000")
        fm3.place(x=x1+420, y=y1, width=ancho , height=alto)

        Label(fm3, text="Cant Personas Activas:",
            bg=bg_fms, 
            fg="#C9C9C9", 
            font=("Consolas", 10)
        ).pack()
        # Info  ---
        Label(fm3, text=lista[2][0][0],
            bg=bg_fms, 
            fg="#fff", 
            font=("Consolas", 10, "bold"),
            justify="center"
        ).pack()

        # Fila 2
        fm4=Frame(fm)
        ancho2=200
        alto=60
        x1=65
        y2=y1*2
        bgfm2="#000"
        fm4.config(bg=bgfm2)
        fm4.place(x=x1, y=y2, width=ancho2 , height=alto)
        # Texto ---
        Label(fm4, text="Edad Promedio:",
            bg=bgfm2, 
            fg="#C9C9C9", 
            font=("Consolas", 10)
        ).pack()
        # Info  ---
        Label(fm4, text=lista[3][0][0],
            bg=bgfm2, 
            fg="#fff", 
            font=("Consolas", 10, "bold"),
            justify="center"
        ).pack()

        fm5=Frame(fm)
        fm5.config(bg="#000")
        fm5.place(x=x1+210, y=y2, width=ancho2 , height=alto)

        Label(fm5, text="Cant Ronin Depo",
            bg=bgfm2, 
            fg="#C9C9C9", 
            font=("Consolas", 10)
        ).pack()
        # Info  ---
        Label(fm5, text=lista[4][0][0],
            bg=bgfm2, 
            fg="#fff", 
            font=("Consolas", 10, "bold"),
            justify="center"
        ).pack()


        fm6=Frame(fm)
        fm6.config(bg="#000")
        fm6.place(x=x1+420, y=y2, width=ancho2 , height=alto)

        Label(fm6, text="Cant Personas Inactivas:",
            bg=bgfm2, 
            fg="#C9C9C9", 
            font=("Consolas", 10)
        ).pack()
        # Info  ---
        Label(fm6, text=lista[5][0][0],
            bg=bgfm2, 
            fg="#fff", 
            font=("Consolas", 10, "bold"),
            justify="center"
        ).pack()

        Label(fm, 
        text="by Efrxn",
        font=("Consolas", 10, "bold"),
        fg="#000"
        ).pack(side="bottom")

    def infoGeneralRonin(self):
        
        datos=self.objCR.infoTabla("dataxie")
        lista=[]
        if len(datos)>0:
            if datos[4][0][0]==None:
                lista.append(0)
            else:
                lista.append(datos[4][0][0])

                


        fm=Frame(self.fm_Details)
        fm.config(bg="#fff")
        fm.place(x=140, y=50, width=750 , height=300)

        Label(fm, 
        text="INFORMACION GENERAL RONINS",
        font=("Consolas", 20, "bold"),
        fg="#000"
        ).pack(pady=10)

        # Fila 1
        fm1=Frame(fm)
        ancho=200
        alto=60
        x1=65
        y1=85
        bg_fms="#000"
        fm1.config(bg=bg_fms)
        fm1.place(x=x1, y=y1, width=ancho , height=alto)
        # Texto ---
        Label(fm1, text="Cant de Ronins Registradas:",
            bg=bg_fms, 
            fg="#C9C9C9", 
            font=("Consolas", 10),
        ).pack()
        # Info  ---
        Label(fm1, text=datos[0][0][0],
            bg=bg_fms, 
            fg="#fff", 
            font=("Consolas", 10, "bold"),
            justify="center"
        ).pack()

        fm2=Frame(fm)
        fm2.config(bg="#000")
        fm2.place(x=x1+210, y=y1, width=ancho , height=alto)

        Label(fm2, text="Cant de Cuentas en Uso:",
            bg=bg_fms, 
            fg="#C9C9C9", 
            font=("Consolas", 10)
        ).pack()
        # Info  ---
        Label(fm2, text=datos[1][0][0],
            bg=bg_fms, 
            fg="#fff", 
            font=("Consolas", 10, "bold"),
            justify="center"
        ).pack()


        fm3=Frame(fm)
        fm3.config(bg="#000")
        fm3.place(x=x1+420, y=y1, width=ancho , height=alto)

        Label(fm3, text="Cant de Cuentas Sin Uso:",
            bg=bg_fms, 
            fg="#C9C9C9", 
            font=("Consolas", 10)
        ).pack()
        # Info  ---
        Label(fm3, text=datos[2][0][0],
            bg=bg_fms, 
            fg="#fff", 
            font=("Consolas", 10, "bold"),
            justify="center"
        ).pack()

        # Fila 2
        fm4=Frame(fm)
        ancho2=200
        alto=60
        x1=65
        y2=y1*2
        bgfm2="#000"
        fm4.config(bg=bgfm2)
        fm4.place(x=x1, y=y2, width=ancho2 , height=alto)
        # Texto ---
        Label(fm4, text="SLP Total:",
            bg=bgfm2, 
            fg="#C9C9C9", 
            font=("Consolas", 10)
        ).pack()
        # Info  ---
        Label(fm4, text=datos[3][0][0],
            bg=bgfm2, 
            fg="#fff", 
            font=("Consolas", 10, "bold"),
            justify="center"
        ).pack()

        fm5=Frame(fm)
        fm5.config(bg="#000")
        fm5.place(x=x1+210, y=y2, width=ancho2 , height=alto)

        Label(fm5, text=f"{100-float(lista[0])}% Manager",
            bg=bgfm2, 
            fg="#C9C9C9", 
            font=("Consolas", 10)
        ).pack()
        # Info  ---
        pm=int(datos[3][0][0])*(100-float(lista[0]))/100

        Label(fm5, text=pm,
            bg=bgfm2, 
            fg="#fff", 
            font=("Consolas", 10, "bold"),
            justify="center"
        ).pack()


        fm6=Frame(fm)
        fm6.config(bg="#000")
        fm6.place(x=x1+420, y=y2, width=ancho2 , height=alto)

        Label(fm6, text=f"{float(lista[0])}% Becados",
            bg=bgfm2, 
            fg="#C9C9C9", 
            font=("Consolas", 10)
        ).pack()
        # Info  ---
        pb=int(datos[3][0][0])*(float(lista[0])/100)
        Label(fm6, text=pb,
            bg=bgfm2, 
            fg="#fff", 
            font=("Consolas", 10, "bold"),
            justify="center"
        ).pack()

        # CREDITOS  ---
        Label(fm, 
        text="by Efrxn",
        font=("Consolas", 10, "bold"),
        fg="#000"
        ).pack(side="bottom")

        


    def infoGeneralBecado(self):
        fm=Frame(self.fm_Details)
        fm.config(bg="#bff")
        fm.place(x=140, y=50, width=750 , height=300)


    def showTabla(self, ListaCampos, ListaRegistros, tipoTabla):
        listaCampos=ListaCampos
        self.listaRegistros=ListaRegistros
        self.tipoTabla=tipoTabla
        

        listaNC=[]
        for i in range(len(listaCampos)):
            nc=int(i+1)
            listaNC.append(nc)
        columns=tuple(listaNC)
        # print(columns)

        self.tabla=ttk.Treeview(
            self.contenedorPrincipal,
            columns=columns,
            show="headings",
            height=8
            )
        
        self.tabla.bind("<Double-Button-1>", self.onDoubleClick)

        barraDesplazamiento=Scrollbar(self.contenedorPrincipal,
                                    command=self.tabla.yview
                                     )

        # ESTILOS--------------------------------------
        estilo=ttk.Style()
        # Tipos: default - alt - vista - clam
        estilo.theme_use("clam")

        # Estilos de los Campos
        estilo.configure(
                        "Treeview.Heading",
                        background="#000",
                        relief="flat",
                        foreground="#fff", #Letas Botones
                        rowheight=45,
                        fielbackground="silver"

                        )

        # Estilo registros por defecto
        estilo.configure("Treeview", background="#fff")

        # Estilos de los registros seleccionados
        estilo.map('Treeview', background=[('selected', '#c7c7c7')])



        # Campos -----------------------------------------
        for i in range(len(listaCampos)):
            self.tabla.heading(i+1, text=listaCampos[i])

        for i in range(len(listaCampos)):
            self.tabla.column(i+1, anchor=CENTER)


    # ------------- Seleccion de tabla -------------
        if self.tipoTabla=="persona":
            # ----------------- Tabla ------------------------
            for indice in range(len(self.listaRegistros)):
                self.tabla.insert("", "end",
                    values=(
                            self.listaRegistros[indice].cedula,
                            self.listaRegistros[indice].nombre+" "+self.listaRegistros[indice].apellido,
                            self.listaRegistros[indice].depo_ronin,
                            self.listaRegistros[indice].contacto,
                            self.listaRegistros[indice].nacionalidad
                            )
                                 )
        elif self.tipoTabla=="ronin":

            # ----------------- Tabla ------------------------
            for indice in range(len(self.listaRegistros)):
                self.tabla.insert("", "end",
                    values=(
                            self.listaRegistros[indice].id,
                            self.listaRegistros[indice].ronin,
                            self.listaRegistros[indice].becado,
                            self.listaRegistros[indice].total_slp,
                            self.listaRegistros[indice].por_becado
                            )
                                    )
            # ----------------- Tabla ------------------------

        elif self.tipoTabla=="becado":
            for indice in range(len(self.listaRegistros)):
                self.tabla.insert("", "end",
                    values=(
                            self.listaRegistros[indice].id_beca,
                            self.listaRegistros[indice].id_persona,
                            self.listaRegistros[indice].total_slp,
                            self.listaRegistros[indice].copas,
                            self.listaRegistros[indice].top
                            )

                                    )
        self.tabla.config(yscrollcommand=barraDesplazamiento.set)


        # POSICIONAMIENTO TABLA AND BARRA DESPLAZAMIENTO
        self.tabla.grid(row=1, column=0)
        barraDesplazamiento.grid(row=1, column=1, sticky="nsew")


    def onDoubleClick(self, event):
        item = event.widget.identify("item",event.x,event.y)
        print(item)
        posicion=self.tabla.index(item)
        print("Datos del usuario", self.listaRegistros[posicion].getData())
        self.selectTabla(posicion)
        self.posicion=posicion


    # PENDIENTE ---------
    def selectTabla(self, posicion):
        if self.tipoTabla=="persona":
            self.details_right()
            self.editarPersona(posicion)

        if self.tipoTabla=="ronin":
            self.details_right()
            self.editarRonin(posicion)



# STAR PERSONA ========================================================
    def editarPersona(self, posicion):
        self.getFramesPersona()
        self.getLabelsPersona()
        self.getEntryPersonas(posicion)
        self.getButtonsPersona()

    def getFramesPersona(self):
        # Contenedor Base ----
        self.fm=Frame(self.fm_Details)
        self.fm.config(bg="#fff")
        self.fm.place(x=140, y=50, width=750 , height=300)

        # Contenedor Titulo Persona
        self.t_p=Frame(self.fm)
        self.t_p.pack(pady=10)

        # CONTENEDOR INFO PERSONA ---
        # Color de fondo Label and Contenedor
        self.bgCP="#668788"
        # Color de fondo Entrys
        self.bgEP="#fff"
        self.espacio_y=16
        self.cont=Frame(self.fm, width=750, height=370)
        self.cont.config(bg=self.bgCP)
        self.cont.grid_propagate(0)
        self.cont.pack()


    def getLabelsPersona(self):
        # Label Titulo
        Label(self.t_p, text="DATOS DE LA PERSONA", bg="#000", fg="#fff", font=("Consolas", 20, "bold")).pack()

        # Labels Info
        Label(self.cont, text="Nombre: ", font=("Consolas", 10, "bold"), bg=self.bgCP).grid(row=0, column=0, sticky="e", pady=self.espacio_y)
        Label(self.cont, text="Apellido: ", font=("Consolas", 10, "bold"), bg=self.bgCP).grid(row=0, column=2, sticky="e")
        Label(self.cont, text="Cedula: ", font=("Consolas", 10, "bold"), bg=self.bgCP).grid(row=0, column=4, sticky="e", pady=self.espacio_y)
        Label(self.cont, text="Nacionalidad: ", font=("Consolas", 10, "bold"), bg=self.bgCP).grid(row=1, column=2, sticky="e")
        Label(self.cont, text="Contacto: ", font=("Consolas", 10, "bold"), bg=self.bgCP).grid(row=1, column=0, sticky="e", pady=self.espacio_y)
        Label(self.cont, text="Edad: ", font=("Consolas", 10, "bold"), bg=self.bgCP).grid(row=2, column=0, sticky="e")
        Label(self.cont, text="Fecha Ingreso: ", font=("Consolas", 10, "bold"), bg=self.bgCP).grid(row=1, column=4, sticky="e", pady=self.espacio_y)
        Label(self.cont, text="Fecha Salida: ", font=("Consolas", 10, "bold"), bg=self.bgCP).grid(row=2, column=4, sticky="e")
        Label(self.cont, text="Estado: ", font=("Consolas", 10, "bold"), bg=self.bgCP).grid(row=2, column=2, sticky="e", pady=self.espacio_y)
        Label(self.cont, text="Depo Ronin: ", font=("Consolas", 10, "bold"), bg=self.bgCP).grid(row=3, column=0, sticky="e", pady=20)
        
        

    def getEntryPersonas(self, posicion):
        # VALIDADOR ---
        instancia=ValidaDatosEntry()


        # NOMBRE ---
        self.validate1=self.cont.register(instancia.validarStr)
        self.var_Nombre=StringVar()
        self.dt_Nombre=Entry(self.cont,
                                textvariable=self.var_Nombre,
                                justify="center",
                                validate="key",
                                validatecommand=(self.validate1,"%d","%S","%s")
                                )
        self.var_Nombre.set(self.listaRegistros[posicion].nombre)
        self.dt_Nombre.config(bg=self.bgEP, font=("Consolas", 10))
        self.dt_Nombre.grid(row=0, column=1, ipady=5)


        # APELLIDO ---
        self.validate2=self.cont.register(instancia.validarStr)
        self.var_apellido=StringVar()
        self.dt_apellido=Entry(self.cont,
                                textvariable=self.var_apellido,
                                validate="key",
                                validatecommand=(self.validate2,"%d","%S","%s"),
                                justify="center"
                                )
        self.var_apellido.set(self.listaRegistros[posicion].apellido)
        self.dt_apellido.config(bg=self.bgEP, font=("Consolas", 10))
        self.dt_apellido.grid(row=0, column=3, ipady=5)

        # CEDULA ---
        self.validate3=self.cont.register(instancia.validarCedula)
        self.var_cedula=StringVar()
        self.dt_Cedula=Entry(self.cont, 
                                textvariable=self.var_cedula,
                                validate="key",
                                validatecommand=(self.validate3,"%d","%S","%s"),
                                justify="center"
                                
                                )
        self.var_cedula.set(self.listaRegistros[posicion].cedula)
        self.stateEntry(self.dt_Cedula, 0)
        self.dt_Cedula.config(bg=self.bgEP, font=("Consolas", 10))
        self.dt_Cedula.grid(row=0, column=5, ipady=5)


        # NACIONALIDAD ---
        vali_naci=self.cont.register(self.validador.validarStr)
        self.var_nacionalidad=StringVar()
        self.dt_nacionalidad=Entry(self.cont,
                                textvariable=self.var_nacionalidad,
                                justify="center",
                                validate="key",
                                validatecommand=(vali_naci, "%d", "%S", "%s")
                                )
        self.var_nacionalidad.set(self.listaRegistros[posicion].nacionalidad)
        self.dt_nacionalidad.config(bg=self.bgEP, font=("Consolas", 10))
        self.dt_nacionalidad.grid(row=1, column=3, ipady=5)


        # CONTACTO ---
        vali_contact=self.cont.register(self.validador.validarStr)
        self.var_contacto=StringVar()
        self.dt_contacto=Entry(self.cont,
                                textvariable=self.var_contacto,
                                justify="center",
                                validate="key",
                                validatecommand=(vali_contact, "%d", "%S", "%s")
                                )
        self.var_contacto.set(self.listaRegistros[posicion].contacto)
        self.dt_contacto.config(bg=self.bgEP, font=("Consolas", 10))
        self.dt_contacto.grid(row=1, column=1, ipady=5)


        # EDAD ---
        vali_edad=self.cont.register(self.validador.validarEdad)
        self.var_edad=StringVar()
        self.dt_edad=Entry(self.cont,    
                                textvariable=self.var_edad,
                                justify="center",
                                validate="key",
                                validatecommand=(vali_edad,"%d","%S","%s")
                                )
        self.var_edad.set(self.listaRegistros[posicion].edad)
        self.dt_edad.config(bg=self.bgEP, font=("Consolas", 10))
        self.dt_edad.grid(row=2, column=1, ipady=5)

        # FECHA INGRESO ---
        self.var_fecha_ingreso=StringVar()
        self.dt_fecha_ingreso=Entry(self.cont,
                                textvariable=self.var_fecha_ingreso,
                                justify="center"
                                )
        self.var_fecha_ingreso.set(self.listaRegistros[posicion].fecha_ingreso)
        self.dt_fecha_ingreso.config(bg=self.bgEP, font=("Consolas", 10))
        self.stateEntry(self.dt_fecha_ingreso, 0)
        self.dt_fecha_ingreso.grid(row=1, column=5, ipady=5)


        # FECHA SALIDA ---
        self.var_fecha_salida=StringVar()
        self.dt_fecha_salida=Entry(self.cont,
                                textvariable=self.var_fecha_salida,
                                justify="center"
                                )
        self.var_fecha_salida.set(self.listaRegistros[posicion].fecha_salida)
        self.dt_fecha_salida.config(bg=self.bgEP, font=("Consolas", 10))
        self.stateEntry(self.dt_fecha_salida, 0)
        self.dt_fecha_salida.grid(row=2, column=5, ipady=5)


        # ESTADO
        self.var_estado=StringVar()
        self.dt_estado=Entry(self.cont,
                                textvariable=self.var_estado,
                                justify="center"
                                )
        self.var_estado.set(self.listaRegistros[posicion].estado)
        self.stateEntry(self.dt_estado, 0)
        self.dt_estado.config(bg=self.bgEP, font=("Consolas", 10))
        self.dt_estado.grid(row=2, column=3, ipady=5)


        # DEPO RONIN
        vali_ronin=self.cont.register(self.validador.validarRonin)
        self.var_depo_ronin=StringVar()
        self.dt_depo_ronin=Entry(self.cont,
                                textvariable=self.var_depo_ronin,
                                justify="center",
                                width=50,
                                validate="key",
                                validatecommand=(vali_ronin,"%d", "%s")
                                )
        self.var_depo_ronin.set(self.listaRegistros[posicion].depo_ronin)
        self.dt_depo_ronin.config(bg=self.bgEP, font=("Consolas", 10))
        self.dt_depo_ronin.grid(row=3, column=1, ipady=6, columnspan=3)





    def getButtonsPersona(self):
        # BOTON COPIAR RONIN ---
        bt=Button(self.cont, text="Copiar", command=self.getRonin)
        bt.grid(row=3, column=4)



    # FUNCIONES PERSONA ---
    def getRonin(self):
        info=self.var_depo_ronin.get()
        pc.copy(info)
    #CONFIRMACION GUARDADO ---
    def validarCambiosPersona(self):        
        self.datosP=(self.var_Nombre.get(), self.var_apellido.get(), self.var_edad.get(), self.var_nacionalidad.get(), self.var_contacto.get(), self.var_depo_ronin.get(), self.var_cedula.get())
        msg=""
        if len(self.var_Nombre.get())<3:
            msg+=" Nombre Invalid0\n"
        if len(self.var_apellido.get())<3:
            msg+=" Apellido Invalido\n"
        if len(self.var_edad.get())>0:
            if int(self.var_edad.get())<18:
                    msg+=" Edad Invalida\n"
        else: 
            msg+=" Edad Nula no Permitida\n"
        if len(self.var_nacionalidad.get())<3:
            msg+=" Nacionalidad Invalida\n"
        if len(self.var_contacto.get())<3:
            msg+=" Contacto Invalido\n"
        if len(self.var_depo_ronin.get())<6:
            msg+=" Ronin Invalida\n"
    
        print(self.datosP)
        if msg=="":
            lista=(self.dt_Nombre, self.dt_apellido, self.dt_Cedula, self.dt_nacionalidad, self.dt_contacto, self.dt_edad, self.dt_depo_ronin)
            self.objGui.swapState(lista, 0)
            self.ep=BotonRGB_Grid(self.DetailsRight, "GUARDAR", 0, 0, self.confGuardado)
        else:
            VentanaEmergente("ERROR EN LOS DATOS ENVIADOS", "Aceptar", "Editar", msg, lambda:print(""))

    def confGuardado(self):
        VentanaEmergente("CONFIRMAR CAMBIOS","CANCELAR", " GUARDAR ","Para ver los cambios Reflejados\nrefresque la tabla", self.funtionEditarPersona)

    # FUNCION PARA GUARDAR PERSONA ---
    def funtionEditarPersona(self):
        x=self.objCP.modificarPersona("dataxie", self.datosP)
        print(x)
        
    
    def confModificacion(self):
        VentanaEmergente("CONFIRMAR CAMBIOS", "CANCELAR", "CONFIRMAR", "TODOS LOS CAMBIOS\nSE VERAN AFECTADOS AL\nACTUALIZAR LA TABLA", self.funtionCambiarEstado)

    # REGISTRAR PERSONA ---
    def registrarPersona(self):
        lista=(self.br.boton, self.bron.boton)
        InsertPersona(lista)

    # CAMBIADOR DE ESTADO EN LA BASE DE DATOS
    def funtionCambiarEstado(self):
        if self.var_estado.get()=="A":
            self.dato=("I", self.var_cedula.get())
        else:
            self.dato=("A", self.var_cedula.get())
            
        print(self.objCP.cambiarEstadoPersona("dataxie",self.dato))






    # MODIFICAR RONIN --- PENDIENTE
    def editarRonin(self, posicion):
        self.getFramesRonin()
        self.getLabelsRonin(posicion)
        self.getEntrysRonin(posicion)
        self.getButtonsRonin(posicion)

    def getFramesRonin(self):
        self.fmR=Frame(self.fm_Details)
        self.fmR.config(bg="#c7c7c7")
        self.fmR.place(x=140, y=50, width=750 , height=300)

        # Tamaño Contenedores
        fw=525
        fh=60
        self.bgr="#668788"
        self.titulo=Frame(self.fmR)
        self.titulo.pack(pady=10)

        self.cont1=Frame(self.fmR, width=fw, height=fh, bg=self.bgr)
        self.cont1.grid_propagate(0)
        self.cont1.pack()

        self.cont2=Frame(self.fmR, width=fw, height=fh, bg=self.bgr)
        self.cont2.grid_propagate(0)
        self.cont2.pack()

        self.titulo2=Frame(self.fmR,)
        self.titulo2.pack(pady=10)

        self.cont3=Frame(self.fmR, width=fw+20, height=fh+10,bg=self.bgr)
        self.cont3.grid_propagate(0)
        self.cont3.pack()

    def getLabelsRonin(self, posicion):
        # TITULO
        print(posicion)
        Label(self.titulo, text="DATOS DE LA RONIN", font=("Consolas", 15, "bold"), bg="#000", fg="#fff").pack()
        # # ID
        Label(self.cont1, text="ID", font=("Consolas", 12),bg=self.bgr).grid(row=0, column=0, padx=20)
        self.var_id=self.listaRegistrosRonin[posicion].id
        Label(self.cont1, text=self.listaRegistrosRonin[posicion].id, font=("Consolas", 10),bg=self.bgr).grid(row=1, column=0)

        # # RONIN
        Label(self.cont1, text="RONIN", font=("Consolas", 12),bg=self.bgr).grid(row=0, column=2, padx=10)

        # SLP
        Label(self.cont2, text="Total SLP", font=("Consolas", 12),bg=self.bgr).grid(row=0, column=0, ipadx=10)
        Label(self.cont2, text=self.listaRegistrosRonin[posicion].total_slp, font=("Consolas", 10),bg=self.bgr).grid(row=1, column=0)

        # % MANAGER
        becado=float(self.listaRegistrosRonin[posicion].por_becado)
        manager=100-becado
        Label(self.cont2, text=f"{manager}% Manager", font=("Consolas", 12),bg=self.bgr).grid(row=0, column=1, padx=10)
        Label(self.cont2, text=f"{round(float(self.listaRegistrosRonin[posicion].total_slp)*(manager/100))}", font=("Consolas", 10),bg=self.bgr).grid(row=1, column=1)
        
        # BECADO

        Label(self.cont2, text=f"% Becado", font=("Consolas", 12),bg=self.bgr).grid(row=0, column=3)
        Label(self.cont2, text=f"{round(float(self.listaRegistrosRonin[posicion].total_slp)*(becado/100))}", font=("Consolas", 10),bg=self.bgr).grid(row=1, column=2, columnspan=2)

        # # FECHA 
        Label(self.cont2, text="Fecha Ingreso:", font=("Consolas", 12),bg=self.bgr).grid(row=0, column=4, padx=10)

        Label(self.cont2, text=self.listaRegistrosRonin[posicion].fecha_ingreso, font=("Consolas", 10),bg=self.bgr).grid(row=1, column=4)

        # # INFORMACION PAGO ---
        Label(self.titulo2, text="DATOS DE PAGO", font=("Consolas", 15, "bold"), bg="#000", fg="#fff").pack()
        # # INFORMACION BECADO
        Label(self.cont3, text="Becado:", font=("Consolas", 11),bg=self.bgr).grid(row=1, column=0, pady=10)

        # TEST ---
        datoT=(self.listaRegistrosRonin[posicion].becado,)
        ld=self.objCP.validarCedula("dataxie", datoT)
        if ld!=None:
            nombre=ld.nombre
        else:
            nombre="None"
        

        Label(self.cont3, text=nombre, font=("Consolas", 10)).grid(row=1, column=1)
        Label(self.cont3, text="Cuenta:", font=("Consolas", 11),bg=self.bgr).grid(row=1, column=2)

        self.var_roninbeca=StringVar()
        dato=(self.listaRegistrosRonin[posicion].becado,)
        self.lr=self.objCP.validarCedula("dataxie", dato)
        try:
            Label(self.cont3, text=str(self.lr.depo_ronin), font=("Consolas", 10)).grid(row=1, column=3)
            Button(self.cont3, text="Remover Beca", command=lambda:self.removerBeca(posicion)).grid(row=2, column=1)

        except:
            print("Becado no registrado")
            Label(self.cont3, text="Becados Disponibles", width=25, font=("Consolas", 10),bg=self.bgr).grid(row=1, column=3)

            lista=["Selecionar Becado"]
            pd=PersonasDisponibles()
            l2=pd.getData()
            for i in l2:
                lista.append(i)

            self.combo = ttk.Combobox(
            self.cont3,
            state="readonly",
            values=lista
            )
            self.combo.set(lista[0])
            self.combo.grid(row=1, column=4)
            
            Button(self.cont3, text="Asignar Beca", command=lambda:self.asignarBeca(posicion)).grid(row=2, column=4)

            
    
    def getEntrysRonin(self, posicion):
        # RONIN ---
        vali_ronin=self.cont3.register(self.validador.validarRonin)
        self.var_ronin=StringVar()
        ronin=Entry(self.cont1, 
        textvariable=self.var_ronin,
        validate="key",
        validatecommand=(vali_ronin,"%d", "%s")
        )
        ronin.config(width=50, font=("Consolas", 10))
        self.var_ronin.set(self.listaRegistrosRonin[posicion].ronin)
        ronin.grid(row=1, column=2)

        # %BECADO   ----
        vali_por_beca=self.cont2.register(self.validador.validarEdad)
        self.var_por_becado=StringVar()
        self.por_becado=Entry(self.cont2, 
            textvariable=self.var_por_becado,
            validate="key",
            validatecommand=(vali_por_beca,"%d","%S","%s"),
            justify="center"
        )
        self.var_por_becado.set(int(self.listaRegistrosRonin[posicion].por_becado))
        self.por_becado.config(width=4)
        self.por_becado.grid(row=0, column=2, sticky="e")

    def getButtonsRonin(self, posicion):
        
        Button(self.cont1, text="View Market", font=("Consolas", 10, "bold"), command=lambda:self.viewMarket(self.listaRegistrosRonin[posicion].ronin)).grid(row=1, column=4, pady=10)
        try:
            dato=self.lr.depo_ronin
            Button(self.cont3, text="Copiar Ronin", command=lambda:self.funtionCopy(dato), font=("Consolas", 10, "bold")).grid(row=2, column=2, columnspan=2)
        except:
            print("ronin no encontrada")

    # FUNCIONES RONIN
    def asignarBeca(self, posicion):
        id_ronin=self.listaRegistrosRonin[posicion].id
        id_persona=self.combo.get()
        if id_persona!="Selecionar Becado":
            print(id_ronin, id_persona)
            self.datosR=(id_persona, id_ronin)
            VentanaEmergente("CONFIRMACION", "CANCELAR", "CONTINUAR", "TODOS LOS DATOS SE VERAN \n SE VERAN REFLEJADOS AL \nACTUALIZAR LA PAGINA", self.asignarBeca2)
        else:
            VentanaEmergente("USUARIO NO SELECCIONADO", "CANCELAR", "CONTINUAR", "USTED NO HA SELECIONADO\n NINGUN USUARIO", lambda:print())
    
    def asignarBeca2(self):
        print(self.objCR.asignarBecado("dataxie", self.datosR))

    def removerBeca(self, posicion):
        dato=(self.listaRegistrosRonin[posicion].id,)
        print(dato)
        VentanaEmergente("REMOVER BECA", "CANCELAR", "ACEPTAR", "TODOS LOS DATOS SE VERAN \n SE VERAN REFLEJADOS AL \nACTUALIZAR LA TABLA", lambda:self.objCR.removerBecado("dataxie", dato))
  
    

    def funtionCopy(self, text):
        try:
            pc.copy(text)
        except:
            print("No se han encontrado elemento que copiar")


    def viewMarket(self, ronin):
        import webbrowser
        webbrowser.open_new("https://marketplace.axieinfinity.com/profile/"+ronin+ "/axie/?game=orgin")
    
    def confGuardadoR(self):
        VentanaEmergente("¿ESTAS SEGURO?", "NO", "SI", "TODOS LOS DATOS SE VERAN \n SE VERAN REFLEJADOS AL \nACTUALIZAR LA PAGINA", self.modificarRonin)

    def modificarRonin(self):
        datos=(self.var_ronin.get(), self.var_por_becado.get(), self.var_id)
        print(self.objCR.modifyRonin("dataxie", datos))

    def confDelete(self):
        VentanaEmergente("¿ESTAS SEGURO?", "NO", "SI", "UNA VEZ ACEPTADO \nSE ELIMINARA DE FORMA\nPERMANENTE\nTODOS LOS DATOS AFECTADORS SE \nREFLEJARAN EN LA TABLA AL REFRES", self.eliminarRonin)

    def eliminarRonin(self):
        dato=(self.var_id,)
        print(self.objCR.deleteRonin("dataxie", dato))

    # CAMBIAR STATE  =========
    def stateEntry(self, entry, valor):
        """"0=Disable | 1=normal"""
        if valor==0:
            entry.config(state="disabled")
        elif valor==1:
            entry.config(state="normal")
        else:
            print("Estado no reconocido")


    





# TEST  ===============================================================
# root=Tk()
# TablaEstandar(root, "persona")

# root.mainloop()
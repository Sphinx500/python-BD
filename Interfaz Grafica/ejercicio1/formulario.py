import tkinter as obj_tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st

import personas

class FormularioPersonas:
    def __init__(self):
        self.persona = personas.CrudPersonas()  
        self.ventana = obj_tk.Tk()  
        ancho_ventana = 750
        alto_ventana = 350
        x_ventana = self.ventana.winfo_screenwidth() // 2 - ancho_ventana // 2 
        y_ventana = self.ventana.winfo_screenheight() // 2 - alto_ventana // 2 # 
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.ventana.geometry(posicion) 
        self.ventana.resizable(0, 0)  
        self.ventana.title("CRUD de Personas")
        self.panel_opciones = ttk.Notebook(self.ventana)
        self.nueva_persona()
        self.consulta_id()
        self.personas_lista()
        self.borrar()
        self.actualizar()
        self.panel_opciones.grid(column=0, row=0, padx=10, pady=10)
        self.ventana.mainloop()
    
    def nueva_persona(self):
        self.agregar_pers = ttk.Frame(self.panel_opciones)
        self.panel_opciones.add(self.agregar_pers, text="Alta de personas")
        self.labelframe1 = ttk.LabelFrame(self.agregar_pers, text="Persona")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)


        self.label1 = ttk.Label(self.labelframe1, text="Nombre:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.nombrenvo = obj_tk.StringVar() 
        self.entrynombre = ttk.Entry(self.labelframe1, textvariable=self.nombrenvo)
        self.entrynombre.grid(column=1, row=0, padx=4, pady=4)

        
        self.label1 = ttk.Label(self.labelframe1, text="Edad:")
        self.label1.grid(column=0, row=1, padx=4, pady=4) 
        self.edadnvo = obj_tk.StringVar()
        self.entryedad = ttk.Entry(self.labelframe1, textvariable=self.edadnvo)
        self.entryedad.grid(column=1, row=1, padx=4, pady=4)

        
        self.label1 = ttk.Label(self.labelframe1, text="correo:")
        self.label1.grid(column=2, row=0, padx=4, pady=4)
        self.mailnvo = obj_tk.StringVar() 
        self.entrymail = ttk.Entry(self.labelframe1, textvariable=self.mailnvo)
        self.entrymail.grid(column=3, row=0, padx=4, pady=4)


        self.label2 = ttk.Label(self.labelframe1, text="Telefono:")
        self.label2.grid(column=2, row=1, padx=4, pady=4)
        self.phonenvo = obj_tk.StringVar()
        self.entryphone = ttk.Entry(self.labelframe1, textvariable=self.phonenvo)
        self.entryphone.grid(column=3, row=1, padx=4, pady=4)

        
        self.boton1 = ttk.Button(self.labelframe1, text="Agregar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4) 

    def agregar(self):
        datos = (self.nombrenvo.get(), self.edadnvo.get(), self.mailnvo.get(), self.phonenvo.get())
        self.persona.registro(datos)
        mb.showinfo("Información", "Los datos fueron cargados correctamente")
        self.nombrenvo.set("")
        self.edadnvo.set("")
        self.mailnvo.set("")
        self.phonenvo.set("")


    def consulta_id(self):
        self.pagina2 = ttk.Frame(self.panel_opciones)
        self.panel_opciones.add(self.pagina2, text="Consulta por ID")
        
        self.labelframe2 = ttk.LabelFrame(self.pagina2, text="Personas")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)


        self.label1 = ttk.Label(self.labelframe2, text="ID:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.id = obj_tk.StringVar()
        self.entryid = ttk.Entry(self.labelframe2, textvariable=self.id)
        self.entryid.grid(column=1, row=0, padx=4, pady=4)

        
        self.label2 = ttk.Label(self.labelframe2, text="Nombre:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombre = obj_tk.StringVar() 
        self.entrynombre = ttk.Entry(self.labelframe2, textvariable=self.nombre, state="readonly") 
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)

        
        self.label2 = ttk.Label(self.labelframe2, text="Edad:")
        self.label2.grid(column=2, row=1, padx=4, pady=4)
        self.edad = obj_tk.StringVar() 
        self.entryedad = ttk.Entry(self.labelframe2, textvariable=self.edad, state="readonly") 
        self.entryedad.grid(column=3, row=1, padx=4, pady=4)

        
        self.label2 = ttk.Label(self.labelframe2, text="Correo:")
        self.label2.grid(column=2, row=2, padx=4, pady=4)
        self.mail = obj_tk.StringVar() 
        self.entrymail = ttk.Entry(self.labelframe2, textvariable=self.mail, state="readonly") 
        self.entrymail.grid(column=3, row=2, padx=4, pady=4)

        
        self.label3 = ttk.Label(self.labelframe2, text="Telefono:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.phone = obj_tk.StringVar() 
        self.entryphone = ttk.Entry(self.labelframe2, textvariable=self.phone, state="readonly") 
        self.entryphone.grid(column=1, row=2, padx=4, pady=4)

        self.boton1 = ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos = (self.id.get(),)
        respuesta =  self.persona.consulta(datos)

        if len(respuesta) > 0:
            self.nombre.set(respuesta[0][0])
            self.edad.set(respuesta[0][1])
            self.mail.set(respuesta[0][2])
            self.phone.set(respuesta[0][3])
        else:
            self.nombre.set("")
            self.edad.set("")
            self.mail.set("")
            self.phone.set("")
            mb.showinfo("Información", "No existe una persona con ese ID")
    
    def personas_lista(self):
        # Agrega un contenedor al panel de pestaña de la ventana creada en el constructor principal
        self.pagina3 = ttk.Frame(self.panel_opciones)
        # Agrega un texto descriptivo de la pestaña
        self.panel_opciones.add(self.pagina3, text="Lista de Personas")
        # Agrega una etiqueta descriptiva del contenedor
        self.labelframe3 = ttk.LabelFrame(self.pagina3, text="Personas")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

        # Agrega un boton, que al momento de ser pulsado, llamara a la funcion "listar"
        self.boton1 = ttk.Button(self.labelframe3, text="Ver Personas", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        # Agrega un Scroll al conenedor
        self.scrolledtext1 = st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0, row=1, padx=10, pady=10)
        
    def listar(self):
        respuesta = self.persona.consulta_todos()
        self.scrolledtext1.delete("1.0", obj_tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(obj_tk.END, "ID:" + str(fila[0]) +
                                    "\nNombre:" + fila[1] +
                                    "\nEdad:" + str(fila[2]) +
                                    "\nCorreo:" + fila[3] +
                                    "\nTelefono:" + str(fila[4]) + "\n\n")

    def borrar(self):
        # Agrega un contenedor al panel de pestaña de la ventana creada en el constructor principal
        self.pagina4 = ttk.Frame(self.panel_opciones)
        # Agrega un texto descriptivo de la pestaña
        self.panel_opciones.add(self.pagina4, text="Eliminación de Personas")
        # Agrega una etiqueta descriptiva del contenedor
        self.labelframe4 = ttk.LabelFrame(self.pagina4, text="Personas")
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
        # Agrega una etiqueta descriptiva del contenedor
        self.label1 = ttk.Label(self.labelframe4, text="ID:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idborra = obj_tk.StringVar()  
        self.entryborra = ttk.Entry(self.labelframe4, textvariable=self.idborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)

        # Agrega un boton, que al momento de ser pulsado, llamara a la funcion "borrar"
        self.boton1 = ttk.Button(self.labelframe4, text="Eliminar", command=self.elimina)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def elimina(self):
        datos = (self.idborra.get(),)
        cantidad = self.persona.eliminar_persona(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Se borró la persona con el ID")
        else:
            mb.showinfo("Información", "No existe la persona con ese ID")

    def actualizar(self):
        # Agrega un contenedor al panel de pestaña de la ventana creada en el constructor principal
        self.pagina5 = ttk.Frame(self.panel_opciones)
        # Agrega un texto descriptivo de la pestaña
        self.panel_opciones.add(self.pagina5, text="Actualizar Persona")
        # Agrega una etiqueta descriptiva del contenedor
        self.labelframe5 = ttk.LabelFrame(self.pagina5, text="Personas")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)

        # Agrega una etiqueta descriptiva del contenedor
        self.label1 = ttk.Label(self.labelframe5, text="ID:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idmod = obj_tk.StringVar()
        self.entryid = ttk.Entry(self.labelframe5, textvariable=self.idmod)
        self.entryid.grid(column=1, row=0, padx=4, pady=4)

        # Agrega una etiqueta descriptiva del contenedor
        self.label2 = ttk.Label(self.labelframe5, text="Nombre:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombremod = obj_tk.StringVar()
        self.entrynombre = ttk.Entry(self.labelframe5, textvariable=self.nombremod)
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)

        # Agrega una etiqueta descriptiva del contenedor
        self.label3 = ttk.Label(self.labelframe5, text="Edad:")
        self.label3.grid(column=2, row=1, padx=4, pady=4)
        self.edadmod = obj_tk.StringVar()
        self.entryedad = ttk.Entry(self.labelframe5, textvariable=self.edadmod)
        self.entryedad.grid(column=3, row=1, padx=4, pady=4)

        # Agrega una etiqueta descriptiva del contenedor
        self.label3 = ttk.Label(self.labelframe5, text="Correo:")
        self.label3.grid(column=2, row=2, padx=4, pady=4)
        self.mailmod = obj_tk.StringVar()
        self.entrymail = ttk.Entry(self.labelframe5, textvariable=self.mailmod)
        self.entrymail.grid(column=3, row=2, padx=4, pady=4)

        # Agrega una etiqueta descriptiva del contenedor
        self.label3 = ttk.Label(self.labelframe5, text="Telefono:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.phonemod = obj_tk.StringVar()
        self.entryphone = ttk.Entry(self.labelframe5, textvariable=self.phonemod)
        self.entryphone.grid(column=1, row=2, padx=4, pady=4)


        # Agrega un boton, que al momento de ser pulsado, llamara a la funcion "consultar_mod"
        self.boton1 = ttk.Button(self.labelframe5, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

        # Agrega un boton, que al momento de ser pulsado, llamara a la funcion "modifica"
        self.boton2 = ttk.Button(self.labelframe5, text="Modificar", command=self.actualiza)
        self.boton2.grid(column=3, row=3, padx=4, pady=4)

    def actualiza(self):
        datos = (self.nombremod.get(), self.edadmod.get(),self.mailmod.get(), self.phonemod.get(), self.idmod.get())
        numero = self.persona.actualizar_persona(datos)
        if numero == 1:
            mb.showinfo("Información", "Se modificó el artículo")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")
    
    def consultar_mod(self):
        datos = (self.idmod.get(),)
        respuesta = self.persona.consulta(datos)
        if len(respuesta) > 0:
            self.nombremod.set(respuesta[0][0])
            self.edadmod.set(respuesta[0][1])
            self.mailmod.set(respuesta[0][2])
            self.phonemod.set(respuesta[0][3])
        else:
            self.nombremod.set("")
            self.edadmod.set("")
            self.mailmod.set("")
            self.phonemod.set("")
            mb.showinfo("Información", "No existe un artículo con dicho código")

aplicacion1 = FormularioPersonas()


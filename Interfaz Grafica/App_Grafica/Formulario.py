# Importacion de los modulos del paquete tkinter, que permite crear pantallas graficas
import tkinter as obj_tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
# Clase que contiene los metodos CRUD para inteactuar con la BD
import Productos


class FormularioProductos:

    # Metodo constructor de la clase, donde inicializamos la creacion de la ventana
    def __init__(self):
        self.producto = Productos.CrudProductos()  # Cracion de un objeto de la clase productos para utilizar los metodos
        self.ventana = obj_tk.Tk()  # Creamos el objeto del paquete TKinder
        ancho_ventana = 750
        alto_ventana = 350
        x_ventana = self.ventana.winfo_screenwidth() // 2 - ancho_ventana // 2 # Se obtiene el ancho de la pantalla completa y se divide entre 2
        y_ventana = self.ventana.winfo_screenheight() // 2 - alto_ventana // 2 # Se obtiene la altura de la pantalla completa y se divide entre 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.ventana.geometry(posicion) # Posiciona la ubicacion de la venta de una forma centrada
        self.ventana.resizable(0, 0)  # No se permitira modificar el tamaño de la ventana
        self.ventana.title("CRUD de Productos")
        self.panel_opciones = ttk.Notebook(self.ventana)  # Se crea un panel de pestañas y se agrega a nuestra ventana principal
        self.nuevo_producto()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrado()
        self.modificar()
        self.panel_opciones.grid(column=0, row=0, padx=10, pady=10)
        self.ventana.mainloop()

    def nuevo_producto(self):
        # Agrega un contenedor al panel de pestaña de la ventana creada en el constructor principal
        self.agregar_prod = ttk.Frame(self.panel_opciones)
        # Agrega un texto descriptivo de la pestaña
        self.panel_opciones.add(self.agregar_prod, text="Alta de productos")
        # Agrega una etiqueta descriptiva del contenedor
        self.labelframe1 = ttk.LabelFrame(self.agregar_prod, text="Producto")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        # Agrega una etiqueta descriptiva para el campo que recibira los datos de entrada
        self.label1 = ttk.Label(self.labelframe1, text="Descripción:")
        self.label1.grid(column=0, row=0, padx=4, pady=4) # Se define el tamaño de la etiqueta
        self.descripcioncarga = obj_tk.StringVar() # obtiene el valor del campo y lo asigna a una variable
        self.entrydescripcion = ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)

        # Agrega una etiqueta descriptiva para el campo que recibira los datos de entrada
        self.label2 = ttk.Label(self.labelframe1, text="Precio:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.preciocarga = obj_tk.StringVar() # obtiene el valor del campo y lo asigna a una variable
        self.entryprecio = ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)

        # Agrega un boton, que al momento de ser pulsado, llamara a la funcion "aregar"
        self.boton1 = ttk.Button(self.labelframe1, text="Agregar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4) # Se define el tamaño del boton

    def agregar(self):
        # Se crea una tubla con los valores obtenidos de los campos del contenedor
        datos = (self.descripcioncarga.get(), self.preciocarga.get())
        self.producto.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados correctamente") # Muestra una ventana emergente con un mensaje
        # Se limpian los campos del contenedor
        self.descripcioncarga.set("")
        self.preciocarga.set("")

    def consulta_por_codigo(self):
        # Agrega un contenedor al panel de pestaña de la ventana creada en el constructor principal
        self.pagina2 = ttk.Frame(self.panel_opciones)
        # Agrega un texto descriptivo de la pestaña
        self.panel_opciones.add(self.pagina2, text="Consulta por código")
        # Agrega una etiqueta descriptiva del contenedor
        self.labelframe2 = ttk.LabelFrame(self.pagina2, text="Producto")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        # Agrega una etiqueta descriptiva para el campo que recibira los datos de entrada, para hacer la busqueda del producto
        self.label1 = ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo = obj_tk.StringVar() # obtiene el valor del campo y lo asigna a una variable
        self.entrycodigo = ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        # Agrega una etiqueta descriptiva para el campo que recibira los datos de entrada
        self.label2 = ttk.Label(self.labelframe2, text="Descripción:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion = obj_tk.StringVar() # obtiene el valor del campo y lo asigna a una variable
        self.entrydescripcion = ttk.Entry(self.labelframe2, textvariable=self.descripcion, state="readonly") # con state="readonly", no permite editar el campo
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        # Agrega una etiqueta descriptiva para el campo que recibira los datos de entrada
        self.label3 = ttk.Label(self.labelframe2, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.precio = obj_tk.StringVar() # obtiene el valor del campo y lo asigna a una variable
        self.entryprecio = ttk.Entry(self.labelframe2, textvariable=self.precio, state="readonly") # con state="readonly", no permite editar el campo
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        # Agrega un boton, que al momento de ser pulsado, llamara a la funcion "consultar"
        self.boton1 = ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos = (self.codigo.get(),) # Se crea una tupla con los valores para la busqueda
        respuesta = self.producto.consulta(datos)
        #Si la lista que devuelve la consulta contiene datos, se setea la info del primer elemento a los campos del formulario
        if len(respuesta) > 0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def listado_completo(self):
        # Agrega un contenedor al panel de pestaña de la ventana creada en el constructor principal
        self.pagina3 = ttk.Frame(self.panel_opciones)
        # Agrega un texto descriptivo de la pestaña
        self.panel_opciones.add(self.pagina3, text="Listado de productos")
        # Agrega una etiqueta descriptiva del contenedor
        self.labelframe3 = ttk.LabelFrame(self.pagina3, text="Productos")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

        # Agrega un boton, que al momento de ser pulsado, llamara a la funcion "listar"
        self.boton1 = ttk.Button(self.labelframe3, text="Ver Productos", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        # Agrega un Scroll al conenedor
        self.scrolledtext1 = st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0, row=1, padx=10, pady=10)

    def listar(self):
        respuesta = self.producto.recuperar_todos()
        self.scrolledtext1.delete("1.0", obj_tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(obj_tk.END, "código:" + str(fila[0]) +
                                      "\ndescripción:" + fila[1] +
                                      "\nprecio:" + str(fila[2]) + "\n\n")

    def borrado(self):
        # Agrega un contenedor al panel de pestaña de la ventana creada en el constructor principal
        self.pagina4 = ttk.Frame(self.panel_opciones)
        # Agrega un texto descriptivo de la pestaña
        self.panel_opciones.add(self.pagina4, text="Eliminación de productos")
        # Agrega una etiqueta descriptiva del contenedor
        self.labelframe4 = ttk.LabelFrame(self.pagina4, text="Productos")
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
        # Agrega una etiqueta descriptiva del contenedor
        self.label1 = ttk.Label(self.labelframe4, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigoborra = obj_tk.StringVar()  # obtiene el valor del campo y lo asigna a una variable
        self.entryborra = ttk.Entry(self.labelframe4, textvariable=self.codigoborra)  # Campo de texto
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)

        # Agrega un boton, que al momento de ser pulsado, llamara a la funcion "borrar"
        self.boton1 = ttk.Button(self.labelframe4, text="Eliminar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos = (self.codigoborra.get(),)
        cantidad = self.producto.baja(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Se borró el artículo con dicho código")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def modificar(self):
        # Agrega un contenedor al panel de pestaña de la ventana creada en el constructor principal
        self.pagina5 = ttk.Frame(self.panel_opciones)
        # Agrega un texto descriptivo de la pestaña
        self.panel_opciones.add(self.pagina5, text="Modificar producto")
        # Agrega una etiqueta descriptiva del contenedor
        self.labelframe5 = ttk.LabelFrame(self.pagina5, text="Productos")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)
        # Agrega una etiqueta descriptiva del contenedor
        self.label1 = ttk.Label(self.labelframe5, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod = obj_tk.StringVar()
        self.entrycodigo = ttk.Entry(self.labelframe5, textvariable=self.codigomod)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        # Agrega una etiqueta descriptiva del contenedor
        self.label2 = ttk.Label(self.labelframe5, text="Descripción:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcionmod = obj_tk.StringVar()
        self.entrydescripcion = ttk.Entry(self.labelframe5, textvariable=self.descripcionmod)
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        # Agrega una etiqueta descriptiva del contenedor
        self.label3 = ttk.Label(self.labelframe5, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.preciomod = obj_tk.StringVar()
        self.entryprecio = ttk.Entry(self.labelframe5, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        # Agrega un boton, que al momento de ser pulsado, llamara a la funcion "consultar_mod"
        self.boton1 = ttk.Button(self.labelframe5, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
        # Agrega un boton, que al momento de ser pulsado, llamara a la funcion "modifica"
        self.boton2 = ttk.Button(self.labelframe5, text="Modificar", command=self.modifica)
        self.boton2.grid(column=1, row=4, padx=4, pady=4)

    def modifica(self):
        datos = (self.descripcionmod.get(), self.preciomod.get(), self.codigomod.get())
        cantidad = self.producto.modificacion(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Se modificó el artículo")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def consultar_mod(self):
        datos = (self.codigomod.get(),)
        respuesta = self.producto.consulta(datos)
        if len(respuesta) > 0:
            self.descripcionmod.set(respuesta[0][0])
            self.preciomod.set(respuesta[0][1])
        else:
            self.descripcionmod.set('')
            self.preciomod.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")


aplicacion1 = FormularioProductos()

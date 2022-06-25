import tkinter as obj_tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import alumnos


class FormularioAlumnos:
    def __init__(self):
        self.alumnos = alumnos.CrudAlumnos() 
        self.ventana = obj_tk.Tk()  
        ancho_ventana = 750
        alto_ventana = 350
        x_ventana = self.ventana.winfo_screenwidth() // 2 - ancho_ventana // 2 
        y_ventana = self.ventana.winfo_screenheight() // 2 - alto_ventana // 2 # 
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.ventana.geometry(posicion) 
        self.ventana.resizable(0, 0)  
        self.ventana.title("CRUD de Alumno")
        self.panel_opciones = ttk.Notebook(self.ventana)
        self.nuevo_alumno()
        self.consulta_id()
        self.alumno_lista()
        self.borrar()
        self.actualizar()
        self.panel_opciones.grid(column=0, row=0, padx=10, pady=10)
        self.ventana.mainloop()
    
    def nuevo_alumno(self):
        self.agregar_pers = ttk.Frame(self.panel_opciones)
        self.panel_opciones.add(self.agregar_pers, text="Alta de alumnos")
        self.labelframe1 = ttk.LabelFrame(self.agregar_pers, text="Alumno")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)


        self.label1 = ttk.Label(self.labelframe1, text="Nombre:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.nombrenvo = obj_tk.StringVar() 
        self.entrynombre = ttk.Entry(self.labelframe1, textvariable=self.nombrenvo)
        self.entrynombre.grid(column=1, row=0, padx=4, pady=4)

        
        self.label1 = ttk.Label(self.labelframe1, text="Carrera:")
        self.label1.grid(column=0, row=1, padx=4, pady=4) 
        self.carreranvo = obj_tk.StringVar()
        self.entrycarrera = ttk.Entry(self.labelframe1, textvariable=self.carreranvo)
        self.entrycarrera.grid(column=1, row=1, padx=4, pady=4)


        self.label2 = ttk.Label(self.labelframe1, text="Promedio:")
        self.label2.grid(column=2, row=1, padx=4, pady=4)
        self.promedionvo = obj_tk.StringVar()
        self.entrypromedio = ttk.Entry(self.labelframe1, textvariable=self.promedionvo)
        self.entrypromedio.grid(column=3, row=1, padx=4, pady=4)

        
        self.boton1 = ttk.Button(self.labelframe1, text="Agregar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4) 

    def agregar(self):
        datos = (self.nombrenvo.get(), self.carreranvo.get(), self.promedionvo.get())
        self.alumnos.registro(datos)
        mb.showinfo("Información", "Los datos fueron cargados correctamente")
        self.nombrenvo.set("")
        self.carreranvo.set("")
        self.promedionvo.set("")


    def consulta_id(self):
        self.pagina2 = ttk.Frame(self.panel_opciones)
        self.panel_opciones.add(self.pagina2, text="Consulta por ID")
        
        self.labelframe2 = ttk.LabelFrame(self.pagina2, text="Alumnos")
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

        
        self.label2 = ttk.Label(self.labelframe2, text="Carrera:")
        self.label2.grid(column=2, row=1, padx=4, pady=4)
        self.carrera = obj_tk.StringVar() 
        self.entrycarrera = ttk.Entry(self.labelframe2, textvariable=self.carrera, state="readonly") 
        self.entrycarrera.grid(column=3, row=1, padx=4, pady=4)

        
        self.label3 = ttk.Label(self.labelframe2, text="Promedio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.promedio = obj_tk.StringVar() 
        self.entrypromedio = ttk.Entry(self.labelframe2, textvariable=self.promedio, state="readonly") 
        self.entrypromedio.grid(column=1, row=2, padx=4, pady=4)

        self.boton1 = ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos = (self.id.get(),)
        respuesta =  self.alumnos.consulta(datos)

        if len(respuesta) > 0:
            self.nombre.set(respuesta[0][0])
            self.carrera.set(respuesta[0][1])
            self.promedio.set(respuesta[0][2])
        else:
            self.nombre.set("")
            self.carrera.set("")
            self.promedio.set("")
            mb.showinfo("Información", "No existe una persona con ese ID")
    
    def alumno_lista(self):
        self.pagina3 = ttk.Frame(self.panel_opciones)
        self.panel_opciones.add(self.pagina3, text="Lista de Alumnos")
        self.labelframe3 = ttk.LabelFrame(self.pagina3, text="Alumnos")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

        
        self.boton1 = ttk.Button(self.labelframe3, text="Ver Alumnos", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.boton2 = ttk.Button(self.labelframe3, text="Imprimir Aprobados", command=self.aprobados)
        self.boton2.grid(column=1, row=0, padx=4, pady=4)
        self.boton2 = ttk.Button(self.labelframe3, text="Imprimir Reprobados", command=self.reprobados)
        self.boton2.grid(column=2, row=0, padx=4, pady=4)
        self.scrolledtext1 = st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0, row=1, padx=10, pady=10)
        
    def listar(self):
        respuesta = self.alumnos.consulta_todos()
        self.scrolledtext1.delete("1.0", obj_tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(obj_tk.END, "ID:" + str(fila[0]) +
                                    "\nNombre:" + fila[1] +
                                    "\nCarrera:" + fila[2] +
                                    "\nPromedio:" + str(fila[3]) + "\n\n")

    def aprobados(self):
        respuesta = self.alumnos.aprobados()
        self.abrir = open("Aprobados.txt", "a", encoding="utf-8")
        for x in respuesta:
            linea = str(x[0]) + " | " + str(x[1]) + " | " + str(x[2]) + " | " + str(x[3])
        self.abrir.write(str(linea))
        mb.showinfo("Información", "Archivo generado correctamente")

    def reprobados(self):
        respuesta = self.alumnos.reprobados()
        self.abrir = open("Reprobados.txt", "a", encoding="utf-8")
        for x in respuesta:
            linea = str(x[0]) + " | " + str(x[1]) + " | " + str(x[2]) + " | " + str(x[3])
        self.abrir.write(str(linea))
        mb.showinfo("Información", "Archivo generado correctamente")

    def borrar(self):
        self.pagina4 = ttk.Frame(self.panel_opciones)
        self.panel_opciones.add(self.pagina4, text="Eliminación de Alumnos")
        self.labelframe4 = ttk.LabelFrame(self.pagina4, text="Alumnos")
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.labelframe4, text="ID:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idborra = obj_tk.StringVar()  
        self.entryborra = ttk.Entry(self.labelframe4, textvariable=self.idborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)

        self.boton1 = ttk.Button(self.labelframe4, text="Eliminar", command=self.elimina)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def elimina(self):
        datos = (self.idborra.get(),)
        cantidad = self.alumnos.eliminar_alumno(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Se borró el alumno con el ID")
        else:
            mb.showinfo("Información", "No existe el alumno con ese ID")

    def actualizar(self):
        self.pagina5 = ttk.Frame(self.panel_opciones)
        self.panel_opciones.add(self.pagina5, text="Actualizar Persona")
        self.labelframe5 = ttk.LabelFrame(self.pagina5, text="Personas")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)


        self.label1 = ttk.Label(self.labelframe5, text="ID:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idmod = obj_tk.StringVar()
        self.entryid = ttk.Entry(self.labelframe5, textvariable=self.idmod)
        self.entryid.grid(column=1, row=0, padx=4, pady=4)

        
        self.label2 = ttk.Label(self.labelframe5, text="Nombre:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombremod = obj_tk.StringVar()
        self.entrynombre = ttk.Entry(self.labelframe5, textvariable=self.nombremod)
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)

        
        self.label3 = ttk.Label(self.labelframe5, text="Carrera:")
        self.label3.grid(column=2, row=1, padx=4, pady=4)
        self.carreramod = obj_tk.StringVar()
        self.entrycarrera = ttk.Entry(self.labelframe5, textvariable=self.carreramod)
        self.entrycarrera.grid(column=3, row=1, padx=4, pady=4)

        
        self.label3 = ttk.Label(self.labelframe5, text="Promedio:")
        self.label3.grid(column=2, row=2, padx=4, pady=4)
        self.promediomod = obj_tk.StringVar()
        self.entrypromedio = ttk.Entry(self.labelframe5, textvariable=self.promediomod)
        self.entrypromedio.grid(column=3, row=2, padx=4, pady=4)



        self.boton1 = ttk.Button(self.labelframe5, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

        self.boton2 = ttk.Button(self.labelframe5, text="Modificar", command=self.actualiza)
        self.boton2.grid(column=3, row=3, padx=4, pady=4)

    def actualiza(self):
        datos = (self.nombremod.get(), self.carreramod.get(), self.promediomod.get() , self.idmod.get())
        numero = self.alumnos.actualizar_alumno(datos)
        if numero == 1:
            mb.showinfo("Información", "Se modificó el alumno")
        else:
            mb.showinfo("Información", "No existe alumno con ese ID")
    
    def consultar_mod(self):
        datos = (self.idmod.get(),)
        respuesta = self.alumnos.consulta(datos)
        if len(respuesta) > 0:
            self.nombremod.set(respuesta[0][0])
            self.carreramod.set(respuesta[0][1])
            self.promediomod.set(respuesta[0][2])
        else:
            self.nombremod.set("")
            self.carreramod.set("")
            self.promediomod.set("")
            mb.showinfo("Información", "No existe un alumno con ese ID")




aplicacion1 = FormularioAlumnos()


from tkinter import *
from tkinter import ttk
from gramatica import parser



ventana = Tk()
Mifr = Frame()
Mifr.config(bg="#A3E8E2")
Mifr.pack(fill="both", expand="True")
ventana.title("Proyecto1 Compiladores 2 201701015")

#FUNCIONES
def ejecutar():
    print(txtFuente.get("1.0", "end"))
    parser.parse(txtFuente.get("1.0", "end"))

#MENU DESPLEGABLE
barra = Menu(ventana)
ventana.config(menu=barra)
Opciones=Menu(barra, tearoff=0)
Opciones.add_command(label="Guardar")
Opciones.add_command(label="Cargar")
Opciones.add_command(label="Ayuda")
barra.add_cascade(label="Opciones", menu=Opciones)

lblTitulo=Label(Mifr,text="DB-Rust")
lblTitulo.config(bg="#A3E8E2")

txtFuente=Text(Mifr, height = 32, width = 52)
txtConsola=Text(Mifr, height = 32, width = 52)

botonExecute=Button(Mifr,text="Ejecutar",command=ejecutar)

botonExecute.grid(row=1,column=1,pady=10,padx=10)
lblTitulo.grid(row=0,column=1,pady=10,padx=10)
lblTitulo.grid(row=0,column=1,pady=10,padx=10)
txtFuente.grid(row=1,column=0,pady=10,padx=10)
txtConsola.grid(row=1,column=2,pady=10,padx=10)

ventana.mainloop()
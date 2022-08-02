from tkinter import *
from tkinter import ttk
from gramatica import parser
import instrucciones.Print as Imprimir


ventana = Tk()
Mifr = Frame()
Mifr.config(bg="#A3E8E2")
Mifr.pack(fill="both", expand="True")
ventana.title("Proyecto1 Compiladores 2 201701015")

#FUNCIONES
def ejecutar():

    print(txtFuente.get("1.0", "end"))
    Respuesta= parser.parse(str(txtFuente.get("1.0", "end")))
    consola=""
    Respuesta.ejecutar()
    print("------------------------------------")
    print(Imprimir.consola)
    txtConsola.insert("end",Imprimir.consola)

def Info():
    print("Agregar cuadro de dialogo con mi info")

#MENU DESPLEGABLE
barra = Menu(ventana)
ventana.config(menu=barra)
btnEditor=Menu(barra, tearoff=0)
btnReportes=Menu(barra, tearoff=0)
btnInfo=Menu(barra, tearoff=0)
barra.add_cascade(label="Editor", menu=btnEditor)
barra.add_cascade(label="Reportes", menu=btnReportes)
barra.add_cascade(label="Acerca de",command=Info)

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
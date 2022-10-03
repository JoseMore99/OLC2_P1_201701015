from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from gramatica import parser
import instrucciones.Print as Imprimir
from simbolo.arbol import Arbol
import simbolo.listaerrores as errores
from simbolo.ambito import ambito
from simbolo.listasimboloc3d import listasimboloc3d
import simbolo.listasimbolos as simbolo
 

ventana = Tk()
Mifr = Frame()
Mifr.config(bg="#A3E8E2")
Mifr.pack(fill="both", expand="True")
ventana.title("Proyecto1 Compiladores 2 201701015")

#FUNCIONES
def ejecutar():
    Imprimir.vaciar()
    print(txtFuente.get("1.0", "end"))
    Respuesta= parser.parse(str(txtFuente.get("1.0", "end"))+"\nmain();")
    global_a = ambito()
    if(Respuesta!=None):
        for i in Respuesta:
            if i != None:
                i.ejecutar(global_a)
        simbolo.Simbolos.graficar()
        simbolo.Simbolos.lista=[]
        
    astC3D = Arbol(Respuesta)  # entrada con parser
    tablaC3D = listasimboloc3d()
    astC3D.setGlobal(tablaC3D)
    tablaC3D.setNombre('Global')
    traduccionOut = ""
    for ins in astC3D.getInstrucciones():
        #nuevaTablaC3D = listasimboloc3d()
        astC3D.setTempNoUsados([])
        if(ins is not None):
           # print(ins)
            traduccion = ins.traducir(astC3D, tablaC3D)
            #print(traduccion)
            traduccionOut += traduccion["codigo"]
            #print(nuevaTablaC3D.getTamanio())
            #print(astC3D.getImports())
    encabezado = "#include <stdio.h>\n float stack[10000]; // Stack\n float heap[10000]; // Heap\n float P; // Puntero Stack\n float H; // Puntero Heap\n"
    
    encabezado+="float {}".format(astC3D.getImports())
    traduccionOut= encabezado+traduccionOut   
    traduccionOut+="""int main(){
    return 0;
}"""
    if(errores.Errores.lista!=[]):
        errores.Errores.graficar()
        errores.Errores.lista=[]
    #print("------------------------------------")
    #print(Imprimir.consola)
    txtConsola.delete("1.0","end")
    txtConsola.insert("end",Imprimir.consola)
    #print(tablaC3D.getTamanio())
    codigo3d.delete("1.0","end")
    codigo3d.insert("end",traduccionOut)


def Info():
    datos = "JOSE CARLOS MOREIRA PAZ\n"
    datos += "201701015\n"
    datos += "OLC2 PROYECTO 1 seccion D\n"
    messagebox.showinfo(message=datos, title="Datos personales")

def Borrar():
    txtFuente.delete("1.0","end")

#MENU DESPLEGABLE
barra = Menu(ventana)
ventana.config(menu=barra)
btnEditor=Menu(barra, tearoff=0)
btnReportes=Menu(barra, tearoff=0)
btnInfo=Menu(barra, tearoff=0)
barra.add_cascade(label="Editor", menu=btnEditor)
barra.add_cascade(label="Reportes", menu=btnReportes)
barra.add_cascade(label="Acerca de",command=Info)
barra.add_cascade(label="Borrar",command=Borrar)

lblTitulo=Label(Mifr,text="DB-Rust")
lblTitulo.config(bg="#A3E8E2")

txtFuente=ScrolledText(Mifr, height = 20, width = 52)
txtConsola=ScrolledText(Mifr, height = 20, width = 52)

codigo3d = ScrolledText(Mifr,  height=15)

botonExecute=Button(Mifr,text="Ejecutar",command=ejecutar)
botonTraductor=Button(Mifr,text="Traducir a C3D",command=ejecutar)

botonExecute.grid(row=1,column=1,pady=5,padx=5)
botonTraductor.grid(row=2,column=1,pady=5,padx=5)
lblTitulo.grid(row=0,column=1,pady=5,padx=5)
lblTitulo.grid(row=0,column=1,pady=5,padx=5)
txtFuente.grid(row=1,column=0,pady=5,padx=5)
codigo3d.grid(row=3,columnspan=5,pady=5,padx=5,sticky=EW)
txtConsola.grid(row=1,column=2,pady=5,padx=5)

ventana.mainloop()
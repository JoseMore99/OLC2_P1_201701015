import os
from simbolo.errores import errores

class listaerrores:
    def __init__(self) :
        self.lista =[]

    def nuevoError(self,fila, columna, clase,descripcion):
        temp =errores(fila, columna, clase,descripcion)
        self.lista.append(temp)

    def graficar(self):
        textdot = open("Errores.dot","w")
        textdot.write("digraph G{\nnode [shape=record];\n")
        textdot.write('a0 [label=<<TABLE border="1" cellspacing="5" cellpadding="5" style="rounded" bgcolor="yellow:violet">\n"')

        textdot.write('<TR><TD>FILA</TD><TD>COLUMNA</TD><TD>CLASE</TD><TD>DESCRIPCION</TD></TR>\n')
        for i in self.lista:
            i.descripcion=i.descripcion.replace("}","\\}")
            i.descripcion=i.descripcion.replace("{","\\{")
            i.descripcion=i.descripcion.replace(">","\\>")
            i.descripcion=i.descripcion.replace("<","\\<")
            textdot.write('<TR><TD>{}</TD><TD>{}</TD><TD>{}</TD><TD>{}</TD></TR>\n'.format(str(i.fila),str(i.columna),str(i.clase),str(i.descripcion)))
        textdot.write("</TABLE>>];")
        textdot.write("\n}")
        textdot.close()
        os.system('dot -Tpng Errores.dot -o Errores.png')

Errores = listaerrores()
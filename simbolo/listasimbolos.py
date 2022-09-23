import os

class listasimbolos:
    def __init__(self) :
        self.lista =[]

    def nuevoSimbolo(self,sim):
        self.lista.append(sim)

    def graficar(self):
        textdot = open("Simbolos.dot","w")
        textdot.write("digraph G{\nnode [shape=record];\n")
        textdot.write('a0 [label=<<TABLE border="1" cellspacing="5" cellpadding="5" style="rounded" bgcolor="yellow:blue">\n"')

        textdot.write('<TR><TD>FILA</TD><TD>COLUMNA</TD><TD>ID</TD><TD>TIPO DE SIMBOLO</TD>')
        textdot.write('<TD>TIPO DE DATO</TD><TD>AMBITO</TD></TR>\n')
        for i in self.lista:
        #simbolo.Simbolos.nuevoSimbolo({"fila":auxfunc.fila,"columna":auxfunc.columna,"id":auxfunc.nombre,"TS":"Arreglo","TD":auxfunc.tipo,"ambito":self.id})
        
            textdot.write('<TR><TD>{}</TD><TD>{}</TD><TD>{}</TD>'.format(str(i["fila"]),str(i["columna"]),str(i["id"])))
            textdot.write('<TD>{}</TD><TD>{}</TD><TD>{}</TD></TR>\n'.format(str(i["TS"]),str(i["TD"]),str(i["ambito"])))
        textdot.write("</TABLE>>];")
        textdot.write("\n}")
        textdot.close()
        os.system('dot -Tpng Simbolos.dot -o Simbolos.png')

Simbolos = listasimbolos()
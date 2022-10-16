import os
from expresion.Tipo import Tipo

class listasimboloc3d:
    def __init__(self, anterior=None):
        self.tablaAnterior = anterior
        self.tablaActual = {}
        self.tamanio = 0
        self.tipoDato = Tipo.ENTERO
        self.nombreDato = ""

    def getTamanio(self):
        return self.tamanio

    def setTamanio(self, t):
        self.tamanio = t

    def masTamanio(self):
        self.tamanio += 1

    def getAnterior(self):
        return self.tablaAnterior

    def setAnterior(self, anterior):
        self.tablaAnterior = anterior

    def getTabla(self):
        return self.tablaActual

    def setTabla(self, tabla):
        self.tablaActual = tabla

    def setVariable(self, simbolo):
        # SIMBOLO (self, tipo, identificador, temporal, num, esConst):
        #print(simbolo)
        if simbolo.getIdentificador() in self.tablaActual:
            self.tablaActual[simbolo.getIdentificador()] = simbolo
        else:
            self.tablaActual[simbolo.getIdentificador()] = simbolo
            self.tamanio += 1
        return 'La variable existe'
    
    def updateVariable (self,simbolo):
        aux = self
        cont = 0
        while aux != None:
            if simbolo.getIdentificador()  in aux.tablaActual:
                aux.tablaActual[simbolo.getIdentificador()] = simbolo
                #print(str(cont)+" : COOOOOOONT")
                break
            else:
                if aux.tablaAnterior != None:
                    cont += aux.tablaAnterior.getTamanio()
                aux = aux.tablaAnterior
        return None

    def graficar(self):
        textdot = open("Simbolosc3d.dot","w")
        textdot.write("digraph G{\nnode [shape=record];\n")
        textdot.write('a0 [label=<<TABLE border="1" cellspacing="5" cellpadding="5" style="rounded" bgcolor="yellow:blue">\n"')

        textdot.write('<TR><TD>ID</TD><TD>TIPO</TD><TD>UBICACION</TD></TR>\n')
        for i in self.tablaActual.values():
        #simbolo.Simbolosc3d.nuevoSimbolo({"fila":auxfunc.fila,"columna":auxfunc.columna,"id":auxfunc.nombre,"TS":"Arreglo","TD":auxfunc.tipo,"ambito":self.id})
            textdot.write('<TR><TD>{}</TD><TD>{}</TD><TD>{}</TD></TR>\n'.format(str(i.id),str(i.tipo),str(i.ubicacion)))
        textdot.write("</TABLE>>];")
        textdot.write("\n}")
        textdot.close()
        os.system('dot -Tpng Simbolosc3d.dot -o Simbolosc3d.png')

    def getVariable(self, id):
        aux = self
        cont = 0
        while aux != None:
            #print(cont)
            if id in aux.tablaActual:
                #print("aqui salio en "+ self.nombreDato)
                return {'simbolo': aux.tablaActual[id], 'entorno': cont}
            else:
                if aux.tablaAnterior != None:
                    cont += aux.tablaAnterior.getTamanio()
                aux = aux.tablaAnterior
        return None

    def getVariableEntorno(self, id):
        aux = self
        while aux != None:
            if id in aux.tablaActual:
                return aux.tablaActual[id]
            else:
                return None

    def getVariableGlobal(self, id):
        aux = self
        if id in aux.tablaActual:
            return aux.tablaActual[id]
        return None

    def getNombre(self):
        return self.nombreDato

    def setNombre(self, nombre):
        self.nombreDato = nombre
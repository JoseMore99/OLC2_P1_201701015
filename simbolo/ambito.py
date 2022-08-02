
from simbolo.simbolo import simbolo


class ambito:

    def __init__(self, anterior=None):
        self.anterior = anterior
        self.tablaSimbolos = {} 
        self.tablaFunciones = {}
        self.estaEnCiclo = False
        self.estaEnFuncion = False

    def nuevosimbolo(self, simbolo:simbolo):
        s = self.tablaSimbolos.get(simbolo.nombre)
        if s == None:
            self.tablaSimbolos[simbolo.nombre] = simbolo

    def editarSimbolo(self, llave, nuevo:simbolo):
        ambitoAux = self
        while ambitoAux != None:
            s = ambitoAux.tablaSimbolos.get(llave)
            if s != None:
                ambitoAux.tablaSimbolos[llave] = nuevo
            ambitoAux = ambitoAux.anterior

    def existesimbolo(self, llave):
        s = self.tablaSimbolos.get(llave)
        if s != None:
            return True
        return False

    def eliminarsimbolo(self, llave):
        s = self.tablaSimbolos.get(llave)
        if s != None:
            del self.tablaSimbolos[llave]

    def buscarsimbolo(self, llave):
        AmbitoAux = self
        while AmbitoAux != None:
            s = AmbitoAux.tablaSimbolos.get(llave)
            if s != None:
                return s
            AmbitoAux = AmbitoAux.anterior
        return None

    

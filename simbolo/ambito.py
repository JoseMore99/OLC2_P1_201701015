
from instrucciones.Struct import Struct
from instrucciones.funcion import funcion
from simbolo.simbolo import simbolo
import simbolo.listasimbolos as Simbolo

class ambito:

    def __init__(self, anterior=None):
        self.anterior = anterior
        self.tablaSimbolos = {} 
        self.tablaFunciones = {}
        self.tablaStructs = {}
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
    
    def nuevaFuncion(self, simbolo:funcion ):
        s = self.tablaFunciones.get(simbolo.id.lower())
        if s == None:
            self.tablaFunciones[simbolo.id.lower()] = simbolo
            Simbolo.Simbolos.nuevoSimbolo({"fila":simbolo.fila,"columna":simbolo.columna,"id":simbolo.id,"TS":"Funcion","TD":simbolo.tipo,"ambito":"Global"})
            

    def buscarFuncion(self, llave):
        ent = self
        while ent != None:
            s = ent.tablaFunciones.get(llave)
            if s != None:
                return s
            ent = ent.anterior
        return None

    def existeFuncion(self, llave):
        s = self.tablaFunciones.get(llave.lower())
        if s != None:
            return True
        return False

    def nuevaStruct(self, simbolo:Struct ):
        s = self.tablaStructs.get(simbolo.id.lower())
        if s == None:
            self.tablaStructs[simbolo.id.lower()] = simbolo

    def buscarStruct(self, llave):
        ent = self
        while ent != None:
            s = ent.tablaStructs.get(llave)
            if s != None:
                return s.parametros
            ent = ent.anterior
        return None

    

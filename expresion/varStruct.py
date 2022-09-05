
from expresion.expresion import expresion
from simbolo.ambito import ambito
import simbolo.listaerrores as errores

class varStruct(expresion):

    def __init__(self, fila, columna, id,buscador):
        self.fila = fila
        self.columna = columna
        self.id = id
        self.buscador = buscador

    def ejecutar(self,ambito:ambito):
        auxSimbolo = ambito.buscarsimbolo(self.id)
        if (auxSimbolo!=None):
            return auxSimbolo.valor[self.buscador]
        else:
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Variable no declarada")
    






from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.simbolo import simbolo

class Capacity(instrucciones):
    
    def __init__(self, fila, columna, id):
        self.fila = fila
        self.columna = columna
        self.id = id

    def ejecutar(self,ambito:ambito):
        auxSimbolo = ambito.buscarsimbolo(self.id)
        dimensiones= auxSimbolo.tipo["dimen"]
        if len(dimensiones)==1:
            return {"valor": dimensiones[0], "tipo": Tipo.ENTERO}
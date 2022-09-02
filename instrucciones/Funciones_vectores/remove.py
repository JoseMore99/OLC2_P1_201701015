from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.simbolo import simbolo

class Remove(instrucciones):
    
    def __init__(self, fila, columna, id,pocision):
        self.fila = fila
        self.columna = columna
        self.id = id
        self.pocision = pocision

    def ejecutar(self,ambito:ambito):
        auxSimbolo = ambito.buscarsimbolo(self.id)
        auxpos = self.pocision.ejecutar(ambito)
        dimensiones= auxSimbolo.tipo["dimen"]
        if len(dimensiones)==1:
            auxSimbolo.tipo["dimen"][0]-=1
            temp = auxSimbolo.valor.pop(auxpos["valor"])
            return temp
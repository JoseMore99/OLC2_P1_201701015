from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.simbolo import simbolo

class push(instrucciones):
    
    def __init__(self, fila, columna, id,valor):
        self.fila = fila
        self.columna = columna
        self.id = id
        self.valor = valor

    def ejecutar(self,ambito:ambito):
        auxSimbolo = ambito.buscarsimbolo(self.id)
        dimensiones= auxSimbolo.tipo["dimen"]
        if len(dimensiones)==1:
            auxSimbolo.tipo["dimen"][0]+=1
            auxSimbolo.valor.append(self.valor.ejecutar(ambito))
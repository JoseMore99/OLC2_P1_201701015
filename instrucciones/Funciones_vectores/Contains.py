
from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.simbolo import simbolo

class Contains(instrucciones):
    
    def __init__(self, fila, columna, id,valor):
        self.fila = fila
        self.columna = columna
        self.id = id
        self.valor = valor

    def ejecutar(self,ambito:ambito):
        auxSimbolo = ambito.buscarsimbolo(self.id)
        dimensiones= auxSimbolo.tipo["dimen"]
        if len(dimensiones)==1:
            if self.valor.ejecutar(ambito) in auxSimbolo.valor:
                return {"valor": True, "tipo": Tipo.BOOL}
            else:
                return {"valor": False, "tipo": Tipo.BOOL}
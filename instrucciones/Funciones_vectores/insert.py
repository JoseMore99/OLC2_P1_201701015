from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.simbolo import simbolo

class insert(instrucciones):
    
    def __init__(self, fila, columna, id,valor,pocision):
        self.fila = fila
        self.columna = columna
        self.id = id
        self.valor = valor
        self.pocision = pocision

    def ejecutar(self,ambito:ambito):
        auxSimbolo = ambito.buscarsimbolo(self.id)
        auxpos = self.pocision.ejecutar(ambito)
        dimensiones= auxSimbolo.tipo["dimen"]
        if len(dimensiones)==1:
            auxSimbolo.tipo["dimen"][0]+=1
            auxSimbolo.valor.insert(auxpos["valor"],self.valor.ejecutar(ambito))
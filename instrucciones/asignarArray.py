from wsgiref.validate import validator
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.simbolo import simbolo

class asignarArray(instrucciones):
    
    def __init__(self, fila, columna, id,pocisiones,valor):
        self.fila = fila
        self.columna = columna
        self.id = id
        self.pocisiones= pocisiones
        self.valor = valor

    def ejecutar(self,ambito:ambito):
        auxSimbolo = ambito.buscarsimbolo(self.id)
        dimensiones= auxSimbolo.tipo["dimen"]
        print(dimensiones)
        def getpos(i):
            aux = self.pocisiones[i].ejecutar(ambito)
            if i==0:
                return aux["valor"]
            return aux["valor"]+dimensiones[i]*getpos(i-1)
        auxSimbolo.valor[getpos(len(dimensiones)-1)]=self.valor.ejecutar(ambito)

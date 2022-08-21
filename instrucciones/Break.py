from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito

class Break(instrucciones):
    
    def __init__(self, fila, columna,valor=None):
        self.fila =fila
        self.columna = columna
        self.valor = valor
    
    
    def ejecutar(self,ambito:ambito):
        return{ "tipo":"201701015B","valor":self.valor,"fila":self.fila,"columna":self.columna}
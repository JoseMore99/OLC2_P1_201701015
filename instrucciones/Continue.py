from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito

class Continue(instrucciones):
    
    def __init__(self, fila, columna):
        self.fila =fila
        self.columna = columna
        
    
    def ejecutar(self,ambito:ambito):
        return{ "tipo":"201701015C","fila":self.fila,"columna":self.columna}
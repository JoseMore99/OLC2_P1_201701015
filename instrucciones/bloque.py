from instrucciones.instrucciones import instrucciones

class bloque(instrucciones):
    
    def __init__(self, fila, columna, instrucciones):
        self.fila =fila
        self.comlumna = columna
        self.instrucciones = instrucciones
        
    
    def ejecutar(self,ambito):
        for i in self.instrucciones:
            intruccion = i.ejecutar(ambito)


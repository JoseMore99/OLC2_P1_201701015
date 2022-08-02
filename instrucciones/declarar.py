from instrucciones.instrucciones import instrucciones

class declarar(instrucciones):
    
    def __init__(self, fila, columna,id,tipo, valor):
        self.fila =fila
        self.comlumna = columna
        self.id = id
        self.tipo = tipo
        self.valor = valor
        
    
    def ejecutar(self,ambito):
        pass
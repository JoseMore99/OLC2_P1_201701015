from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito

class If(instrucciones):
    
    def __init__(self, fila, columna,condicion,contenido,sino):
        self.fila =fila
        self.comlumna = columna
        self.condicion = condicion
        self.contenido = contenido
        self.sino = sino
        
    
    def ejecutar(self,ambito:ambito):
        auxcondi = self.condicion.ejecutar(ambito)
        if(auxcondi["tipo"]==Tipo.BOOL):
            if(auxcondi["valor"]):
                return self.contenido.ejecutar(ambito)
            else:
                if(self.sino!=None):
                    return self.sino.ejecutar(ambito)
        else:
            print("Error en Condicion del if")
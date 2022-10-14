from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol

class Continue(instrucciones):
    
    def __init__(self, fila, columna):
        self.fila =fila
        self.columna = columna
        
    
    def ejecutar(self,ambito:ambito):
        return{ "tipo":"201701015C","fila":self.fila,"columna":self.columna}
        
    def traducir(self,arbol:Arbol, tabla):
        if self.eContinua() != None:
            codigo = ""
            codigo += arbol.menosStackV(tabla.tamanio)
            codigo += arbol.goto(self.eContinua())

            return {'temporal': "", 'codigo': codigo}
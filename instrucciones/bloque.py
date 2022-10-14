from ast import Continue, Return
from tkinter.messagebox import NO
from instrucciones.Break import Break
from instrucciones.instrucciones import instrucciones
from simbolo.arbol import Arbol

class bloque(instrucciones):
    
    def __init__(self, fila, columna, instrucciones):
        self.fila =fila
        self.comlumna = columna
        self.instrucciones = instrucciones
        
    
    def ejecutar(self,ambito):
        for interar in self.instrucciones:
            intruccion = interar.ejecutar(ambito)
            if ( intruccion is not None):
                
                return intruccion

    def traducir(self,arbol:Arbol, tabla,condi={}):
        codigo = ""
        for interar in self.instrucciones:
            if "break" in condi:
                interar.eSetSalida(condi["break"])
                interar.eSetContinua(condi["continue"])
                interar.eSetReturn(condi["return"])
                interar.eSetTemporal(condi["temporal"])
            intruccion = interar.traducir(arbol,tabla)
            codigo += intruccion["codigo"]
        return {'codigo': codigo}


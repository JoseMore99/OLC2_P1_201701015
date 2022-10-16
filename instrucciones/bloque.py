from ast import Continue, Return
from tkinter.messagebox import NO
from expresion.Tipo import Tipo
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
        tipo = None
        for interar in self.instrucciones:
            if "break" in condi:
                interar.eSetSalida(condi["break"])
                interar.eSetContinua(condi["continue"])
                interar.eSetReturn(condi["return"])
                interar.eSetTemporal(condi["temporal"])
            intruccion = interar.traducir(arbol,tabla)
            codigo += intruccion["codigo"]
            if "tipo" in intruccion:
                tipo = intruccion["tipo"]
        return {'codigo': codigo ,'tipo':tipo}


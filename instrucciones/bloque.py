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

    def traducir(self,arbol:Arbol, tabla,condicion=""):
        codigo = ""
        for interar in self.instrucciones:
            # if isinstance(interar, Break):
            #     codigo += arbol.masStackV(tabla.tamanio)
            #     codigo += arbol.goto(condicion)
            # if isinstance(interar, Continue):
            #     pass
            # if isinstance(interar, Return):
            #     pass
            intruccion = interar.traducir(arbol,tabla)
            codigo += intruccion["codigo"]
        return {'codigo': codigo}


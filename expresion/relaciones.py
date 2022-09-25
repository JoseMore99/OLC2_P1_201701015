
from expresion.Tipo import Tipo
from expresion.TipoR import TipoR
from expresion.expresion import expresion
from simbolo.arbol import Arbol
import simbolo.listaerrores as errores
class relaciones(expresion):

    def __init__(self, fila, columna,izquierda,derecha, tiporel):
        self.fila = fila
        self.columna = columna
        self.izquierda=izquierda
        self.derecha=derecha
        self.tiporel = tiporel

    def ejecutar(self,ambito):
        valIz = self.izquierda.ejecutar(ambito)
        valDer = self.derecha.ejecutar(ambito)
        #print(str(valIz["tipo"])+"+"+str(valDer["tipo"]))
        if(valIz["tipo"]==valDer["tipo"]):
            if self.tiporel == TipoR.MENORQUE  : 
                return {"valor": valIz["valor"]<valDer["valor"], "tipo": Tipo.BOOL}
            elif self.tiporel == TipoR.MENORIGUAL :
                return {"valor": valIz["valor"]<=valDer["valor"], "tipo": Tipo.BOOL}
            elif self.tiporel == TipoR.MAYORQUE :
                return {"valor": valIz["valor"]>valDer["valor"], "tipo": Tipo.BOOL}
            elif self.tiporel == TipoR.MAYORIGUAL :
                return {"valor": valIz["valor"]>=valDer["valor"], "tipo": Tipo.BOOL}
            elif self.tiporel == TipoR.IGUAL :
                return {"valor": valIz["valor"]==valDer["valor"], "tipo": Tipo.BOOL}
            elif self.tiporel == TipoR.DIFERENTE :
                return {"valor": valIz["valor"]!=valDer["valor"], "tipo": Tipo.BOOL}
            elif self.tiporel == TipoR.AND :
                return {"valor": valIz["valor"] == valDer["valor"], "tipo": Tipo.BOOL}
            elif self.tiporel == TipoR.OR :
                return {"valor": valIz["valor"] or valDer["valor"], "tipo": Tipo.BOOL}
            elif self.tiporel == TipoR.NOT :
                return {"valor":not valIz["valor"], "tipo": Tipo.BOOL}
            
            
            else:
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Relacion invalida")
        else:
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
    def traducir(self,arbol:Arbol, tabla):
        pass
        

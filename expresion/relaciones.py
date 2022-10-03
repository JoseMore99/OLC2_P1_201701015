
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
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "tiporelinvalida")
        else:
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
    def traducir(self,arbol:Arbol, tabla):
        codigo = ""
        rel = ""
        temp = arbol.newTemp()
        lTrue = arbol.newLabel()
        lFalse = arbol.newLabel()
        izq = self.obtieneValorC3D(self.izquierda, arbol, tabla)
        der = self.obtieneValorC3D(self.derecha, arbol, tabla)
        self.tipo = Tipo.BOOL
        if self.tiporel== TipoR.IGUAL:
            rel = "=="
        elif self.tiporel== TipoR.DIFERENTE:
            rel = "!="
        elif self.tiporel== TipoR.MENORQUE:
            rel = "<"
        elif self.tiporel== TipoR.MENORIGUAL:
            rel = "<="
        elif self.tiporel== TipoR.MAYORQUE:
            rel = ">"
        elif self.tiporel== TipoR.MAYORIGUAL:
            rel = ">="
        else:
            return 'None'
        # print(izq, der)  # TODO ARREGLAR ESTO DE LOS TEMPORALES

        if 'temporal' in izq:
            if 'temporal' in der:
                codigo += arbol.getCond2(izq["temporal"],
                                         rel, der["temporal"], lTrue)
                codigo += arbol.assigTemp1(temp["temporal"], "0.0")
                codigo += arbol.goto(lFalse)
                codigo += arbol.getLabel(lTrue)
                codigo += arbol.assigTemp1(temp["temporal"], "1.0")
                codigo += arbol.getLabel(lFalse)
        elif 'heap' in izq:
            if 'heap' in der:
                codigo += arbol.getCond2(izq["heap"], rel, der["heap"], lTrue)
                codigo += arbol.assigTemp1(temp["temporal"], "0.0")
                codigo += arbol.goto(lFalse)
                codigo += arbol.getLabel(lTrue)
                codigo += arbol.assigTemp1(temp["temporal"], "1.0")
                codigo += arbol.getLabel(lFalse)
        codigo = izq["codigo"]+der["codigo"]+codigo

        '''
        if(op1 tiporelop2){goto L1};
        goto L2;
        L1:
        lVerdera
        L2:
        lFalsa
        '''
        return {'temporal': temp["temporal"], 'codigo': codigo}
    
    def obtieneValorC3D(self, operando, arbol, tabla):
        valor = operando.traducir(arbol, tabla)
        return valor
        


from expresion.expresion import expresion
import simbolo.listaerrores as errores
class aritmetica(expresion):

    def __init__(self, fila, columna,izquierda,derecha, tipoArit):
        self.fila = fila
        self.columna = columna
        self.izquierda=izquierda
        self.derecha=derecha
        self.tipoArit = tipoArit

    def ejecutar(self,ambito):
        valIz = self.izquierda.ejecutar(ambito)
        valDer = self.derecha.ejecutar(ambito)
        #print(str(valIz["tipo"])+"+"+str(valDer["tipo"]))
        if(valIz["tipo"]==valDer["tipo"]):
            if self.tipoArit == "+"  : 
                return {"valor": valIz["valor"]+valDer["valor"], "tipo": valIz["tipo"]}
            elif self.tipoArit == "-" :
                if(str(valIz["valor"]).isdigit and str(valDer["valor"]).isdigit):
                     return {"valor": valIz["valor"]-valDer["valor"], "tipo": valIz["tipo"]}
                else:
                    errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
            elif self.tipoArit == "*" :
                if(str(valIz["valor"]).isdigit and str(valDer["valor"]).isdigit):
                     return {"valor": valIz["valor"]*valDer["valor"], "tipo": valIz["tipo"]}
                else:
                    errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
            elif self.tipoArit == "/" : 
                if(str(valIz["valor"]).isdigit and str(valDer["valor"]).isdigit):
                    if (valDer["valor"]!=0):
                        return {"valor": valIz["valor"]/valDer["valor"], "tipo": valIz["tipo"]}
                    else:
                        errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Aritmetica incorrecta, Division por cero")
                else:
                    errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
            elif self.tipoArit == "%" : 
                if(str(valIz["valor"]).isdigit and str(valDer["valor"]).isdigit):
                     return {"valor": valIz["valor"]%valDer["valor"], "tipo": valIz["tipo"]}
                else:
                    errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
            elif self.tipoArit == "^" : 
                if(str(valIz["valor"]).isdigit and str(valDer["valor"]).isdigit):
                     return {"valor": valIz["valor"]**valDer["valor"], "tipo": valIz["tipo"]}
                else:
                    errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
            elif self.tipoArit == "r" : 
                #print("RAIIIIIIIIIIIIIIIIIIIIIIIZ")
                if(str(valIz["valor"]).isdigit and str(valDer["valor"]).isdigit):
                     return {"valor": valIz["valor"]**(0.5), "tipo": valIz["tipo"]}
                else:
                    errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
            elif self.tipoArit == "a" : 
                if(str(valIz["valor"]).isdigit and str(valDer["valor"]).isdigit):
                     return {"valor": abs(valIz["valor"]), "tipo": valIz["tipo"]}
                else:
                    errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
        else:
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
            
        

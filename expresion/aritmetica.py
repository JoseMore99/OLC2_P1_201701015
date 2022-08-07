
from expresion.expresion import expresion
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
                    print("error en la resta Aritmetica")
            elif self.tipoArit == "*" :
                if(str(valIz["valor"]).isdigit and str(valDer["valor"]).isdigit):
                     return {"valor": valIz["valor"]*valDer["valor"], "tipo": valIz["tipo"]}
                else:
                    print("error en la multiplicacion Aritmetica")
            elif self.tipoArit == "/" : 
                if(str(valIz["valor"]).isdigit and str(valDer["valor"]).isdigit):
                     return {"valor": valIz["valor"]/valDer["valor"], "tipo": valIz["tipo"]}
                else:
                    print("error en la division Aritmetica")
            elif self.tipoArit == "%" : 
                if(str(valIz["valor"]).isdigit and str(valDer["valor"]).isdigit):
                     return {"valor": valIz["valor"]%valDer["valor"], "tipo": valIz["tipo"]}
                else:
                    print("error en el modulo Aritmetica")
        else:
            print("error en la Aritmetica")
            
        

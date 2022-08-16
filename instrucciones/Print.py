from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones

consola =""
class Print(instrucciones):
    
    def __init__(self, fila, columna, valor, expresiones):
        self.fila =fila
        self.comlumna = columna
        self.valor = valor
        self.expresiones = expresiones
        
    
    def ejecutar(self,ambito):
        global consola
        aux = self.valor.ejecutar(ambito)
        if(aux!=None and aux["tipo"]==Tipo.STRING):
            if(self.expresiones==[]):
                consola += str(aux["valor"])+"\n"
            else:
                texto = str(aux["valor"])
                for i in self.expresiones:
                    temp = i.ejecutar(ambito)
                    if(temp!=None):
                        texto = texto.replace("{}",str(temp["valor"]),1)
                    else:
                        print("Error en replace del print")
                consola+=texto+"\n"
        else:
            print("Error en imprimir")
        #print(consola)

def vaciar():
    global consola
    consola=""
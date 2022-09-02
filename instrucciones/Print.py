from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones

consola =""
class Print(instrucciones):
    
    def __init__(self, fila, columna, valor, expresiones):
        self.fila =fila
        self.columna = columna
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
                        #print(temp)
                        if(isinstance(temp["valor"],list)):
                            contenido ="["
                            for j in temp["valor"]:
                                contenido+=str(j["valor"])+","
                            contenido+="]"
                            contenido= contenido.replace(",]","]")
                            texto = texto.replace("{:?}",contenido,1)
                        else:
                            texto = texto.replace("{}",str(temp["valor"]),1)
                        #print(temp["valor"],"-")
                    else:
                        print("Error en replace del print")
                consola+=texto+"\n"
        else:
            print("Error en imprimir")
        #print(consola)

def vaciar():
    global consola
    consola=""
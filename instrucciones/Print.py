from instrucciones.instrucciones import instrucciones

consola =""
class Print(instrucciones):
    
    def __init__(self, fila, columna, valor):
        self.fila =fila
        self.comlumna = columna
        self.valor = valor
        
    
    def ejecutar(self,ambito):
        global consola
        aux = self.valor.ejecutar(ambito)
        if(aux!=None):
            consola += str(aux["valor"])+"\n"
        #print(consola)

def vaciar():
    global consola
    consola=""
from instrucciones.instrucciones import instrucciones

consola =""
class Print(instrucciones):
    
    def __init__(self, fila, columna, valor):
        self.fila =fila
        self.comlumna = columna
        self.valor = valor
        
    
    def ejecutar(self):
        global consola
        aux = self.valor.ejecutar()
        consola += str(aux["valor"])+"\n"
        print(consola)
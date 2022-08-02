
from expresion.Tipo import Tipo
from expresion.expresion import expresion

class nativo(expresion):

    def __init__(self, fila, columna, tipo, valor):
        self.fila = fila
        self.columna = columna
        self.tipo = tipo
        self.valor = valor

    def ejecutar(self,ambito):
       
        if(self.tipo==Tipo.ENTERO):
            return {"valor": int(self.valor), "tipo": self.tipo}
        elif(self.tipo==Tipo.DECIMAL):
            return {"valor": float(self.valor), "tipo": self.tipo}
        elif(self.tipo==Tipo.BOOL):
            if(self.valor=="true"):
                return {"valor": True, "tipo": self.tipo}
            else:
                return {"valor": False, "tipo": self.tipo}
        elif(self.tipo==Tipo.CHAR):
            return {"valor": str(self.valor), "tipo": self.tipo}
        elif(self.tipo==Tipo.STRING):
            return {"valor": str(self.valor), "tipo": self.tipo}





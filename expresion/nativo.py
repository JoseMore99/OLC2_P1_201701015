
from expresion.Tipo import Tipo
from expresion.expresion import expresion
from simbolo.arbol import Arbol

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
    
    def traducir(self,arbol:Arbol,tabla):
        temp = self.valor
        if(self.tipo==Tipo.ENTERO):
            temp = float(self.valor)
        elif(self.tipo==Tipo.DECIMAL):
            temp = float(self.valor)
        elif(self.tipo==Tipo.BOOL):
            if(self.valor=="true"):
                temp = 1.0
            else:
                temp = 0.0
        elif(self.tipo==Tipo.CHAR):
            temp = float(ord(self.valor))
        elif(self.tipo==Tipo.STRING):
            return arbol.guardarStr(temp)
        return arbol.nuevoTemp(str(temp))





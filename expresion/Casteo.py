
from optparse import AmbiguousOptionError
from expresion.Tipo import Tipo
from expresion.expresion import expresion

class Casteo(expresion):

    def __init__(self, fila, columna,valor,tipo):
        self.fila = fila
        self.columna = columna
        self.tipo = tipo
        self.valor = valor

    def ejecutar(self,ambito):
        temp = self.valor.ejecutar(ambito)
        if(self.tipo==Tipo.ENTERO):
            return {"valor": int(temp["valor"]), "tipo": self.tipo}
        elif(self.tipo==Tipo.DECIMAL):
            return {"valor": float(temp["valor"]), "tipo": self.tipo}
        elif(self.tipo==Tipo.BOOL):
            if(temp["valor"]=="true"):
                return {"valor": True, "tipo": self.tipo}
            else:
                return {"valor": False, "tipo": self.tipo}
        elif(self.tipo==Tipo.CHAR):
            return {"valor": str(temp["valor"]), "tipo": self.tipo}
        elif(self.tipo==Tipo.STRING):
            return {"valor": str(temp["valor"]), "tipo": self.tipo}



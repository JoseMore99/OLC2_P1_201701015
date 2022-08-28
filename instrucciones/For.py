from expresion.Tipo import Tipo
from expresion.nativo import nativo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.simbolo import simbolo

class For(instrucciones):
    
    def __init__(self, fila, columna,variable,varcambio,varcambio2,contenido):
        self.fila =fila
        self.comlumna = columna
        self.variable = variable
        self.varcambio = varcambio
        self.varcambio2 = varcambio2
        self.contenido = contenido
        
    
    def ejecutar(self,Ambito:ambito):
        auxcondi = self.varcambio.ejecutar(Ambito)
        if isinstance(auxcondi["tipo"],dict) :
            entornoAnt= ambito(Ambito)
            self.variable.valor=nativo(0, 0,auxcondi["valor"][0]["tipo"],auxcondi["valor"][0]["valor"])
            self.variable.ejecutar(entornoAnt)
            for i in auxcondi["valor"]:
                entornoAnt.editarSimbolo(self.variable.id,simbolo(i["tipo"],self.variable.id,i["valor"],True))
                respuesta = self.contenido.ejecutar(entornoAnt)
                if(respuesta is not None):
                    if(respuesta["tipo"]=="201701015B"):
                        break
                    if(respuesta["tipo"]=="201701015C"):
                        continue
                    if(respuesta["tipo"]=="201701015R"):
                        if respuesta["valor"] is not None:
                            return respuesta
                        return
                    #return respuesta
            #return respuesta
        else:
            auxcondi = self.varcambio.ejecutar(Ambito)
            auxcondi2 = self.varcambio2.ejecutar(Ambito)
            if(auxcondi["tipo"]==Tipo.ENTERO and auxcondi2["tipo"]==Tipo.ENTERO):
                entornoAnt= ambito(Ambito)
                self.variable.valor=nativo(0, 0,auxcondi["tipo"],auxcondi["valor"])
                self.variable.ejecutar(entornoAnt)
                for i in range(auxcondi["valor"],auxcondi2["valor"]):
                    simbolonew = simbolo(Tipo.ENTERO,self.variable.id,i,True)
                    entornoAnt.editarSimbolo(self.variable.id,simbolonew)
                    respuesta = self.contenido.ejecutar(entornoAnt)
                    if(respuesta is not None):
                        if(respuesta["tipo"]=="201701015B"):
                            break
                        if(respuesta["tipo"]=="201701015C"):
                            continue
                        if(respuesta["tipo"]=="201701015R"):
                            return respuesta
            else:
                print("Error en for")
from expresion.Tipo import Tipo
from expresion.nativo import nativo
from instrucciones.declarar import declarar
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol
from simbolo.listasimboloc3d import listasimboloc3d
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
            #print(auxcondi)
            #print(self.varcambio2)
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
                import simbolo.listaerrores as errores
                errores.Errores.nuevoError(self.fila,self.comlumna, 'Semantico', "Expresiones en for no admitidas")
    
    def traducir(self,arbol:Arbol, tabla):
        tip = Tipo.ENTERO
        codigo = ""
        tempControl = arbol.newTemp()
        lControl = arbol.newLabel()

        lFalso = arbol.newLabel()
        lSalida = arbol.newLabel()
        nuevaTabla = listasimboloc3d(tabla)
        nuevaTabla.setNombre('For')
        arbol.tamReturn += tabla.tamanio
        codigo += arbol.masStackV(tabla.tamanio)
        dec = self.variable
        dec.tipo = self.varcambio.tipo
        nuevaDec = dec.traducir(arbol, nuevaTabla)
        if self.varcambio2 != self.varcambio:
            val1 = self.varcambio.traducir(arbol, nuevaTabla)
            val2 = self.varcambio2.traducir(arbol, nuevaTabla)
            codigo += val1["codigo"]
            codigo += val2["codigo"]
            #print(val1, val2)
            codigo += arbol.assigTemp1(
                tempControl["temporal"], val1["temporal"])
            codigo += arbol.getLabel(lControl)
            codigo += arbol.getCond2(tempControl["temporal"],">=", val2["temporal"], lSalida)
            codigo += arbol.assigStackN("P", tempControl["temporal"])
            codigo += arbol.goto(lFalso)
            codigo += arbol.getLabel(lFalso)
            # Instrucciones
            transferencia = {"break":lSalida,"continue":lControl,"return":self.eReturn(),"temporal":self.eTemporal()}
            aux = self.contenido.traducir(arbol, nuevaTabla,condi=transferencia)

            arbol.tamReturn -= tabla.tamanio
            codigo += aux["codigo"]
            codigo += arbol.assigTemp2(tempControl["temporal"], tempControl["temporal"], "+", "1.0")
            codigo += arbol.goto(lControl)
        codigo += arbol.getLabel(lSalida)
        arbol.tamReturn -= tabla.tamanio
        codigo += arbol.menosStackV(tabla.tamanio)
        return {'temporal': '', 'codigo': codigo, 'tipo': tip}


'''codigo = ""
        tempC = arbol.newTemp()
        tempF = arbol.newTemp()
        lControl = arbol.newLabel()
        lFalso = arbol.newLabel()
        nuevaTabla = listasimboloc3d(tabla)
        nuevaTabla.setNombre('For')
        codigo += arbol.masStackV(tabla.tamanio)
        
        if self.varcambio != self.varcambio2:
            temp1 = self.varcambio.traducir(arbol,tabla)
            codigo+= temp1["codigo"]
            codigo += arbol.assigTemp1(tempC,temp1["temporal"])
            temp2 = self.varcambio2.traducir(arbol,tabla)
            codigo+= temp2["codigo"]
            codigo += arbol.assigTemp1(tempF,temp2["temporal"])
            codigo += arbol.getLabel(lControl)
            transferencia = {"break":lFalso,"continue":lControl,"return":self.eReturn(),"temporal":self.eTemporal()}
            aux = self.contenido.traducir(arbol, nuevaTabla,condi=transferencia)
            codigo += aux["codigo"]
            codigo += arbol.getCond2(tempC["temporal"], "==",tempF["temporal"], lFalso)
            codigo += arbol.assigTemp2(tempC["temporal"],tempC["temporal"], " + ", "1.0")
            codigo += arbol.goto(lControl)
            codigo += arbol.getLabel(lFalso)

        return {'codigo': codigo}'''
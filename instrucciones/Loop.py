from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol
from simbolo.listasimboloc3d import listasimboloc3d

class Loop(instrucciones):
    
    def __init__(self, fila, columna,contenido):
        self.fila =fila
        self.comlumna = columna
        self.contenido = contenido
        
    
    def ejecutar(self,ambito:ambito):
        while(True):
            respuesta = self.contenido.ejecutar(ambito)
            if(respuesta is not None):
                if(respuesta["tipo"]=="201701015B"):
                    break
                if(respuesta["tipo"]=="201701015C"):
                    continue
                if(respuesta["tipo"]=="201701015R"):
                        return respuesta
    def traducir(self,arbol:Arbol, tabla):
        codigo = ""
        lControl = arbol.newLabel()
        lVerdadero = arbol.newLabel()
        lFalso = arbol.newLabel()
        nuevaTabla = listasimboloc3d(tabla)
        nuevaTabla.setNombre('Loop')
        arbol.tamReturn += tabla.tamanio
        codigo += arbol.masStackV(tabla.tamanio)
        codigo += arbol.getLabel(lControl)
        codigo += arbol.getCond2("1.0", "==", "1.0", lVerdadero)
        codigo += arbol.goto(lFalso)
        codigo += arbol.getLabel(lVerdadero)
        aux = ""
        tip = Tipo.ENTERO
        transferencia = {"break":lFalso,"continue":lControl,"return":self.eReturn(),"temporal":self.eTemporal()}
        aux = self.contenido.traducir(arbol, nuevaTabla,condi=transferencia)

        arbol.tamReturn -= tabla.tamanio
        codigo += aux["codigo"]
        codigo += arbol.goto(lControl)
        codigo += arbol.getLabel(lFalso)
        '''
        LC:
        if a>b goto LV
        goto LF
        LV: 
        instrucciones
        goto LC
        LF:
        '''
        codigo += arbol.menosStackV(tabla.tamanio)
        return {'temporal': "", 'codigo': codigo, 'tipo': tip}
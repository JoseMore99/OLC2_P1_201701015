from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol
from simbolo.listasimboloc3d import listasimboloc3d

class While(instrucciones):
    
    def __init__(self, fila, columna,condicion,contenido):
        self.fila =fila
        self.comlumna = columna
        self.condicion = condicion
        self.contenido = contenido
        
    
    def ejecutar(self,ambito:ambito):
        auxcondi = self.condicion.ejecutar(ambito)
        if(auxcondi["tipo"]==Tipo.BOOL):
            while(auxcondi["valor"]):
                respuesta = self.contenido.ejecutar(ambito)
                if(respuesta is not None):
                    if(respuesta["tipo"]=="201701015B"):
                        break
                    if(respuesta["tipo"]=="201701015C"):
                        continue
                    if(respuesta["tipo"]=="201701015R"):
                            return respuesta
                auxcondi = self.condicion.ejecutar(ambito)
            #return respuesta
        else:
            import simbolo.listaerrores as errores
            errores.Errores.nuevoError(self.fila,self.comlumna, 'Semantico', "condicion incorrecta en while")

    def traducir(self,arbol:Arbol, tabla):
        codigo = ""
        lControl = arbol.newLabel()
        lVerdadero = arbol.newLabel()
        lFalso = arbol.newLabel()
        nuevaTabla = listasimboloc3d(tabla)
        nuevaTabla.setNombre('While')
        arbol.tamReturn += tabla.tamanio
        codigo += arbol.masStackV(tabla.tamanio)
        codigo += arbol.getLabel(lControl)
        cond = self.condicion.traducir(arbol, nuevaTabla)
        if self.condicion.tipo == Tipo.BOOL:
            codigo += cond["codigo"]
            codigo += arbol.getCond2(cond["temporal"], "==", "1.0", lVerdadero)
            codigo += arbol.goto(lFalso)
            codigo += arbol.getLabel(lVerdadero)
            aux = ""
            tip = Tipo.ENTERO
            aux = self.contenido.traducir(arbol, tabla)

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
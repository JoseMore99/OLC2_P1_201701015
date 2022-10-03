from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol
from simbolo.listasimboloc3d import listasimboloc3d

class If(instrucciones):
    
    def __init__(self, fila, columna,condicion,contenido,sino):
        self.fila =fila
        self.comlumna = columna
        self.condicion = condicion
        self.contenido = contenido
        self.sino = sino
        
    
    def ejecutar(self,ambito:ambito):
        auxcondi = self.condicion.ejecutar(ambito)
        if(auxcondi["tipo"]==Tipo.BOOL):
            if(auxcondi["valor"]):
                return self.contenido.ejecutar(ambito)
            else:
                if(self.sino!=None):
                    return self.sino.ejecutar(ambito)
        else:
            import simbolo.listaerrores as errores
            errores.Errores.nuevoError(self.fila,self.comlumna, 'Semantico', "Error en condicion if")
            
    def traducir(self,arbol:Arbol, tabla):
        codigo = ""
        lFalsa1 = arbol.newLabel()
        lSalida = arbol.newLabel()
        val = self.condicion.traducir(arbol, tabla)
        # print(self.eTemporal())
        if self.condicion.tipo != Tipo.BOOL:
            import simbolo.listaerrores as errores
            errores.Errores.nuevoError(self.fila,self.comlumna, 'Semantico', "Error en condicion if")
        lVerdadera = arbol.newLabel()
        '''
    if (a>b) goto Lv
    goto lF
    Lv:
    instrucciones true
    goto Ls
    Lf:
    instrucciones else
    goto Ls
    goto Ls
    Ls
    '''

        codigo += val["codigo"]
        codigo += arbol.getCond2(val["temporal"], "==", "1.0", lVerdadera)
        codigo += arbol.goto(lFalsa1)
        codigo += arbol.getLabel(lVerdadera)
        nuevaTabla = listasimboloc3d(tabla)
        arbol.tamReturn += tabla.getTamanio()
        codigo += arbol.masStackV(tabla.getTamanio())

        aux = self.contenido.traducir(arbol, tabla)
        tip = Tipo.ENTERO
        
        codigo += aux["codigo"]
        arbol.tamReturn -= tabla.tamanio
        codigo += arbol.menosStackV(tabla.tamanio)
        codigo += arbol.goto(lSalida)
        codigo += arbol.getLabel(lFalsa1)

        if(self.sino!=None):
            aux2 = self.sino.traducir(arbol, tabla)
            codigo += aux2["codigo"]
            codigo += arbol.goto(lSalida)
        codigo += arbol.getLabel(lSalida)
        return {'temporal': '', 'codigo': codigo, 'tipo': tip}
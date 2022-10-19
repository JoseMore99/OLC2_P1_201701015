from __future__ import barry_as_FLUFL
from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol
from simbolo.listasimboloc3d import listasimboloc3d

class Match(instrucciones):
    
    def __init__(self, fila, columna,condicion,coincidencias):
        self.fila =fila
        self.comlumna = columna
        self.condicion = condicion
        self.coincidencias = coincidencias
        
    
    def ejecutar(self,ambito:ambito):
        auxcondi = self.condicion.ejecutar(ambito)
        bul=True
        for i in self.coincidencias:
            for j in i.listaval:
                try:
                    tempcondi = j.ejecutar(ambito)
                except:
                    if(j=='_' and bul):
                        aux = i.ejecutar(ambito)
                        if aux is not None:
                            return aux
                if(auxcondi["valor"]==tempcondi["valor"] and auxcondi["tipo"]==tempcondi["tipo"] ):
                    bul=False
                    print(auxcondi)
                    print(tempcondi)
                    aux = i.ejecutar(ambito)
                    if aux is not None:
                        return aux
            if not bul:
                break
    def traducir(self,arbol:Arbol, tabla):
        codigo = ""
        lSalida = arbol.newLabel()
        val = self.condicion.traducir(arbol, tabla)
        # print(self.eTemporal())
        codigo += val["codigo"]
        for i in self.coincidencias:
            lVerdadera = arbol.newLabel()
            lFalsa1 = arbol.newLabel()
            for j in i.listaval:
                try:
                    comparador = j.traducir(arbol, tabla)
                    codigo += comparador["codigo"]
                    codigo += arbol.getCond2(val["temporal"], "==",comparador["temporal"], lVerdadera)
                except:
                    codigo += arbol.getCond1("1.0", lVerdadera)
            codigo += arbol.goto(lFalsa1)
            codigo += arbol.getLabel(lVerdadera)
            nuevaTabla = listasimboloc3d(tabla)
            arbol.tamReturn += tabla.getTamanio()
            codigo += arbol.masStackV(tabla.getTamanio())
            try:
                transferencia = {"break":self.eSalida(),"continue":self.eContinua(),"return":self.eReturn(),"temporal":self.eTemporal()}
            except:
                transferencia={}
            aux = i.contenido.traducir(arbol, nuevaTabla,condi=transferencia)
            tip = Tipo.ENTERO
            
            codigo += aux["codigo"]
            arbol.tamReturn -= tabla.tamanio
            codigo += arbol.menosStackV(tabla.tamanio)
            codigo += arbol.goto(lSalida)
            codigo += arbol.getLabel(lFalsa1)

        codigo += arbol.getLabel(lSalida)
        return {'temporal': '', 'codigo': codigo, 'tipo': tip}
                   
                
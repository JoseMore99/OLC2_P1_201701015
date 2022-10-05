from expresion.Tipo import Tipo
from instrucciones.declarar import declarar
from instrucciones.instrucciones import instrucciones
from simbolo.arbol import Arbol

class funcion(instrucciones):
    
    def __init__(self, fila, columna,id,tipo, contenido,parametros):
        self.fila =fila
        self.columna = columna
        self.id = id
        self.tipo = tipo
        self.contenido = contenido
        self.parametros=parametros
        
    
    def ejecutar(self,ambito):
        ambito.nuevaFuncion(self)
    
    def traducir(self,arbol:Arbol, tabla):
        codigo = ""
        aux = ""
        lSalida = arbol.newLabel()
        tabla.masTamanio()
        codigo += "void " + self.id+"() {\n"
        nRetorno = arbol.newTemp()
        codigo += arbol.assigTemp1(nRetorno["temporal"], "P")
        for nuevoVal in self.parametros:
            if isinstance(nuevoVal["tipato"], str):
                # Se realiza como un struct
                tmpsNoUsados = arbol.getTempNoUsados()
                dec = declarar( self.fila,self.columna, nuevoVal["identificador"],Tipo.STRUCT, None,True)
                nuevaDec = dec.traducir(arbol, tabla)
                arbol.setTempNoUsados(tmpsNoUsados)
                # codigo += nuevaDec["codigo"]
            else:
                if nuevoVal["tipato"] == None:
                    nuevoVal["tipato"] = Tipo.ENTERO
                tmpsNoUsados = arbol.getTempNoUsados()
                dec = declarar(self.fila,self.columna, nuevoVal["identificador"],nuevoVal["tipato"], None, True)
                nuevaDec = dec.traducir(arbol, tabla)
                arbol.setTempNoUsados(tmpsNoUsados)
        aux = self.contenido.traducir(arbol, tabla)
        codigo += aux
        codigo += arbol.goto(lSalida)
        codigo += arbol.getLabel(lSalida)
        codigo += "return;\n}\n"
        arbol.tamReturn = 0
        # print(self.tipo)
        arbol.getFunciones().append(self)
        return {'codigo': codigo}


from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol
from simbolo.simbolo import simbolo

class Len(instrucciones):
    
    def __init__(self, fila, columna, id):
        self.fila = fila
        self.columna = columna
        self.id = id

    def ejecutar(self,ambito:ambito):
        if (isinstance(self.id,str)):
            auxSimbolo = ambito.buscarsimbolo(self.id)
            dimensiones= auxSimbolo.tipo["dimen"]
            return {"valor": dimensiones[0], "tipo": Tipo.ENTERO}
        else:
            auxSimbolo = self.id.ejecutar(ambito)
            #print("+++++++++++++")
            #print(auxSimbolo)
            longitud=len(auxSimbolo["valor"])
            #print("Longitud {}".format(longitud))
            return {"valor":longitud, "tipo": Tipo.ENTERO}
    def traducir(self,arbol:Arbol, tabla):
        codigo=""
        auxiliar = tabla.getVariableEntorno(self.id) 
        if auxiliar != None:
            retorno = auxiliar.getArreglo()
            
            if len(auxiliar.getDimensiones())==1:
                auxiliar.getDimensiones()[0]-=1
                retorno.pop(self.pocision.valor)
                if auxiliar.getTipo()==Tipo.ARRAY:
                    auxiliar.setTipo(self.valor.tipo)
            

            val = arbol.guardarArreglo(retorno)

            codigo +=val["codigo"]
            
            tVar = arbol.newTemp()
            tStck = arbol.newTemp()
            codigo += arbol.assigTemp1(tVar["temporal"], val["heap"])
            codigo += arbol.assigTemp2(tStck["temporal"],"P", "+", tabla.getTamanio())
            codigo += arbol.assigStackN(tStck["temporal"],tVar["temporal"])
            #Actualiza la ubicacion del vector
            auxiliar.setUbicacion(tabla.getTamanio())
            # else: guardar en heap y despues la referencia en stack
        else:
            import simbolo.listaerrores as errores
            errores.Errores.nuevoError(self.fila,self.comlumna, 'Semantico', "Variable no encontrada")

        #print("aquiiiiiii")
        #print(tabla.getTamanio())
        return {'codigo': codigo}
            
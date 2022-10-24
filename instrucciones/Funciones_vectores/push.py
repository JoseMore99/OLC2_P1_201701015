from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol
from simbolo.simbolo import simbolo
from simbolo.simboloc3d import simboloc3d

class push(instrucciones):
    
    def __init__(self, fila, columna, id,valor):
        self.fila = fila
        self.columna = columna
        self.id = id
        self.valor = valor

    def ejecutar(self,ambito:ambito):
        auxSimbolo = ambito.buscarsimbolo(self.id)
        dimensiones= auxSimbolo.tipo["dimen"]
        #print(self.valor)
        if(isinstance(self.valor,list)):

            try:
                auxSimbolo.tipo["dimen"][1]=len(self.valor)
                auxSimbolo.tipo["dimen"][0]+=1
            except:
                auxSimbolo.tipo["dimen"].append(len(self.valor))
            #print(auxSimbolo.tipo["dimen"][0])
            #print(auxSimbolo.tipo["dimen"][1])
            for val in self.valor:
                auxSimbolo.valor.append(val.ejecutar(ambito))
        if len(dimensiones)==1:
            auxSimbolo.tipo["dimen"][0]+=1
            auxSimbolo.valor.append(self.valor.ejecutar(ambito))
            
    def traducir(self,arbol:Arbol, tabla):
        codigo=""
        auxiliar = tabla.getVariableEntorno(self.id) 
        if auxiliar != None:
            retorno = auxiliar.getArreglo()
            if(isinstance(self.valor,list)):
                try:
                    auxiliar.getDimensiones()[1]=len(self.valor)
                    auxiliar.getDimensiones()[0]+=1
                except:
                    auxiliar.getDimensiones().append(len(self.valor))
                for val in self.valor:
                    retorno.append(val.valor)
                    if auxiliar.getTipo()==Tipo.ARRAY:
                        auxiliar.setTipo(val.tipo)
            if len(auxiliar.getDimensiones())==1:
                auxiliar.getDimensiones()[0]+=1
                retorno.append(self.valor.valor)
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

    def recorrer(self,array,ambito,tipo=None):
        temp = []
        for i in array:
            if(isinstance(i,list)):
                t=self.recorrer(i,ambito)
                temp.extend(t)
            else: 
                try:
                    self.tipo=i["tipo"]
                    temp.extend(i)
                except:
                    temp.append(i.ejecutar(ambito))
        #print(temp)
        return temp
    
    def recorrerC3D(self,array):
        temp = []
        for i in array:
            if(isinstance(i,list)):
                t=self.recorrerC3D(i)

                temp.extend(t)
            else: 
                try:
                    self.tipo=i.tipo
                    temp.extend(i)
                except:
                    temp.append(i.valor)
        #print(temp)
        return temp

    def ObtenerDimen(self,array):
        i= array
        if(isinstance(i,list)):
            self.dimensiones.append(len(i))
            self.ObtenerDimen(i[0])
        else:
            return 

from expresion.Tipo import Tipo
from expresion.expresion import expresion
from instrucciones.declarar import declarar
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol
from simbolo.listasimboloc3d import listasimboloc3d
import simbolo.listasimbolos as simbolo

class llamarfunc(instrucciones):

    def __init__(self, fila, columna, id,parametros):
        self.fila = fila
        self.columna = columna
        self.id = id
        self.parametros = parametros

    def ejecutar(self,Ambito:ambito):
        auxfuncion = Ambito.buscarFuncion(self.id)
        print("funcion "+self.id)
        referencias ={}
        if (auxfuncion!=None):
            if(len(self.parametros)==len(auxfuncion.parametros)):
                entornoAnt= ambito(Ambito)
                for p in range(len(self.parametros)):
                    if ( isinstance(self.parametros[p],str) or isinstance(auxfuncion.parametros[p],str)):
                        #print(self.parametros[p])
                        #print(auxfuncion.parametros[p])
                        auxfunc = Ambito.buscarsimbolo(self.parametros[p])
                        referencias[auxfuncion.parametros[p]]=auxfunc.nombre
                        auxfunc.nombre = auxfuncion.parametros[p]
                        entornoAnt.nuevosimbolo(auxfunc)
                        simbolo.Simbolos.nuevoSimbolo({"fila":auxfunc.fila,"columna":auxfunc.columna,"id":auxfunc.nombre,"TS":"Arreglo","TD":str(auxfunc.tipo["tipo"]),"ambito":self.id})
                    else:
                        auxpara = self.parametros[p].ejecutar(Ambito)
                        auxfunc = auxfuncion.parametros[p]
                        if (auxpara["tipo"]==auxfunc.tipo):
                            auxfunc.valor = self.parametros[p]
                            auxfunc.ejecutar(entornoAnt)
                            simbolo.Simbolos.nuevoSimbolo({"fila":auxfunc.fila,"columna":auxfunc.comlumna,"id":auxfunc.id,"TS":"Variable","TD":auxfunc.tipo,"ambito":self.id})
                        else:
                            import simbolo.listaerrores as errores
                            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Asignacion de parametros incorrecta en funcion"+self.id)
                respuesta=auxfuncion.contenido.ejecutar(entornoAnt)
                #ACTUALIZANDO NOMBRE DE VECTOR
                
                for i in list(referencias.keys()):
                    auxfunc = entornoAnt.buscarsimbolo(i)
                    Ambito.editarSimbolo(referencias[i],auxfunc)

                if(respuesta is not None):
                    if(respuesta["tipo"]=="201701015B"):
                        import simbolo.listaerrores as errores
                        errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Break incorrecto en de funcion "+self.id)
                    if(respuesta["tipo"]=="201701015C"):
                        import simbolo.listaerrores as errores
                        errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Continue incorrecto en de funcion "+self.id)
                    if(respuesta["tipo"]=="201701015R"):
                            #print(respuesta["valor"].ejecutar(entornoAnt))
                            if  respuesta["valor"] is not None:
                                return respuesta["valor"].ejecutar(entornoAnt)
                            else:
                                return
            else:
                import simbolo.listaerrores as errores
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Error el parametros de funcion"+self.id)
        else:
            import simbolo.listaerrores as errores
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Funcion no declarada")
    
    def traducir(self,arbol:Arbol, tabla):
        codigo = ""
        #print(arbol.getFunciones())
        funcion = arbol.getFuncion(self.id)
        if funcion != None:
            if len(funcion.parametros) == len(self.parametros):
                nuevaTabla = listasimboloc3d(tabla)
                codigo += arbol.masStackV(tabla.tamanio)
                iterador = 0
                nuevaTabla.masTamanio()
                varTemps = arbol.getTempNoUsados()
                nuevoTemp = arbol.newTemp()
                codigo += arbol.assigTemp1(nuevoTemp["temporal"], "P")
                #print(varTemps)
                for t in varTemps:
                    #print(t)
                    codigo += arbol.masStackV(1)
                    codigo += "stack[(int){}] = {};\n".format(nuevoTemp["temporal"], t)

                    codigo += arbol.assigTemp2(nuevoTemp["temporal"], nuevoTemp["temporal"], "+", "1.0")

                nuevaTabla.getAnterior().setTamanio(
                    nuevaTabla.getAnterior().getTamanio()+len(varTemps))
                for nuevoVal in self.parametros:
                    val = nuevoVal.traducir(arbol, nuevaTabla)
                    if isinstance(funcion.parametros[iterador].tipo, str):
                        # Se realiza como un struct
                        nuevaDec = funcion.parametros[iterador].traducir(arbol, nuevaTabla)
                        codigo += nuevaDec["codigo"]

                        var = nuevaTabla.getVariable(
                            funcion.parametros[iterador].id)
                        if var != None:
                            # if var.tipo != nuevoVal.tipo:
                            #     return Error("Semantico", "Tipo de dato diferente", self.fila, self.columna)
                            # else:
                            var.setValor(val)
                            nuevaTabla.setNombre(funcion.id)
                        else:
                            import simbolo.listaerrores as errores
                            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Error el parametros de funcion"+self.id)
                    else:
                        funcion.parametros[iterador].tipo = nuevoVal.tipo
                        funcion.parametros[iterador].valor = nuevoVal
                        nuevaDec = funcion.parametros[iterador].traducir(arbol, nuevaTabla)
                        print(funcion.parametros[iterador])
                        print(nuevaDec["codigo"])
                        codigo += nuevaDec["codigo"]
                    iterador = iterador+1

                codigo += self.id+"();\n"
                aux2 = ""

                nuevaTabla.getAnterior().setTamanio(nuevaTabla.getAnterior().getTamanio()-len(varTemps))
                for t in reversed(varTemps):
                    aux2 += arbol.menosStackV(1)
                    aux2 += "{} = stack[(int){}];\n".format(t, "P")
                nuevoTemp = arbol.newTemp()
                codigo += arbol.assigTemp1(nuevoTemp["temporal"], "P")

                # TODO hacer un metodo que obtenga los temporales usados antes de que llamen una funcion
                # print(arbol.getTempNoUsados())
                tempRetorno = arbol.newTemp()
                codigo += arbol.getStack(tempRetorno["temporal"],
                                         nuevoTemp["temporal"])
                codigo += aux2
                codigo += arbol.menosStackV(tabla.tamanio)
                self.tipo = funcion.tipo
                print(self.tipo)
                return {'heap': tempRetorno["temporal"], 'temporal': tempRetorno["temporal"], 'codigo': codigo}
            else:
                import simbolo.listaerrores as errores
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Error el parametros de funcion"+self.id)
        else:
            import simbolo.listaerrores as errores
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Funcion no encontrada "+self.id)
            return{"codigo":""}
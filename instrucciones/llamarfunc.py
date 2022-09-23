
from expresion.expresion import expresion
from simbolo.ambito import ambito
import simbolo.listasimbolos as simbolo

class llamarfunc(expresion):

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
                            return respuesta["valor"].ejecutar(entornoAnt)
            else:
                import simbolo.listaerrores as errores
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Error el parametros de funcion"+self.id)
        else:
            import simbolo.listaerrores as errores
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Funcion no declarada")
    

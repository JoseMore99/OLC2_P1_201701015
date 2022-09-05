from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.simbolo import simbolo

class declararStruct(instrucciones):
    
    def __init__(self, fila, columna,id,tipo, valor,mutabilidad,idstruct):
        self.fila =fila
        self.comlumna = columna
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.mutabilidad= mutabilidad
        self.idstruct = idstruct

        
    
    def ejecutar(self,ambito:ambito):
        if ambito.existesimbolo(self.id):
            import simbolo.listaerrores as errores
            errores.Errores.nuevoError(self.fila,self.comlumna, 'Semantico', 'variable declarada dos veces')
        else:
            buscador = ambito.buscarStruct(self.idstruct)
            resultado={}
            print(buscador)
            for i in buscador:
                for j in self.valor:
                    if(j["nombre"] ==i["nombre"]):
                        print(j)
                        aux=j["valor"].ejecutar(ambito) 
                        resultado[i["nombre"]]=aux
            simboloNew= simbolo(self.tipo,self.id,resultado,self.mutabilidad,self.fila,self.comlumna)
            ambito.nuevosimbolo(simboloNew)
'''s = {"s":54}
print(s["s"]+2)'''
from __future__ import barry_as_FLUFL
from contextlib import ContextDecorator
from xml.etree.ElementTree import TreeBuilder


def recorrer(array):
    temp = []
    for i in array:
        if(isinstance(i,list)):
            t=recorrer(i)
            temp.extend(t)
        else: 
            try:
                temp.extend(i)
            except:
                temp.append(i)
    #print(temp)
    return temp


'''x = "o o {} o o"
print(x)
print(x.count("{}"))
x=x.replace("o","0",1)
x=x.replace("o","1",1)
x=x.replace("o","2",1)
x=x.replace("o","3",1)
x=x.replace("o","4",1)
x=x.replace("o","5",1)
print(x)
for i in range(5):
    print(i)'''

'''x = 0
t = "aknd"
r=[1,2,3,4]
print(isinstance(list(t),list))
print(list(t))'''
z=[[[1,2,3,4],[5,6,7,8]],[[9,10,11,11],[12,13,14,15]]]
dimensiones =[]
pocisiones =[0,1,0]
pos = pocisiones
temporal=[]
'''
dimensiones.append(len(z))
for i in pocisiones:
    if(len(temporal)==0):
        temporal=z[i]
        dimensiones.append(len(temporal))
    else:
        temporal=temporal[i]
        try:
            dimensiones.append(len(temporal))
        except: pass
for indice, valor in enumerate(z):
	print(f'El valor de la posición {indice} es {valor}')
print(dimensiones)
print(pocisiones)
print(pos)
def getpos(i):
    if i==0:
        return pos[i]
    return pos[i]+dimensiones[i]*getpos(i-1)
cocal=[0,0]
cocal.append(0)

def getpos2(i):
    if i==0:
        return cocal[i]
    return cocal[i]+dimensiones[i]*getpos2(i-1)
    
vectorfial=recorrer(z)
print(z)
print(temporal)

medida = dimensiones[-1]
nemo = getpos2(len(dimensiones)-1)
print("nemo"+str(nemo))
print(vectorfial[nemo:nemo+medida])
    
    

print("--------")
print(getpos(len(dimensiones)-1))
print(vectorfial)
print(vectorfial[getpos(len(dimensiones)-1)])
print("--------------")
g={"0":{"0":{"0":"1","1":"12","2":"13"},"1":{"0":"1","1":"2","2":"3"}},"1":{"0":{"0":"21","1":"22","2":"23"},"1":{"0":"31","1":"32","2":"33"}}}
t=[0,0,0]
print(t[::len(t)-1])
aux = g
print(g)
for i in range(len(t)-1):
    aux = aux[str(t[i])]


print(aux)
aux[str(len(t)-1)] = "777"
print(g)

oiu=[]
oiu.append({"2":"3"})
oiu.append({"1":"4"})
oiu.append({"4":"2"})
oiu.append({"5":"1"})
dicti= {}
print(isinstance(dicti,dict))

dictadura = {"0":"01","1":"11","2":"21","3":"31"}
retorno = dictadura.pop("0")
print("---------------")
print(dictadura)
contador = 0
valores = list(dictadura.keys())
print(valores)
for i in valores:
    dictadura[str(contador)]=dictadura.pop(i)
    print(dictadura)
    contador+=1
print(retorno)'''
print("---------------")

lista = [1,1,1,1,1,1,1,1,2,1]
primero = True
almacen= 0
almacenactual= 0
for anterior in range(len(lista)-1):

    actual=anterior+1

    if lista[anterior]!=lista[actual] and primero:
        almacen = lista[anterior]
        almacenactual = lista[actual]
        primero= False

    elif lista[anterior]!=lista[actual] and primero== False:
        print("a."+str(lista[anterior]))
        break
    elif lista[anterior]==lista[actual] and primero== False and almacen !=0:
        print("c."+str(almacen))
        break
    elif lista[anterior]!=lista[actual]:
        print("b."+str(lista[anterior]))
        break
if almacenactual !=0:
    print(almacenactual)
       
for i in range(4):
    print(i)
        
        
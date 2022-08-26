'''s = {"s":54}
print(s["s"]+2)'''
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
print(z[0][1][1])
dimensiones =[]
pocisiones =[1,1,2]
pos = pocisiones
temporal=[]

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
'''for indice, valor in enumerate(z):
	print(f'El valor de la posición {indice} es {valor}')'''
print(dimensiones)
print(pocisiones)
print(pos)
def getpos(i):
    def papas():
        print("cocos")
    if i==0:
        papas()
        return pos[i]
    return pos[i]+dimensiones[i]*getpos(i-1)
    
vectorfial=recorrer(z)


print(z)
print(temporal)
print("--------")
print(getpos(len(dimensiones)-1))
print(vectorfial)
print(vectorfial[getpos(len(dimensiones)-1)])
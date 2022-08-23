s = {"s":54}
print(s["s"]+2)

x = "o o {} o o"
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
    print(i)

x = 0
t = "aknd"
r=[1,2,3,4]
print(isinstance(list(t),list))
print(list(t))
z=[[[1,2,3,4],[9,8,7,6]],[[1,2,3],[8,7,6]]]
print(z[0][1][1])
pocisiones =[0,1,1]
temporal=[]
for i in pocisiones:
    if(len(temporal)==0):
        temporal=z[i]
    else:
        temporal=temporal[i]
print(temporal)
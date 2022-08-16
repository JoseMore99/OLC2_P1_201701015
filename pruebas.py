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
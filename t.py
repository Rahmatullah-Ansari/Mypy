a=[1,3,5,7,9]
print(a[::2])
a=-1
b=a*0.5
print(type(b))
def fun(a,b):
    print(b,end=';')
    print(a)
fun(2,4)
def fun():
    print("fun()")
    return 5
fun()
mylist=[5,6,7]
for i in mylist:
    if(i%2==0):
        print(i)
def fun(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return (x*1)+(x+2)
for i in range(0,3):
    print(fun(i),end=" ")
setA={3,6,9}
setB={1,3,9}
print(setA|setB)
print("Prime"=="prime")
x=10
if x==10:
    pass
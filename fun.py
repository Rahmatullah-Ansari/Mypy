def fact(num):
    f=1
    for i in range(1,num+1):
        f *= i
    return f
def fib(num):
    a=0
    b=1
    for i in range(num):
        print(str(a)+" ",end="")
        t=a+b
        a=b
        b=t
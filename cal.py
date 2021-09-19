temp=1
def fact(num):
    global temp
    for i in range(1,num+1):
        temp *= i
    return temp

n = int(input("Enter how many number you want to enter:"))
A = []
for i in range(1,(n+1)):
    num = int(input("Enter "+str(i)+" number="))
    A.append(num)
print(A)
big = A[0]
second_big = None
for i in A[1:]:
    if big < i:
        second_big = big
        big = i
    elif second_big == None or second_big < i:
        second_big = i
print("Biggest number= "+str(big))
print("second biggest number= "+str(second_big))
n = int(input("Enter how many numbers you want to enter:"))
A = []
for i in range(1,(n+1)):
    num = int(input("Enter "+str(i)+" number="))
    A.append(num)
print(A)
even = 0
odd = 0
for i in A:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers= "+str(even))
print("Odd numbers= "+str(odd))


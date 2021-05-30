#pattern.
size = int(input('Enter size of pattern:'))
for i in range(size+1):
    for j in range(i):
        print(j,end=" ")
    print()
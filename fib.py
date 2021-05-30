import fun as f
num = int(input("Enter a number:\n"))
print("Factorial = "+str(f.fact(num)))
print("Fibonacci sequence = ",end="")
f.fib(num)
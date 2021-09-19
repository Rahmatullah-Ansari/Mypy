def calculate(num1,ch,num2):
    if ch == '+':
        return num1+num2
    elif ch == '-':
        return num1-num2
    elif ch == '*':
        return num1*num2
    elif ch == '/':
        return num1/num2
    else:
        print("Input character is not recognized!")
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")
print(num1, ch , num2, "=",calculate(num1,ch,num2))
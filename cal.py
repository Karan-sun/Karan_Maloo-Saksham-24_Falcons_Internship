# Calculator
num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))
oper = input("Enter the operator :")
if oper == "+":
    print(num1+num2)
elif oper == "-":
    print(num1-num2)
elif oper == "*":
    print(num1*num2)
elif oper == "/":
    print(num1/num2)
else:
    print("invaild input")
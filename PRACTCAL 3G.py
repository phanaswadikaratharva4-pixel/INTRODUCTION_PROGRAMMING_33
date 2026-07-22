num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
operator = input("enter operator (+, -, *, /):")

if operator == "+":
    print("result =",num1 + num2)
elif operator == "-":
    print("result =",num1 - num2)
elif operator == "*":
    print("result  =",num1 * num2)
elif operator == "/":
    if num2 !=0:
        print("result =",num1 / num2)
    else:
        print("error! division by zero is not allowed.")
else:
    print("invalid operator! please enter +, -, *, or /.")

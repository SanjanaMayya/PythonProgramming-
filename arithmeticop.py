def addition(a,b):
    sum = a + b
    print(sum)
def subtraction(a,b):
    diff = a - b
    print(diff)
def multiplication(a,b):
    prod = a * b
    print(prod)
def division(a,b):
    if (b==0):
        print("Division by zero error")
    else:
        quotient = a / b
        print(quotient)
def modulusdiv(a,b):
    if (b==0):
        print("Division by zero error")
    else:
        remainder = a % b
        print(remainder)
while(1):
    a = int(input("Enter the value for a :"))
    b = int(input("Enter the value for b :"))
    print("1.Addition.\n2.Subtraction.\n3.Multiplication.\n4.Division.\n5.Modulus Division.\n6.Exit")
    menu = int(input("Enter the menu option :"))
    if menu==1:
        addition(a,b)
    elif menu==2:
        subtraction(a,b)
    elif menu==3:
        multiplication(a,b)
    elif menu==4:
        division(a,b)
    elif menu==5:
        modulusdiv(a,b)
    elif menu==6:
        exit()
    else:
        print("Invalid Operator")
        


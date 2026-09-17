a = int(input("Enter first number: "))
b = int(input("Enter second number:"))
c = input("Enter operator : ")
#with if else
if c == "+":
    print("The addition is",a+b)
elif c== "-":
    print("The subtraction is" ,a-b)
elif c == "*":
    print("The multiplication is",a*b)
elif c=="%":
    print("The division is",a%b)
else:
    print("Invalid input")

#with function
def add(a,b):
    print(a,"+",b ,"=",a+b)

def sub(a,b):
    print(a,"-",b,"=",a-b)

def mul(a,b):
    print(a,"*",b,"=",a*b)

def div(a,b):
    print(a,"%",b,"=",a%b)


def add(a,b):
    result=a+b
    print(result)
def sub(a,b):
    result=a-b
    print(result)
def divmod(a,b):
    result=a/b
    print(result)
def mul(a,b):
    result=a*b
    print(result)

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
op=input("which operator you used")

if op=="+":
    add(a,b)
elif op=="-":
    sub(a,b)
elif op=="/":
    divmod(a,b)
elif op=="*":
    mul(a,b)

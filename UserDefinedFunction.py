#Function with no Argument & no Return value.

def printline():
    print("*"*50)

printline()
print("Welcome to user defined funtion in python")
printline()

#Function with Argument but no Return value.

def add(a,b):
    print("Additional : ",a+b)

printline()
x=int(input("Enter value : "))
y=int(input("Enter value : "))
add(x,y)
printline()

#Function with Agrumnent & Return value.

def sub(a,b):
    return a-b

printline()
x=int(input("Enter value : "))
y=int(input("Enter value : "))
#ans=sub(x,y)
print("Subtraction : ",sub(x,y))
printline()

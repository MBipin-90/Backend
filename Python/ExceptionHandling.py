print("Start Code")
try:
   a=int(input("Enter A : "))
   b=int(input("Enter B : "))
   c=a/b
   print("Division : ",c)
except ZeroDivisionError as e:
    print("Exception Caught : ",e)
except ValueError as e:
    print("Value Caught : ",e)
print("End Code")

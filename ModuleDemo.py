import udf

while True:

    print("*"*50)
    print("1. Odd Even")
    print("2. Max of Two")
    print("3. Max of Three")
    print("4. Fibonacci")
    print("5. Prime")
    print("6. Exit")
    print("*"*50)


    choice=int(input("Enter Your Choice : "))
    print("*"*50)

    if choice==1:
        a=int(input("Enter Number : "))
        udf.oddeven(a)
    elif choice==2:
        a=int(input("Enter Number : "))
        b=int(input("Enter Number : "))
        udf.maxoftwo(a,b)
    elif choice==3:
        a=int(input("Enter Number : "))
        b=int(input("Enter Number : "))
        c=int(input("Enter Number : "))
        udf.maxofthree(a,b,c)
    elif choice==4:
        a=int(input("Enter Number : "))
        udf.fibonacci(a)
    elif choice==5:
        a=int(input("Enter Number : "))
        udf.prime(a)
    elif choice==6:
        print("Thank You For Using Our Service.")
        print("*"*50)
        break
    else:
        print("Ivalid choice. please Try Again.")
    print("*"*50)

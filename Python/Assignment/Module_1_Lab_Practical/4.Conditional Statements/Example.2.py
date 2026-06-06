"""Practical Example 6: Write a Python program to check if a number is prime using if_else."""

n=int(input("Enter N: "))

if n%2!=0:
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            print(n,"Is not prime")
            break
    else:
        print(n,"Is prime")
else:
    print(n,"Is not prime")

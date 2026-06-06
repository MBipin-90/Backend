"""Practical Example 5: Write a Python program to find greater and less than a number using
if_else."""

number = int(input("Enter a number: "))

reference = 50

if number > reference:
    print("The number is greater than 50.")
elif number < reference:
    print("The number is less than 50.")
else:
    print("The number is equal to 50.")

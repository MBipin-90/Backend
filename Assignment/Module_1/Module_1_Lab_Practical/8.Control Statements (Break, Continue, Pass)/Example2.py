"""Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using 
the break statement."""

list = ["apple", "mango", "banana"]

for item in list:
    if item == "mango":
        break
    print(item)

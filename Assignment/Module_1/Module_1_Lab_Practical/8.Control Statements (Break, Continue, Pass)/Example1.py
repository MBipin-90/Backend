"""Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue 
statement. List1 = ['apple', 'banana', 'mango']"""

list=["apple", "mango", "banana"]

for item in list:
    if item == "mango":
        continue
    print(item)

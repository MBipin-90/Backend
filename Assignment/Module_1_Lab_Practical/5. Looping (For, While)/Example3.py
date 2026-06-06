"""Practical Example 3: Write a Python program to find a specific string in the list using a simple
for loop and if condition."""

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

search_item = "Mango"

found = False

for fruit in fruits:
    if fruit == search_item:
        found = True
        break

# Display result
if found:
    print(search_item, "found in the list.")
else:
    print(search_item, "not found in the list.")

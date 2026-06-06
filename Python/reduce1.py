from functools import reduce

def add(x,y):
    return x + y

numbers=[1,2,3,4]
result=reduce(add,numbers,100)

print(result)

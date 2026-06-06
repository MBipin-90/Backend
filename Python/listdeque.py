from _collections import deque

l=deque([])
l.append(10)
print(list(l))
l.append(20)
print(list(l))
l.append(30)
print(list(l))
l.append(40)
print(list(l))
l.append(50)
print(list(l))


l.popleft()
print(list(l))
l.popleft()
print(list(l))
l.popleft()
print(list(l))
l.popleft()
print(list(l))
l.popleft()
print(list(l))


#ramdoming

import random

l=[]

#print(random.randint(1,100))
#print(random.choice([1,2,101,"tops",True,"python",10,20]))

for i in range(1,101):
    l.append(i)
print(l)


l=[]
lucky=[]
import random
for i in range(1,101):
    l.append(i)

for i in range(10):
    num=random.choice(l)
    lucky.append(num)
    l.remove(num)

print(l)
print(lucky)



num=random.randint(1,20)


while True:
    guess=int(input("Guess A Number Between 1 to 20: "))
    if guess==num:
        print("You Guessed A Correct Number")
        break
    elif guess>num:
        print("You Guessed A Greater Number")
    elif guess<num:
        print("You Guessed A Smaller Number")








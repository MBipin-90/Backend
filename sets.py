s={1,2,10,20,1.1,2.2,"tops",True,1,2,10,20,"python"}

print(s)
s.pop()
print(s)
s.remove(10)
print(s)
s1={100,20,300}
s.update(s1)
print(s)
s.add(101)
print(s)
s2={1,2,3,4,5}
s3={1,3,5,7,9}

print(s3.difference(s2))
print(s2.intersection(s3))
print(s2.union(s3))

for i in s:
    print(i)

l=[1,2,3,10,20,"tops",1,2,10,20,"python"]
print(set(l))

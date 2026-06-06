d={101:"Bipin",456:"Hello",787:"Bye",333:"Ji"}

print(d)
print(d[787])
#print(d["Bye"])
print(d.get(333))
print(d.items())
print(d.keys())
print(d.values())   
print(d.pop(787))
print(d)
print(d.popitem())
print(d)

d1={100:"Bye",201:"JI"}
d.update(d1)
print(d)

for i in d:
    print(i," : ",d[i])
         


s=input("Enter string : ")

al=0
nm=0
sp=0
uc=0
lc=0

for i in s:
    if i.isalpha():
        al=al+1
    elif i.isnumeric():
        nm=nm+1
    elif i.isspace():
        sp=sp+1
    if i.isupper():
        uc=uc+1
    elif i.islower():
        lc=lc+1
print("Total Alphabet : ",al)
print("Total Numeric : ",nm)
print("Total Space : ",sp)
print("Total upper : ",uc)
print("Total lower : ",lc)


        


l1=["Bipin", "Python", "Developer", "anjali"]

def findVowels(name):
    if name[0] in "aeiou":
        return name

l2=list(filter(findVowels,l1))

print(l2)

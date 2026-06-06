#  01234567890123456    +
s="ABC DEFG HI JKLMN"
#  76543210987654321    -


print("----------Positive indexing----------")
print(s[3:13])
print(s[:15])
print(s[2:])
print(s[2:16:4])
print(s[:8:3])
print(s[5::2])
print(s[::5])


print("----------Negative indexing----------")
print(s[-16:-5])
print(s[:-2])
print(s[-12:])
print(s[-15:-3:3])
print(s[:-4:5])
print(s[-17::6])
print(s[::-2])

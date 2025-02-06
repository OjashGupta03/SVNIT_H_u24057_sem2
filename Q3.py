"""a=[]
for i in range(65,91):
    a.append(chr(i))
str=input("enter sentence to check:\n")
str=str.upper()
print(str)
for i in a:
    if i not in str:
        print("Not Pangrams sentence")
        exit()
    else:
        continue
print("Pangrams sentence")"""

a=set()
str=input("enter sentence to check:\n")
str=str.lower()
for i in str:
    if i.isalpha:
        a.add(i)
print("Pangrams" if len(a)==26 else "not Pangrams")



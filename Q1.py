a=input("enter string:")
result=""
j=0
for i in a:
    if(j%2==0):
        result+=i.lower()
    else:
        result+=i.upper()
    j+=1
print(result)
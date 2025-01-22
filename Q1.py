L=list()
LL=list()
a=int(input("enter number to be stored in list:"))
for i in range(1,a+1,1):
    L.append(i)
print(L)
for i in range(1,a+1,1):
    LL.append(i*i)
print(LL)
b=97
LLL=list()
for i in range(1,27,1):
    c=chr(b)
    LLL.append(c*i)
    b=b+1
print(LLL)

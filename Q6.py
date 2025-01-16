a=int(input("enter a number:"))
sum1=0
q=0

while(a!=0):
    q=a%10
    a=a//10
    sum1=sum1*10+q
print("reversed numbered = ",sum1)

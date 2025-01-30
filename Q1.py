"""n=int(input("Enter number:"))
k=n
while(n>9):
    num=n
    sum=0
    while(num!=0):
        sum+=num%10
        num=num//10
    n=sum
print(f"digital root of {k} is {digital(int(input("Enter number:")))}")
"""
def digital(n):
    if(n//10!=0):
        sum=0
        num=n
        while(num!=0):
            sum+=num%10
            num=num//10
        n=sum
        n=digital(n)
    return n
k=int(input("Enter number:"))
print(f"digital root of {k} is {digital(k)}")

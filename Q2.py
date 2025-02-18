T=int(input())
for i in range(T):
    k=int(input())
    sum,d=1,1
    for j in range(3,k+1):
        if (j%2==0):
            sum=sum+d
        else:
            sum+=d
            d=d+1
    print(sum)
    sum,d=1,1 
    
   # k=int(input())
   # l=floor(k/2)
   # b=ceil(k/2)
   # print(l*b)


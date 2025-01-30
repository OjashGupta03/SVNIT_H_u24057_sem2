T=int(input("enter number of test cases:"))
for i in range(T):
    N=int(input("enter number:"))
    a,count=N,0
    while(a!=0):
        if(N%(a%10)==0):
            count+=1
        a=a//10
    print(count)
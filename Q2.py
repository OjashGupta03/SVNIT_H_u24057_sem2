f=lambda x,y:x+y
def fibo(N):
    x=0
    y=1
    while(y<=N):
        t=y
        y=f(x,y)
        x=t
    if(N==x or N==0):
        print("IsFibo")
    else:
        print("IsNotFibo")
T=int(input("number of test cases:"))
for i in range(T):
    fibo(int(input("Enter number to check:")))


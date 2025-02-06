T=int(input("Enter number of test cases:"))
for l in range(T):
    A=int(input())
    B=int(input())
    count=0
    for i in range(A,B+1):
        i=i**0.5
        if  i==(i//1):
            count+=1
    print(count)
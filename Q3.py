def uthopian(N):
    length=1
    i=0
    while(i<N):
        if(i%2==0):
            length*=2
        else:
            length+=1
        i+=1
    return length  


Test=int(input("enter number of test cases:"))
for i in range(Test):
    print("height=",uthopian(int(input("Enter number of cycles:"))))    

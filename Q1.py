T=int(input("Enter Number of test cases:"))
for k in range(T):
    str=list(input())
    i,j,count=0,len(str)-1,0
    while (i<j):
        if(str[i]>str[j]):
            str[i],str[j]=str[j],str[i]
        if str[i]==str[j]:
            i=i+1
            j=j-1
        else:
            b=ord(str[j])-1
            count+=1
            str[j]=chr(b)  
    a=""
    for i in str:
        a=a+i
    print(a,count,sep=" - ")
"""
T=int(input("Enter test cases: "))
for i in range(T):
    str=input("Enter string: ")
    a=len(str)
    sum=0
    for i in range (len(str)//2):
        sum+=(max(ord(str[i]),ord(str[0-i-1]))-min(ord(str[i]),ord(str[0-i-1])))
    print(sum)

"""
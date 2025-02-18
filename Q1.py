L=int(input())
R=int(input())
max=0
for i in range(L,R):
    for j in range(i+1,R):
        max=max if max > (i^j) else (i^j)
print(max)
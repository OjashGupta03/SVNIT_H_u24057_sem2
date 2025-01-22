"""Q2.Write a program that generates 100 random integers that are either 0 or 1. Then find thelongest run of zeros, the largest number of zeros in a row.
For instance, the longest run of zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4."""
import random
L=list()
count=0
for i in range(1,101,1):
    L.append(random.randint(0,1))
print(L)
max=0
for i in range(0,100,1):
    if (L[i]==0):
        count=count+1
    else:
        if max<count:
            max=count
        count=0
if max<count:
            max=count
            count=0
print(max)

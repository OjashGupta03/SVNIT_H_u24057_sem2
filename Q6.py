
# Create a class for representing any 2-D point or vector. The methods inside this class include 
#its magnitude and its rotation with respect to the X-axis. Using the objects define functions for 
#calculating the distance between two vectors, dot product, cross product of two vectors. Extend 
#the 2-D vectors into 3-D using the concept of inheritance. Update the methods according to 3D.
# 
class dimension:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def mag(self):
        return (self.x**2 + self.y**2)**0.5 
    def __add__(self,A):
        return dimension(self.x+A.x,self.y+A.y)
    def __sub__(self,A):
        return dimension(self.x-A.x,self.y-A.y)
    def print(self):
        print((self.x,self.y))
        return (self.x,self.y)
    def scalar(A,B):
        return A.x*B.x+A.y*B.y
    def distance(a,b):
        d=(a.x-b.x)**2 + (a.y-b.y)**2
        return d**0.5
a=dimension(0,0)
a.print()
b=dimension(3,4)
b.print()
c=a+b
c.print()
(a-b).print()
print(a.scalar(b))
print(f"distance {a.print()} and {b.print()} : {a.distance(b)}")
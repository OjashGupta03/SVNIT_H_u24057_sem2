#5. Create a base class "Shape" with methods to calculate the area and perimeter. Implement 
#derived classes "Rectangle" and "Circle" that inherit from "Shape" and provide their own area and perimeter calculations. 
class Shape:
    def _init_(self,figure):
        self.figure = figure

    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def _init_(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14*self.radius**2
    def perimeter(self):
        return 2*3.14*self.radius
    
class Rectangle(Shape):
    def _init_(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)

rect = Rectangle(10,20)
print(rect.area())
print(rect.perimeter())
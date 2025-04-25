#4. Create a class "Employee" with attributes name and salary. Implement overloaded operators + and - to combine and compare employees based on their salaries.
class Employee:
    def _init_(self,name,salary):
        self.name = name
        self.salary = salary
        
    def _add_(self,other):
        sum =  self.salary + other.salary
        return f"Total salary is {sum}"
    
    def _sub_(self,other):
        diff =  self.salary - other.salary
        return f"Difference is {diff}"
    
obj1 = Employee("hitesh",1000)
obj2 = Employee("Dhiraj",6000)

print(obj1 + obj2)
print(obj1 - obj2)
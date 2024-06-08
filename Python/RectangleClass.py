class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return(self.length * self.breadth) 
    def perimeter(self):
        return(2 * (self.length + self.breadth))
   
length = int(input()) 
breadth = int(input())
rect_obj = Rectangle(length, breadth)
print(rect_obj.area())
print(rect_obj.perimeter())
class Shape:
    def __init__(self, radius):
        self.radius = radius 
    def area(self):
        return(3.14 * self.radius * self.radius)
    def perimeter(self):
        return(2 * 3.14 * self.radius) 
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius 
        super().__init__(self.radius)
    
class Rectange(Shape):
    def __init__(self, length, breadth):
        self.length = length 
        self.breadth = breadth 
    def area(self):
        return(self.length * self.breadth) 
    def perimeter(self):
        return(2 * (self.length + self.breadth))
        
circle_obj = Circle(5)
print(circle_obj.area())
print(circle_obj.perimeter())

rect_obj = Rectange(3,2)
print(rect_obj.area())
print(rect_obj.perimeter())
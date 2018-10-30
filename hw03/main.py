import math
class Rectangle(object):
    def __init__(self, width=0, height=0):
        super().__init__()
        self.width = width
        self.height = height
         
    def area(self):
        return self.width * self.height
         
         
class Square(Rectangle):
    def __init__(self, side=0):
        super().__init__(side, side)
         
         
         
class Ellipse(object):
    pi = 3.1415926535
    def __init__(self, a=0, b=0):
        super().__init__()
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b * self.pi
         
class Circle(Ellipse):
    def __init__(self, r=0):
        super().__init__(r, r)

def compute_area(shapes):
    return sum(x.area() for x in shapes)      
         
shapes = [Ellipse(10,20), Square(15), Circle(5), Rectangle(20,15), Circle(5), Square(15), Ellipse(10,20)]
total_area = compute_area(shapes)
print(total_area)
import time
time.sleep(5)

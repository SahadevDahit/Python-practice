class shape:
   
   def area():
       return 0

class rectangle(shape):
   def __init__(self, l, w):
       self.length = l
       self.width = w
       
   def area(self):
       return self.length * self.width
   
class Square(shape):
   def __init__(self, l):
       self.length = l
       
   def area(self):
       return self.length * self.length


rectangle=rectangle(10, 20);
print("Area of rectangle ",rectangle.area())

square=Square(10);
print("Area of square ",square.area())
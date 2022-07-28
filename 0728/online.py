class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = (p1.x, p1.y)
        self.p2 = (p2.x, p2.y)
        self.hor = abs(self.p1[0]-self.p2[0])
        self.ver = abs(self.p1[1]-self.p2[1])
    def get_area(self):
        return self.hor * self.ver
    def get_perimeter(self):
        return 2 * (self.hor + self.ver)
    def is_square(self):
        if self.ver == self.hor:
            return True
        else:
            return False
        
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())
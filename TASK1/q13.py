class Shape:
    def __init__(self, color):
     self.color = color
    def get_color(self):
     return self.color
    def get_area(self):
     pass
class Square(Shape):
    def __init__(self, color, side):
     super().__init__(color)
     self.side = side
    def get_area(self):
     return self.side * self.side
# Driver code
side=int(input("side length\n"))
color=input("enter color\n")
sq = Square(color, side)
print("Color:", sq.get_color())
print("Area:", sq.get_area())
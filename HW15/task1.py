# Create class Figure, and its heirs - Triangle(Figure), Circle(Figure), Rectangle(Figure),
# and Square(Rectangle)

# Add methods to get square and perimeter for each of them

class Figure:
    def __init__(self, a, b, c, d, p, r):
        self.side_length_1 = a
        self.side_length_2 = b
        self.side_length_3 = c
        self.side_length_4 = d
        self.pi = p
        self.radious = r



class Rectangle(Figure):
     def __init__(self, a, b, c, d, p, r):
        Figure.__init__(self, a, b, c, d, p, r)

     def perimeter_metchod(self):
        perimeter = self.side_length_1 + self.side_length_2 + self.side_length_3 + self.side_length_4
        print(f"P rectangle ={perimeter}")
        square_r = self.side_length_1*self.side_length_2
        print(f"S rectangle ={square_r}")



class Triangle(Figure):
    def __init__(self, a, b, c, d, p, r):
        Figure.__init__(self, a, b, c, d, p, r)

    def perimeter_metchod(self):
        perimeter = self.side_length_1 + self.side_length_2 + self.side_length_3
        print(f"P triangle ={perimeter}")
        square_t = self.side_length_1 * self.side_length_2/2
        print(f"S rectangle ={square_t}")



class Square(Figure):
    def __init__(self, a, b, c, d, p, r):
        Figure.__init__(self, a, b, c, d, p, r)

    def perimeter_metchod(self):
        perimeter = self.side_length_1 + self.side_length_2 + self.side_length_3 + self.side_length_4
        print(f"P squere = {perimeter}")
        square_s = self.side_length_1**2
        print(f"S square ={square_s}")



class Circle(Figure):
    def __init__(self, a, b, c, d, p, r):
        Figure.__init__(self, a, b, c, d, p, r)

    def perimeter_metchod(self):
        perimeter = 2*self.pi*self.radious
        print(f"P circle = {perimeter}")
        square_c = self.pi*self.radious**2
        print(f"S square ={square_c}")



if __name__ == '__main__':
      rectangle = Rectangle(a=2, b=2, c=3, d=3, p=None, r=None)
      rectangle.perimeter_metchod()

      triangle = Triangle(a=4, b=3, c=5, d=None, p=None, r=None)
      triangle.perimeter_metchod()

      square = Square(a=2, b=2, c=2, d=2, p=None, r=None)
      square.perimeter_metchod()

      circle = Circle(a=None, b=None, c=None, d=None, p=3.14, r=1)
      circle.perimeter_metchod()





class Rectangle:
    def __init__(self, value1, value2):
        self.length = value1
        self.width = value2

    def calculateArea(self):
        return self.length * self.width

    def calculatePerimeter(self):
        return 2* (self.length + self.width)

square = Rectangle(10,10)
print(square.calculateArea())
print(square.calculatePerimeter())
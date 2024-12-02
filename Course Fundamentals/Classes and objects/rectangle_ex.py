class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def resize(self, new_width, new_height):
        self.width = new_width
        self.length = new_height

rect = Rectangle(5, 5)
area = rect.calculate_area()
print(area)

rect.resize(6, 6)
area = rect.calculate_area()
print(area)

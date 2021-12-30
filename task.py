import math


class Shape:
    def __init__(self, center):
        self.center = center

    @staticmethod
    def get_distance(figure_1, figure_2):
        x_difference = (figure_2.center[0] - figure_1.center[0]) ** 2
        y_difference = (figure_2.center[1] - figure_1.center[1]) ** 2

        return math.sqrt(x_difference + y_difference)


class Circle(Shape):
    def __init__(self, center, radius):
        self.radius = radius
        super().__init__(center)

    def get_center(self):
        return self.center

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def move(self, x, y):
        self.center = [x, y]


class Square(Shape):
    def __init__(self, center, side):
        self.side = side
        super().__init__(center)

    def get_center(self):
        return self.center

    def get_vertex(self):
        return {
            'A': [self.center[0] - self.__half_side(), self.center[1] - self.__half_side()],
            'B': [self.center[0] - self.__half_side(), self.center[1] + self.__half_side()],
            'C': [self.center[0] + self.__half_side(), self.center[1] + self.__half_side()],
            'D': [self.center[0] + self.__half_side(), self.center[1] - self.__half_side()]
        }

    def get_area(self):
        return self.side ** 2

    def move(self, x, y):
        self.center = [x, y]

    def __half_side(self):
        return self.side / 2


class Triangle(Shape):
    def __init__(self, center, side):
        self.side = side
        super().__init__(center)

    def get_center(self):
        return self.center

    def get_vertex(self):
        return {
            'A': [self.center[0] - self.side / 2, self.center[1] - self.__circumscribed_circle_radius() / 2],
            'B': [self.center[0], self.center[1] + self.__circumscribed_circle_radius()],
            'C': [self.center[0] + self.side / 2, self.center[1] - self.__circumscribed_circle_radius() / 2]
        }

    def get_area(self):
        return 3 * math.sqrt(3) / 4 * self.__circumscribed_circle_radius() ** 2

    def move(self, x, y):
        self.center = [x, y]

    def __circumscribed_circle_radius(self):
        return self.side / math.sqrt(3)


print('==========Circle===========')
circle = Circle([0, 1], 2)

print('.get_center() -> {}'.format(circle.get_center()))
print('.get_area() -> {}'.format(circle.get_area()))
circle.move(0, 3)
print('.move(0, 3) -> {}'.format(circle.get_center()))


print('==========Square===========')
square = Square([1, 2], 3)

print('.get_center() -> {}'.format(square.get_center()))
print('.get_vertex() -> {}'.format(square.get_vertex()))
print('.get_area() -> {}'.format(square.get_area()))
square.move(0, 3)
print('.move(0, 3) -> {}'.format(square.get_center()))


print('==========Triangle===========')
triangle = Triangle([4, 7], 2.5)

print('.get_center() -> {}'.format(triangle.get_center()))
print('.get_vertex() -> {}'.format(triangle.get_vertex()))
print('.get_area() -> {}'.format(triangle.get_area()))
triangle.move(0, 3)
print('.move(0, 3) -> {}'.format(triangle.get_center()))


print('==========.get_distance()===========')
square = Square([1, 2], 3)
triangle = Triangle([0, 0], 2.5)

distance = Shape.get_distance(square, triangle)

print('Distance between circle and triangle is {}'.format(distance))


# OCP - Open Closed Principle
# Should be able to extend a class's behaviour without modifying it

# **BAD
class AreaCalculator(object):
    def __init__(self, shapes):
        pass

    @property
    def total_area(self):
        pass


class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height


# **BAD
class AreaCalculator(object):
    def __init__(self, shapes):
        pass

    @property
    def total_area(self):
        if shape == "shape1":
            # shape1.calculateArea()
            pass
        if shape == "shape2":
            # shape2.calculateArea()
            pass


# What if you want other shapes's area?
# should you change AreaCalculator's total_area?

# **GOOD
class Shape(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculateArea(self):
        pass


class Rectangle(Shape):
    def calculateArea(self):
        pass


class Triangle(Shape):
    def calculateArea(self):
        pass


# **GOOD
class AreaCalculator(object):
    def __init__(self, shape):
        self.shape = shape

    @property
    def total_area(self):
        self.shape.calculateArea()

# LSP = Liskov Substitution Principle
# Derived classes must substitutable for their base class

# if you have a parent class and a child class,
# then the base class and child class can be used
#  interchangeably without getting incorrect results.

# **BAD
class Rectangle(object):
    def calcArea(self):
        pass


class Square(Rectangle):
    def calcArea(self):
        pass


# LSP is violated because there is an unexpected result.
# calcArea in square is different from
# rectangle's though in mathematics square "is-a" rectangle,

from abc import ABCMeta, abstractmethod

# **GOOD
class Shape(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def calcArea(self)
        pass

class Square(Shape):
    def calcArea(self)
        pass

class Rectangle(Shape):
    def calcArea(self)
        pass
"""
Represent an operation to be performed on the elements of an object
structure. Visitor lets you define a new operation without changing the
classes of the elements on which it operates.
"""

import abc


class AbstractElement(metaclass=abc.ABCMeta):
    """
    Abstract Accept operation that takes a visitor as an argument.
    """

    @abc.abstractmethod
    def accept(self, visitor):
        pass


class ConcreteElementA(AbstractElement):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)


class ConcreteElementB(AbstractElement):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)


class AbstractVisitor(metaclass=abc.ABCMeta):
    """
    Abstract process for visitors
    """

    # Processes when visiting an element:

    @abc.abstractmethod
    def visit_concrete_element_a(self, concrete_element_a):
        pass

    @abc.abstractmethod
    def visit_concrete_element_b(self, concrete_element_b):
        pass


class ConcreteVisitor1(AbstractVisitor):
    def visit_concrete_element_a(self, concrete_element_a):
        pass

    def visit_concrete_element_b(self, concrete_element_b):
        pass


class ConcreteVisitor2(AbstractVisitor):
    def visit_concrete_element_a(self, concrete_element_a):
        pass

    def visit_concrete_element_b(self, concrete_element_b):
        pass


def main():
    concrete_visitor_1 = ConcreteVisitor1()
    concrete_element_a = ConcreteElementA()
    concrete_element_a.accept(concrete_visitor_1)


if __name__ == "__main__":
    main()

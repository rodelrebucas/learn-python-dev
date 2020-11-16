#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Compose objects into tree structures to represent part-whole
# hierarchies. Describes a group of objects that is treated as a **single instance**.


class Graphic:
    # Common behavior among components
    # Also for managing child in the nested structure
    def render(self):
        raise NotImplementedError("You should implement this.")


"""
    Define behavior for components having children.
    Store child components.
    Implement child-related operations in the Component interface.
"""


class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics = []

    def render(self):
        for graphic in self.graphics:
            graphic.render()

    def add(self, graphic):
        self.graphics.append(graphic)

    def remove(self, graphic):
        self.graphics.remove(graphic)


"""
    Represent leaf objects in the composition. A leaf has no children.
    Define behavior for primitive objects in the composition.
"""


class Ellipse(Graphic):
    def __init__(self, name):
        self.name = name

    def render(self):
        print("Ellipse: {}".format(self.name))


if __name__ == "__main__":

    graphic = CompositeGraphic()  # Main object
    graphic1 = CompositeGraphic()
    graphic2 = CompositeGraphic()

    ellipse1 = Ellipse("1")
    ellipse2 = Ellipse("2")
    ellipse3 = Ellipse("3")
    ellipse4 = Ellipse("4")

    graphic1.add(ellipse1)
    graphic1.add(ellipse2)
    graphic1.add(ellipse3)

    graphic2.add(ellipse4)

    # nested components
    graphic.add(graphic1)
    graphic.add(graphic2)

    graphic.render()  # Actual action fires here..

### OUTPUT ###
# Ellipse: 1
# Ellipse: 2
# Ellipse: 3
# Ellipse: 4

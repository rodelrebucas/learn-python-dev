#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A pattern that provides an unified interface for different objects
# to be usable on different interfaces

# *References:
# http://ginstrom.com/scribbles/2008/11/06/generic-adapter-class-in-python/
# https://sourcemaking.com/design_patterns/adapter
# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#adapter


class Dog(object):
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat(object):
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"


class Human(object):
    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "'hello'"


class Car(object):
    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "vroom{0}".format("!" * octane_level)


class Adapter(object):
    def __init__(self, obj, **adapted_methods):
        self.obj = obj  # store the obj for referencing its name
        self.__dict__.update(adapted_methods)  # store method/s as attribute

    def __getattr__(self, attr):
        # return the adapted method
        # taken from self / object's attr
        return getattr(self.obj, attr)


def main():
    objects = []

    dog = Dog()
    cat = Cat()
    human = Human()
    car = Car()

    # store each Adapter instance to the object
    objects.append(Adapter(dog, make_noise=dog.bark))
    objects.append(Adapter(cat, make_noise=cat.meow))
    objects.append(Adapter(human, make_noise=human.speak))
    objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))

    for obj in objects:
        # Here we can refer to the make_noise method
        # for each different sounds an object makes
        print("A {0} goes {1}".format(obj.name, obj.make_noise()))


if __name__ == "__main__":
    main()

### OUTPUT ###
# A Dog goes woof!
# A Cat goes meow!
# A Human goes 'hello'
# A Car goes vroom!!!

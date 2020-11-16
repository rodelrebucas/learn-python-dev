# - access/create an object's property only if it is called

from __future__ import print_function
import functools


# Class decorator
class lazy_property(object):
    def __init__(self, function):
        self.function = function
        # preserve identity of the wrapped function
        # works like wrap decorator
        functools.update_wrapper(self, function)

    # access point for this class/object
    # in every instance
    def __get__(self, obj, type_):
        if obj is None:
            return self

        # return value of the wrapped function
        val = self.function(obj)
        # add this wrapped function as a property
        obj.__dict__[self.function.__name__] = val
        return val


# function decorator
def lazy_property2(fn):
    attr = "_lazy__" + fn.__name__

    # this will be the property of class - self is (Person)
    @property
    def _lazy_property(self):
        if not hasattr(self, attr):
            print("Whos parent self?: ", self)  # Person
            print(
                "***Parent: ", fn(self)
            )  # fn is the parents method, get the value of this method
            print("***Parent attr: ", self.__dict__)  # _lazy_parents not exist yet
            # set/update the parents attributes
            setattr(self, attr, fn(self))
        return getattr(self, attr)

    return _lazy_property


class Person(object):
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.call_count2 = 0

    # this method will behave as a property of a class
    # after wrapping
    # p = Person()
    # calling p.relatives will acsess this class's __get__
    # __get__ is defined in lazy_property
    @lazy_property
    def relatives(self):
        # Get all relatives, let's assume that it costs much time.
        relatives = "Many relatives."
        return relatives

    @lazy_property2
    def parents(self):
        self.call_count2 += 1
        return "Father and mother"


def main():
    Jhon = Person("Jhon", "Coder")
    print(u"Name: {0}    Occupation: {1}".format(Jhon.name, Jhon.occupation))
    print(u"Before we access `relatives`:")
    print(Jhon.__dict__)
    print(u"Jhon's relatives: {0}".format(Jhon.relatives))
    print(u"After we've accessed `relatives`:")
    print(Jhon.__dict__)
    print(Jhon.parents)
    print(Jhon.__dict__)
    print(Jhon.parents)
    print(Jhon.call_count2)


if __name__ == "__main__":
    main()

### OUTPUT ###
# Name: Jhon    Occupation: Coder
# Before we access `relatives`:
# {'call_count2': 0, 'name': 'Jhon', 'occupation': 'Coder'}
# Jhon's relatives: Many relatives.
# After we've accessed `relatives`:
# {'relatives': 'Many relatives.', 'call_count2': 0, 'name': 'Jhon', 'occupation': 'Coder'}
# Father and mother
# {'_lazy__parents': 'Father and mother', 'relatives': 'Many relatives.', 'call_count2': 1, 'name': 'Jhon', 'occupation': 'Coder'}  # noqa flake8
# Father and mother
# 1

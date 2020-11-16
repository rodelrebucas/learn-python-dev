#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Holds a reference of the created subclasses


class RegistryHolder(type):

    REGISTRY = {}

    # special method
    def __new__(cls, name, bases, attrs):
        # create the new Object
        # cls will be (BaseRegisteredClass)
        # and some other subclasses
        new_cls = type.__new__(cls, name, bases, attrs)
        """
            Here the name of the class is used as key but it could be any class
            parameter.
        """
        # store it to the class's class , the *metaclass* =D mindblown
        cls.REGISTRY[new_cls.__name__] = new_cls
        return new_cls

    @classmethod
    def get_registry(cls):
        return dict(cls.REGISTRY)


class BaseRegisteredClass(object):
    __metaclass__ = RegistryHolder  # <-- Take Note. Defines the behavior of the class
    """
        Any class that will inherit from BaseRegisteredClass will be included
        inside the dict RegistryHolder.REGISTRY, the key being the name of the
        class and the associated value, the class itself.
    """
    pass


if __name__ == "__main__":
    print("Before subclassing: ")
    for k in RegistryHolder.REGISTRY:
        print(k)

    class ClassRegistree(BaseRegisteredClass):
        def __init__(self, *args, **kwargs):
            pass

    print("After subclassing: ")
    for k in RegistryHolder.REGISTRY:
        print(k)

###  OUTPUT ###
# Before subclassing:
# BaseRegisteredClass
# After subclassing:
# BaseRegisteredClass
# ClassRegistree

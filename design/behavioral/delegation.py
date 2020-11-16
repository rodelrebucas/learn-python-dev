#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Reference: https://en.wikipedia.org/wiki/Delegation_pattern
Author: https://github.com/IuryAlves

*TL;DR80
Allows object composition to achieve the same code reuse as inheritance.
"""


class Delegator(object):
    def __init__(self, delegate):
        self.delegate = delegate

    # special method for calling attributes / methods
    def __getattr__(self, name):
        # wrap any calls to an attr
        # to ignore not found error when
        # accessing non existing attributes
        # else attach one
        def wrapper(*args, **kwargs):
            if hasattr(self.delegate, name):
                # get Delegates called method
                attr = getattr(self.delegate, name)
                if callable(attr):
                    # return as is
                    return attr(*args, **kwargs)
            else:
                return "Default value"

        return wrapper

    def add_attr(self, attr):
        setattr(self, attr.__name__, attr)
        attr = getattr(self, attr.__name__)
        return attr


class Delegate(object):
    def do_something(self, something):
        print("Doing %s" % something)


def p(name):
    print(name)


def c(a, b):
    print(a, b)


if __name__ == "__main__":
    delegator = Delegator(Delegate())

    # instead of delegator.delegate.do_something()
    # attaches the Delegate method to Delegator
    delegator.do_something("nothing")  # 'Doing nothing'

    delegator.add_attr(p)
    delegator.add_attr(c)

    delegator.p("Name")
    delegator.c(1, 2)

    print(delegator.do_anything())  # Default value

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function


class Person(object):
    def __init__(self, name, action):
        self.action = action

    def do_action(self):
        return self.action


class Calculate(object):
    def amount(self, val):
        self.val = val
        return self

    def plus(self, increase):
        print(self.val + increase)
        return self


if __name__ == "__main__":

    calc = Calculate()
    person = Person("Jack", calc)
    person.do_action().amount(10).plus(10)

### OUTPUT ###
# 20

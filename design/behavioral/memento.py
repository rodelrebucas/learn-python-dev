#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://code.activestate.com/recipes/413838-memento-closure/
# Provides the ability to restore an object to its previous state.

from copy import copy
from copy import deepcopy


def memento(obj, deep=False):
    # copy the state here make sure its not a reference via deep copy
    state = deepcopy(obj.__dict__) if deep else copy(obj.__dict__)

    def restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)

    # Now holds a reference to an obj/instance and also its properties via state
    return restore


# By Class method's explicit restore
class Transaction(object):
    """A transaction guard.

    This is, in fact, just syntactic sugar around a memento closure.
    """

    isDeep = False
    states = []

    def __init__(self, isDeep, *obj_instances):
        self.isDeep = isDeep
        self.obj_instances = obj_instances
        self.commit()

    # commit or save the instance's property and value
    def commit(self):
        print("Commited obj/s: ", self.obj_instances)
        # functions that holds a reference to an *instance and its *saved/committed state/property
        self.states = [
            memento(obj_instance, self.isDeep) for obj_instance in self.obj_instances
        ]

    def rollback(self):
        for state_restore in self.states:
            # revert to the object's saved state
            state_restore()


# Option 2 by decorating
class Transactional(object):
    """Adds transactional semantics to methods.
    Methods decorated  with
    @Transactional will rollback to entry-state upon exceptions.
    """

    def __init__(self, method):
        self.method = method

    def __get__(self, obj, T):
        def transaction(*args, **kwargs):
            # copy the object directly and return a function that holds
            # an object reference and property as state
            state_restore = memento(obj)

            try:
                return self.method(obj, *args, **kwargs)
            except Exception as e:
                state_restore()
                raise e

        return transaction


class NumObj(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"self.value: {self.value}"

    def increment(self):
        self.value += 1

    def replaceValueWithString(self):
        self.value = "Two"
        print("self.value:", self.value)

    @Transactional
    def do_stuff(self):
        self.value = "1111"  # <- invalid value
        self.increment()  # <- will fail and rollback


# Other simple implementation
import pickle


class Originator:
    """
    Create a memento containing a snapshot of its current internal
    state.
    Use the memento to restore its internal state.
    """

    def __init__(self):
        self._state = None

    # rollback here
    def set_memento(self, memento):
        previous_state = pickle.loads(memento)
        vars(self).clear()
        vars(self).update(previous_state)

    def create_memento(self):
        return pickle.dumps(vars(self))  # equivalent to __dict__


def simulate():
    originator = Originator()
    memento = originator.create_memento()
    originator._state = True
    originator.set_memento(memento)


if __name__ == "__main__":
    num_obj = NumObj(1)
    print("num_obj property:", num_obj.__dict__)  # Property: {'value': 1}
    # create a transaction to save the num_obj property
    num_obj_transaction = Transaction(True, num_obj)

    num_obj.replaceValueWithString()  # self.value: Two
    #  restoring explicitly
    num_obj_transaction.rollback()
    print(num_obj)  # self.value: 1

    # Restore state when exceptions are encountered
    try:
        num_obj.do_stuff()
    except Exception as e:
        print("-> doing stuff failed!")
        import sys
        import traceback

        traceback.print_exc(file=sys.stdout)
    print(num_obj)

    # Other simple implementation
    simulate()

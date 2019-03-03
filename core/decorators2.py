"""

    Other decorator implementations

"""
# ------------------------------------->
# Decorator as keeper of states

import functools


def count_calls(func):
    print("Executed once")

    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        # increment here
        wrapper_count_calls.num_calls += 1
        return func(*args, **kwargs)

    # create and initialize the attribute outside the inner function
    wrapper_count_calls.num_calls = 0

    # return inner function
    return wrapper_count_calls


@count_calls
def call():
    print("Hello")


# function calls
call()
call()
print(call.num_calls)  # 2

# ------------------------------------->
# Decorator as keeper of states using Classes


class Counter:
    def __init__(self):
        self.count = 0

    # Special method that is invoke when instance or decorated function is innvoke
    def __call__(self):
        self.count += 1


counter = Counter()
counter()
print(counter.count)  # 1
counter()
print(counter.count)  # 2


# ------------------------------------->
# Decorator as keeper of states using Classes and a decorator class


class CounterCls:
    def __init__(self, func):
        self.count = 0
        self.func = func

    # Special method that is invoke when instance or decorated function is innvoke
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Calling {self.func.__name__} with count: ", self.count)
        return self.func(*args, **kwargs)


@CounterCls
def count_me():
    print("Im Counted..")


count_me()  # Calling count_me with count:  1
count_me()  # Calling count_me with count:  2

# ------------------------------------->
# Decorator to make a singleton class


def singleton(cls):
    functools.wraps(cls)

    def wrapper_singleton(*args, **kwargs):
        if wrapper_singleton.instance is None:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class SingletonCls(object):
    def __init__(self, name):
        self.name = name


instance_one = SingletonCls("one")
instance_two = SingletonCls("two")

# Same id
print(id(instance_one))  # 140282411492968
print(id(instance_two))  # 140282411492968

print(instance_one.name)  # one
print(instance_two.name)  # one

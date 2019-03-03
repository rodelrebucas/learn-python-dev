# Singleton - ensures only one object of the class is created


# Basic example
class Singleton(object):
    def __new__(cls):  # special method for creating instance
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s1 = Singleton()  # instance e.g. object at 123
print("Object created..", s1)

s2 = Singleton()  # instance e.g. object at 123
print("Object created..", s2)

# Lazy singleton instantiation
class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("Init called..., no instance yet")
        else:
            print("Instance already created: ", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()  # create actual instance
        return cls.__instance


s1 = Singleton()
print(Singleton.getInstance())
s3 = Singleton()

# mono state singleton
# all instances share one state
class Car:
    __shared_state = {"tires": 4}

    def __init__(self):
        self.x = 1
        # __dict__ special variable for storing property / state
        self.__dict__ = self.__shared_state


a = Car()
b = Car()
# same state
print(a.__dict__)
print(b.__dict__)

# Using metaclasses
# metaclass is a class of Class
# metaclass can define the class, and overrides __init__ and __new__
class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print("MetaSingleton:", args)
        # cls is the class Object Logger
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    def __init__(self, *args, **kwargs):
        print("Logger:", args)


logger1 = Logger(1, 2)
logger2 = Logger()
print(logger1)
print(logger2)

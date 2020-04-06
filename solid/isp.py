# ISP - Interface Segration Principle
# Clients should not be forced to depend on methods that they do not use

# **BAD

from abc import ABCMeta, abstractmethod


class Worker(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def canEat(self):
        pass

    @abstractmethod
    def doWork(self):
        pass


class Human(Worker):
    def canEat(self):
        pass

    def doWork(self):
        pass


class Robot(Worker):
    def canEat(self):  # a robot does not need to eat
        pass

    def doWork(self):
        pass


# **GOOD
class Human(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def canEat(self):
        pass

    @abstractmethod
    def doWork(self):
        pass


class Robot(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def doWork(self):
        pass


class HumanWorker(Human):
    def canEat(self):
        pass

    def doWork(self):
        pass


class RobotWorker(Robot):
    def doWork(self):
        pass

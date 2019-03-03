# Template - defines the structure or design or your logic
# Use if you have:
# 1. multiple algorithms which have closely similar implementations
# 2. subclassing help reduce code duplication

# Parts:
# 1. AbstractClass - interface for the algorithm
# 2.    template_method() - steps that makes up the algorithm
# 3. ConcreteClass - implements AbstractClass

from abc import abstractclassmethod, ABCMeta


class Trip(metaclass=ABCMeta):

    # logic here...
    @abstractclassmethod
    def day1(self):
        pass

    @abstractclassmethod
    def day2(self):
        pass

    @abstractclassmethod
    def setTransport(self):
        pass

    @abstractclassmethod
    def returnHome(self):
        pass

    # template method
    def itenerary(self):
        # steps that makes up the algorithm/business logic
        self.setTransport()
        self.day1()
        self.day2()
        self.returnHome()


# implemented in each type of trips
class SouthTrip(Trip):
    def day1(self):
        pass

    def day2(self):
        pass

    def setTransport(self):
        pass

    def returnHome(self):
        pass


class NorthTrip(Trip):
    def day1(self):
        pass

    def day2(self):
        pass

    def setTransport(self):
        pass

    def returnHome(self):
        pass

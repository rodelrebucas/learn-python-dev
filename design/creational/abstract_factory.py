# - Abstract factory pattern provides interface to create *families of related objects*
# - Interface decides what object to create
# - Creates related products


from abc import ABCMeta, abstractmethod

### Main interface
# Abstract factory
class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass


# Concrete factories interface
class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class UsPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()


# abstract products
class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, VegPizza):
        pass


class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, NonVegPizza):
        pass


# concrete products
class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print(f"Prepare {type(self).__name__}")


class ChickenPizza(NonVegPizza):
    def serve(self):
        print(f"Prepare {type(self).__name__}")


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print(f"Prepare {type(self).__name__}")


class HamPizza(NonVegPizza):
    def serve(self):
        print(f"Prepare {type(self).__name__}")


# factories can create same product groups
indian = IndianPizzaFactory()
american = UsPizzaFactory()

print(indian.createNonVegPizza())
print(american.createVegPizza())

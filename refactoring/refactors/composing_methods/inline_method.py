# When a method body is more obvious than the method itself

# from
class PizzaDelivery:
    # ...
    def getRating(self):
        return 2 if self.moreThanFiveLateDeliveries() else 1

    def moreThanFiveLateDeliveries(self):
        return self.numberOfLateDeliveries > 5


# to
class PizzaDelivery:
    # ...
    def getRating(self):
        return 2 if self.numberOfLateDeliveries > 5 else 1

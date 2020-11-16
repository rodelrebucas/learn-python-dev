# Long lines of method , extracing methods is impossible

# from
class Order:
    # ...
    def price(self):
        primaryBasePrice = 0
        secondaryBasePrice = 0
        tertiaryBasePrice = 0
        # long computation.
        # ...
        pass


# to
class Order:
    # ...
    def price(self):
        return PriceCalculator(self).compute()


class PriceCalculator:
    def __init__(self, order):
        self._primaryBasePrice = 0
        self._secondaryBasePrice = 0
        self._tertiaryBasePrice = 0
        # copy relevant information from order object.
        # ...

    def compute(self):
        # long computation.
        # ...
        pass

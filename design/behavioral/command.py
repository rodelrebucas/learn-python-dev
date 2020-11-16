# Command pattern - hides information when an action is performed
# Consists of: Command, Receiver, Invoker and Client

# Why command pattern?
# 1. encapsulates a request object
# 2. parameterization of clients with different requests
# 3. queue a request
# 4. provide an object oriented callback

# Can be used when:
# 1. paremeterizing objects depending on the action performed
# 2. add actions to queue and execute the requests at some point
# 3. create a structure of high-level of operations that are based on smaller operations


from abc import ABCMeta, abstractmethod

# Command - abstract command
class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


# Client - concrete command
# This class represents the action you want
class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


# Client
class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


# Receiver
class StockTrade:
    # - these are the actual actions
    # or logic of the command happens
    def buy(self):
        print("You will buy stocks")

    def sell(self):
        print("You will sell stocks")

    # -


# Invoker - entry or point of execution
class Agent:
    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()


if __name__ == "__main__":
    # Receiver/ contains the actual actions you want
    stock = StockTrade()

    # Client - actions you want execute
    buystock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)

    # Invoker
    agent = Agent()
    agent.placeOrder(buystock)  # actions as parameter
    agent.placeOrder(sellStock)  # actions as parameter

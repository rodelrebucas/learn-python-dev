# state design pattern - a way for an object to change its behavior at *runtime*
#  Parts:
# State - interface that encapsulates objects behaviour
# ConcreteState - implements the actual behavior
# Context - maintains the current state

# State
class ComputerState(object):
    name = "default state object"
    allowed = []

    def __init__(self):
        print(self)

    # change the class of  the object/current instance
    # at runtime
    def switch(self, state):
        old_state = self.name
        self.__class__ = state
        print(f"Switching from {old_state} to {self}")
        print(self.name)

    def __str__(self):
        return self.name


# Concrete state
class Off(ComputerState):
    name = "off"


class On(ComputerState):
    name = "On"


# Context
class Computer(object):
    def __init__(self):
        # default state
        self.state = Off()

    def change(self, state):
        self.state.switch(state)


if __name__ == "__main__":

    # create the context
    context = Computer()  # off

    # change the state
    context.change(On)  # Switching from Off to On
    # On

# Advantages
# 1. Tight cohesion since states can be aggregated into the ConcreteState class
# 2. Polymorphism makes it easier to add additional behaviour or state
# 3. Not dependent on conditionals such as if/else , switch/case

# Disadvantages
# 1. As states grow larger, you need to write more classes, hence more effort on maintenance
# and changes
# 2. Adds Complexity as codebase grow larger

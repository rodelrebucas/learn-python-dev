# Separate the construction of a complex object from its
# representation so that the same construction process can create different representations.
# Parse a complex representation, create one of several targets.

# Allows you to build different kind of object by implementing the Steps,
# to build on particular object
# * Building an object requires steps

# Abstract <anything>
class Anything(object):
    def __init__(self):
        self.build_step_1()
        self.build_step_2()

    def build_step_1(self):
        raise NotImplementedError

    def build_step_2(self):
        raise NotImplementedError


# Concrete implementations
class AnythingA(Anything):
    def build_step_1(self):
        pass

    def build_step_2(self):
        pass


class AnythingB(Anything):
    def build_step_1(self):
        pass

    def build_step_2(self):
        pass

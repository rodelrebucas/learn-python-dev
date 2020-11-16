# Encapsulates object interacton
# Provides loose coupling by keeping objects from interacting explicitly


class Mediator:
    """
    Implement cooperative behavior by coordinating Colleague objects.
    Know and maintains its colleagues.
    """

    def __init__(self):
        self._colleague_1 = Colleague1(self)
        self._colleague_2 = Colleague2(self)

    # Some processes here...


class Colleague1:
    def __init__(self, mediator):
        # Communicates to mediator to reach another colleague
        self._mediator = mediator


class Colleague2:
    def __init__(self, mediator):
        # Communicates to mediator to reach another colleague
        self._mediator = mediator


def main():
    mediator = Mediator()


if __name__ == "__main__":
    main()

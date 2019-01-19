# - A single class that represents an entire subsystem

## Principle of lease knowledge
# - Simplifies an underlying subsystem's complexity
# - We design a facade when there are tighly coupled classes
# - also when there are alot of dependencies between classes
#   you don't want to expose the system to avoid unintentional changes
#
# A facade contains:
# client, facade, and the system that contains sub systems
class EventManager(object):
    def __init__(self):
        print("Orgnize system...")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.caterer = Musician()
        self.caterer.setMusicType()


# Subsystems
class Hotelier(object):
    pass


class Florist(object):
    pass


class Caterer(object):
    pass


class Musician(object):
    pass


class You(object):
    pass


# You -> EventManager(facade) -> Subsystems

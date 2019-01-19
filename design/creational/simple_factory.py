from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class dog(Animal):
    def do_say(self):
        print("bark...")


class cat(Animal):
    def do_say(self):
        print("Meow...")


class ForestFactory(object):
    def make_sound(self, animal):
        return eval(animal)().do_say()


if __name__ == "__main__":
    forest = ForestFactory()
    animal_type = input("animal type[dog/cat]? ")
    forest.make_sound(animal_type)

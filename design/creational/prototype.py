# Reduce no. of classes by using prototypical instance at run-time
# Useful when:
#     1. instantiation is expensive
#     2 .easier to derive new closely related objects


class Prototype(object):

    value = "default"

    def clone(self, **attrs):
        """Clone a prototype and update inner attributes dictionary"""
        obj = (
            self.__class__()
        )  # returns the class's type for this instance (self) which Prototype
        obj.__dict__.update(attrs)  # update/add the instance's attributes

        return obj  # returns the Prototype class with updated attributes


# Helps stores different kinds of protoypes
class PrototypeDispatcher(object):
    def __init__(self):
        self._objects = {}

    def findOneObject(self, name):
        return self._objects[name]

    def get_objects(self):
        """Get all objects"""
        return self._objects

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]


def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    protoInstanceA = prototype.clone()
    protoInstanceB = prototype.clone(value="a-value", category="a", keyX="sample")
    protoInstanceC = prototype.clone(value="b-value", is_checked=True)

    print(prototype)
    print(protoInstanceA)

    dispatcher.register_object("objecta", protoInstanceA)
    dispatcher.register_object("objectb", protoInstanceB)
    dispatcher.register_object("objectc", protoInstanceC)

    print([{n: p.value} for n, p in dispatcher.get_objects().items()])


if __name__ == "__main__":
    main()

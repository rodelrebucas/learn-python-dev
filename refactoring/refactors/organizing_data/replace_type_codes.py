## Replace type codes with Class

# from
class Person:
    A: str
    B: str
    C: str
    bloodType: str


# to, Im not sure about this...
class BloodType:
    bloodType: str

    def __init__(self, type_):
        self.bloodType = type_

    def getBloodType(self):
        return self.bloodType

    @staticmethod
    def typeA():
        return BloodType("A")

    # constructor for setting the value
    # static methods returning the object based on the value of A,B,C
    # more like an enum in java


class Person:
    bloodType: BloodType

    def __init__(self, bloodType):
        self.bloodType = BloodType("A")

    def setBloodType(self, type_):
        self.bloodType = BloodType(type_)

    def getbloodType(self):
        return self.bloodType.getBloodType()

    def useBlood(self):
        print(
            f"Using blood type { self.bloodType.typeA()}"
        )  # why do i need to do this?, why just not self.bloodType


if __name__ == "__main__":
    p = Person("A")
    p.useBlood()
    print(p.getbloodType())

# ---
## Replace type codes with class
# Problem: You have a coded type that directly affects program behavior
# (values of this field trigger various code in conditionals).

# Solution: Create subclasses for each value of the coded type.
# Then extract the relevant behaviors from the original class
#  to these subclasses. Replace the control flow code with polymorphism.

# ---
## Replacing type code with State/Strategy, see State or Strategy pattern

# ---
## Replace Subclass with Fields
# You have subclasses differing only in their (constant-returning) methods.
# Solution: Replace the methods with fields in the parent class and delete the subclasses.

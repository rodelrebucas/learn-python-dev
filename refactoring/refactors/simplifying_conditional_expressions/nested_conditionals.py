## Replace Nested Conditional with Guard Clauses

# from
def getPayAmount(self):
    if self.isDead:
        result = deadAmount()
    else:
        if self.isSeparated:
            result = separatedAmount()
        else:
            if self.isRetired:
                result = retiredAmount()
            else:
                result = normalPayAmount()
    return result


# to
def getPayAmount(self):
    if self.isDead:
        return deadAmount()
    if self.isSeparated:
        return separatedAmount()
    if self.isRetired:
        return retiredAmount()
    return normalPayAmount()


## Replace Conditional with Polymorphism

# from
class Bird:
    # ...
    def getSpeed(self):
        if self.type == EUROPEAN:
            return self.getBaseSpeed()
        elif self.type == AFRICAN:
            return self.getBaseSpeed() - self.getLoadFactor() * self.numberOfCoconuts
        elif self.type == NORWEGIAN_BLUE:
            return 0 if isNailed else self.getBaseSpeed(self.voltage)
        else:
            raise Exception("Should be unreachable")


# to
class Bird:
    # ...
    def getSpeed(self):
        pass


class European(Bird):
    def getSpeed(self):
        return self.getBaseSpeed()


class African(Bird):
    def getSpeed(self):
        return self.getBaseSpeed() - self.getLoadFactor() * self.numberOfCoconuts


class NorwegianBlue(Bird):
    def getSpeed():
        return 0 if self.isNailed else self.getBaseSpeed(self.voltage)


# Somewhere in client code
speed = bird.getSpeed()

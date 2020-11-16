## Error to exception
# The intention is to return an error

# from
def withdraw(self, amount):
    if amount > self.balance:
        return -1
    else:
        self.balance -= amount
    return 0


# to
def withdraw(self, amount):
    if amount > self.balance:
        raise BalanceException()  # or Exception
    self.balance -= amount


# now wrap the caller  with try/Except

## Exception to test
# The intention is to test

# from
def getValueForPeriod(periodNumber):
    try:
        return values[periodNumber]
    except IndexError:
        return 0


# to
def getValueForPeriod(self, periodNumber):
    if periodNumber >= len(self.values):
        return 0
    return self.values[periodNumber]

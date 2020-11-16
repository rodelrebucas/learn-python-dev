# altering or assigning other values to parameters

# from
def discount(inputVal, quantity):
    if inputVal > 50:
        inputVal -= 2
    # ...


# to
def discount(inputVal, quantity):
    result = inputVal
    if inputVal > 50:
        result -= 2
    # ...

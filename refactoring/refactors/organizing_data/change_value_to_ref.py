# So you have many identical instances of a single class
# that you need to replace with a single object.

# from aggregation
class A:
    customer = Customer()


# to association
class A:
    def __init__(self, customer):
        pass


### Reverse refactor : Change Reference to Value

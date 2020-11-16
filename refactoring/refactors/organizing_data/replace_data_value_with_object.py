# If field has its own behavior and associated data make this field
# make this field an object

# from
class Order:
    customer: str


# to
class Customer:
    pass


class Order:
    customer: Customer

# variable used to assign the result from a method call

# from
def hasDiscount(order):
    basePrice = order.basePrice()
    return basePrice > 1000


# to
def hasDiscount(order):
    return order.basePrice() > 1000

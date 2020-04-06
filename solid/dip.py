# DIP - Dependency Injection Principle
# High level modules should not depend on low level modules.
# Both should depend upon abstractions.

# **BAD
class CarWashService(object):
    def __init__(self):
        self.paymentMethod = Bank()

    # CarWashService depends on Bank() class
    # What if you want to add other payment method?
    # CarshWashService is tighly coupled with Bank()


# **GOOD
class CarWashService(object):
    def __init__(self, paymentMethod):
        self.paymentMethod = paymentMethod

    # Changes on paymentMethod doesn't affect
    # CarWashService since paymentMethod is injected.
    # You can pass any payment method

# - representaton of another object
# - seeker and provider
#       seeker      - requests a resource
#       provider    - provides a resource

# Example:
# Buying an item: using  a debit card
# Proxy: the debit card, since you want to get money from the bank
# Client: You
# Subject: The action you want to do, that a proxy can and the Real subject can do
# Real Subject: The main entity that has the resources

# Subject
from abc import ABCMeta, abstractmethod
class Payment(metaclass=ABCMeta)
    @abstractmethod
    def pay(self):
        pass

# Client
class You:
    def __init__(self):
        self.debitCard = DebitCard()

    def make_payment(self):
        self.debitCard.pay()

# Proxy
class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def pay(self):
        # logic for getting card number
        # ... some other logics for processing
        # call the Real subject's action
        self.bank.pay()

# Real Subject
class Bank(Payment):
    def __init__(self):
        self.card  = None
        self.account = None

    def pay(self):
        # pay logic here
        pass
    
    # ... other logic,process for
    # getting card, account and funds
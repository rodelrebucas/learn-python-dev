# SRP - Single Responsibility Principle
# A class should have one and only one reason to change

# **BAD


class Email(object):
    def setSender(self):
        pass

    def setRecipient(self):
        pass

    def sendEmail(self):
        pass

    def setCredential(self):
        pass


# we want to achieve a tight cohesion thus functionalities
# that conceptually belongs together should  go together,
# minimizing a lot of functionalities and the need to change
# and keep track of changes that depends on the class

# **GOOD
class Email(object):
    def __init__(self, authentication):
        self.auth = authentication

    def setSender(self):
        pass

    def setRecipient(self):
        pass

    def sendEmail(self):
        self.auth.authenticate()
        # send logic


class Auth(object):
    def setCredential(self):
        pass


# we removd setCredential() since it does not logically belong to
# email class

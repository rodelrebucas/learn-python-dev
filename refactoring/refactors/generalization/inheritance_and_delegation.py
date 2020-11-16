## Inheritance to delegation

# from
class Profile:
    account: int
    name: str
    lastname: str

    def pMeth(self):
        pass

    # ... other methods


class SocialMedia(Profile):
    media = "my-media"


# to
class SocialMedia:
    media = "my-media"
    profile: Profile

    def __init__(self, profile):
        self.profile = profile

    # delegate method
    def pMeth(self):
        self.profile.pMeth()


profile = Profile()
media = SocialMedia(profile)
media.pMeth()  # class profiles's pMeth


# Refactor if:
# 1. There is a violation of Liskov Substitution Principle
# 2. Subclass uses only a portion of the methods of the superclass.


## Reverse refactor: Replace Delegation with Inheritance
# A class contains many simple methods
# that delegate to all methods of another class.

# Refactor only if:
# 1. class doesn't have a parent class
# 2. large amount of delegations

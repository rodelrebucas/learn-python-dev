# - Simple factory pattern is responsible for creating objects *with different types*.
# - Subclass decides what kind  of object is instantiated
# - Creates only one product

### Simple factory pattern
from abc import ABCMeta, abstractmethod

# Sections, a base class = Product
class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


# Concrete Product
class PersonalSection(Section):
    def describe(self):
        print("Personal Section")


class AlbumSection(Section):
    def describe(self):
        print("Album Section")


class PatentSection(Section):
    def describe(self):
        print("Patent Section")


class PublicationSection(Section):
    def describe(self):
        print("PUblication Section")


# Creator, an abstrast class to be implemented by
# the concrete creators
class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    # creators' *factory method
    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


# Concrete creators
# Implements Profile to create the object desired
class linkedin(Profile):
    # Concrete creators' *factory method
    def createProfile(self):
        self.name = "LinkedIn"
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())


class facebook(Profile):
    def createProfile(self):
        self.name = "Facebook"
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


if __name__ == "__main__":
    profile_type1 = "facebook"  # input("Name your profile[Facebook or LinkedIn]")
    profile1 = eval(profile_type1.lower())()  # create the instance
    print(f"Created instance of profile: {profile1.name}:")

    profile_type2 = "linkedin"
    profile2 = eval(profile_type2.lower())()
    print(f"Created instance of profile: {profile2.name}:")

    print(f"Created instances of profiles: {profile1.name, profile2.name}:")

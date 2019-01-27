# Code fragments that can be grouped together

# From
def printProfile(self):
    self.printAge()

    # print details
    print("name:", self.name)
    print("lastname:", self.lastname)


# To
def printOprintProfilewing(self):
    self.printAge()
    self.printName()


def printName(self, outstanding):
    print("name:", self.name)
    print("amount:", self.lastname)

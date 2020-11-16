# complex expressions

# from
def renderBanner(self):
    if (
        (self.platform.toUpperCase().indexOf("MAC") > -1)
        and (self.browser.toUpperCase().indexOf("IE") > -1)
        and self.wasInitialized()
        and (self.resize > 0)
    ):
        # do something
        pass


# to
def renderBanner(self):
    isMacOs = self.platform.toUpperCase().indexOf("MAC") > -1
    isIE = self.browser.toUpperCase().indexOf("IE") > -1
    wasResized = self.resize > 0

    if isMacOs and isIE and self.wasInitialized() and wasResized:
        # do something
        pass

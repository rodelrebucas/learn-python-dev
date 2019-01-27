# A utility class doesn’t contain the method that you need
#  and you can’t add the method to the class.

# from
class Report:
    # ...
    def sendReport(self):
        nextDay = Date(
            self.previousEnd.getYear(),
            self.previousEnd.getMonth(),
            self.previousEnd.getDate() + 1,  # compute next day
        )
        # ...


# to
class Report:
    # ...
    def sendReport(self):
        newStart = self._nextDay(self.previousEnd)
        # ...

    # compute next day in a separate method
    def _nextDay(self, arg):
        return Date(arg.getYear(), arg.getMonth(), arg.getDate() + 1)

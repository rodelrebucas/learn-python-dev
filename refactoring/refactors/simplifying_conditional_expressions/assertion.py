# Introduce Assertion

# from
def getExpenseLimit(self):
    # should have either expense limit or a primary project
    return (
        self.expenseLimit
        if self.expenseLimit != NULL_EXPENSE
        else self.primaryProject.getMemberExpenseLimit()
    )


# to
def getExpenseLimit(self):
    # assert first to check if these fields have values
    # this helps you fail fast and check certain conditions
    # before processing
    assert (self.expenseLimit != NULL_EXPENSE) or (self.primaryProject != None)

    return (
        self.expenseLimit
        if (self.expenseLimit != NULL_EXPENSE)
        else self.primaryProject.getMemberExpenseLimit()
    )

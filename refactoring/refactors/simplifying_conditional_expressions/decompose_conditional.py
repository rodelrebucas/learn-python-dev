# from
if date.before(SUMMER_START) or date.after(SUMMER_END):
    charge = quantity * winterRate + winterServiceCharge
else:
    charge = quantity * summerRate

# to
if isSummer(date):
    charge = summerCharge(quantity)
else:
    charge = winterCharge(quantity)

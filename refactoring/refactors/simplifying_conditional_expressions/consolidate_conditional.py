# from
def disabilityAmount():
    if seniority < 2:
        return 0
    if monthsDisabled > 12:
        return 0
    if isPartTime:
        return 0
    # compute the disability amount
    # ...


# to
def disabilityAmount():
    if isNotEligableForDisability():
        return 0
    # compute the disability amount
    # ...

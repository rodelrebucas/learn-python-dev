# from
low = daysTempRange.getLow()
high = daysTempRange.getHigh()
withinPlan = plan.withinRange(low, high)

# to
withinPlan = plan.withinRange(daysTempRange)  # process as object

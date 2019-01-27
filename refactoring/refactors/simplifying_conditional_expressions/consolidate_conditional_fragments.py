# from
if isSpecialDeal():
    total = price * 0.95
    send()
else:
    total = price * 0.98
    send()

# to
if isSpecialDeal():
    total = price * 0.95
else:
    total = price * 0.98
send()

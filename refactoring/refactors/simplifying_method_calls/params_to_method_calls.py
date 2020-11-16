# from
basePrice = quantity * itemPrice
seasonalDiscount = this.getSeasonalDiscount()
fees = this.getFees()
finalPrice = discountedPrice(basePrice, seasonalDiscount, fees)

# to
basePrice = quantity * itemPrice
finalPrice = discountedPrice(
    basePrice
)  # just call the queries inside the method, no need to pass other params

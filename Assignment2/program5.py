cost_price = float(input("Enter cost price: "))
discount = float(input("Enter discount (%): "))

selling_price = cost_price - (cost_price * discount / 100)

print("Selling Price =", selling_price)

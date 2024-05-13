import math

pi = math.pi
e = math.e
tau = math.tau
x = 81
y = 7
z = -23234.5454
angle = 45

print(pi)
print(e)
print(tau)
print(math.sqrt(x))
print(math.factorial(y))
print(math.floor(z))
print(math.degrees(y))
print(math.radians(angle))
print(" \n")
angle = math.radians(angle)

unit_price = 49.99
quantity = 30
print(f"Subtotal:  ${quantity * unit_price}")

print(f"Subtotal:  ${quantity * unit_price:,}")
print(" \n")

sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate:.2%}")
print(" \n")

unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
subtotal = unit_price * quantity
sales_tax = subtotal * sales_tax_rate
total = subtotal + sales_tax
output = f"""
Subtotal:       ${subtotal:,.2f}
Sales Tax:      ${sales_tax:,.2f}
Total:          ${total:,.2f}
"""
print(output)


print(" \n")
print(" The cosin of pi/4 in radians: ", math.cos(angle))
cosangle = math.cos(angle)
cosangle = math.degrees(cosangle)
print(" The cosin of pi/4 in degrees: ", cosangle)











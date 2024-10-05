""" Replace the literal values for the constants at the top (like MAX_INCREASE) with randomly generated values (
within sensible ranges)"""
import random

MAX_INCREASE = random.uniform(0.05, 0.20)  # 5-20%
MAX_DECREASE = random.uniform(0.05, 0.10)  # 5-10%
MIN_PRICE = random.uniform(0.01, 0.05)
MAX_PRICE = random.randint(80, 150)
INITIAL_PRICE = random.randint(1, 15)
FILENAME = "capitalist_conrad.txt"
days = 0
out_file = open(FILENAME, "w")
price = INITIAL_PRICE
print(f"Starting price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)
    days += 1
    price *= (1 + price_change)
    print(f"On day {days} the price is ${price:,.2f}", file=out_file)
out_file.close()

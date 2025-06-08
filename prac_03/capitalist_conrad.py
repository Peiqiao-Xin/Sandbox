"""

  # constants
  max_inc ← 0.1
  max_dec ← 0.05
  min_price ← 0.01
  max_price ← 1000.0
  init_price ← 10.0
  file ← open "stock_output.txt" for write

  price ← init_price
  day ← 0
  write file: "Starting price: $" + format(price)

  while price between min_price and max_price
    day ← day + 1
    if random_choice(1,2) = 1
      change ← uniform(0, max_inc)
    else
      change ← uniform(-max_dec, 0)
    price ← price * (1 + change)
    write file: "On day " + day + " price is: $" + format(price)
  end while
"""
import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
FILENAME = "stock_output.txt"

# open output file for writing (this creates a new file if it doesn't exist)
out_file = open(FILENAME, 'w')

price = INITIAL_PRICE
day = 0
# noinspection PyTypeChecker
print(f"Starting price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    day += 1
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

    price *= (1 + price_change)
    print(f"On day {day} price is: ${price:,.2f}", file=out_file)

# don't forget to close the file when we've finished with it
out_file.close()
"""

  price ← INITIAL_PRICE
  day ← 0
  open FILENAME for write as out
  write "Starting price: $" + format(price) to out
  while price between MIN_PRICE and MAX_PRICE
    day ← day + 1
    if rand(1,2)=1
      change ← rand_uniform(0, MAX_INCREASE)
    else
      change ← rand_uniform(-MAX_DECREASE, 0)
    price ← price * (1 + change)
    write "On day " + day + " price is: $" + format(price) to out
"""
import random

MAX_INCREASE = 0.1
MAX_DECREASE = 0.05
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
FILENAME = "stock_output.txt"

def main():
    price = INITIAL_PRICE
    day = 0
    with open(FILENAME, "w") as out_file:
        print(f"Starting price: ${price:,.2f}", file=out_file)
        while MIN_PRICE <= price <= MAX_PRICE:
            day += 1
            if random.randint(1,2) == 1:
                change = random.uniform(0, MAX_INCREASE)
            else:
                change = random.uniform(-MAX_DECREASE, 0)
            price *= (1 + change)
            print(f"On day {day} price is: ${price:,.2f}", file=out_file)

if __name__ == "__main__":
    main()
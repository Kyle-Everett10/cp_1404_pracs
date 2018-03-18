import random
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
days_of_simulation = 1
print("Starting price: ${}".format(price))

out_file = open("OUTPUT_FILE.txt", 'w')
while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(0, MAX_INCREASE)
    price *= (1+price_change)
    print("On day {}, the price is: ${:.2f}".format(days_of_simulation, price), file=out_file)
    days_of_simulation += 1
out_file.close()

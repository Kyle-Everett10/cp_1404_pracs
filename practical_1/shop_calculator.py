number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

total_price = 0.0
for i in range(number_of_items):
    item_price = float(input("Enter item price: $"))
    total_price += item_price

if total_price > 100:
    discount_price = total_price / 10
    total_price = total_price - discount_price

if number_of_items == 1:
    multiple_items = "item"
else:
    multiple_items = "items"

print("Total price for", number_of_items, "{} is ${:.2f}".format(multiple_items,total_price))

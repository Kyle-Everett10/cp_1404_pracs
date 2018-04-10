from prac_7.guitar import Guitar
guitar1 = Guitar("Gibson L-5 CES", 16035.40, 1922)
another_guitar = Guitar("Another Guitar", 500, 2013)
print("{} - expected True, got {}".format(guitar1.name, guitar1.is_vintage(guitar1.get_age())))
print("{} - expected False, got {}".format(another_guitar.name, another_guitar.is_vintage((another_guitar.get_age()))))

print("{} - expected 96 got {}".format(guitar1.name, guitar1.get_age()))
print("{} - expected 5, got {}".format(another_guitar.name, another_guitar.get_age()))

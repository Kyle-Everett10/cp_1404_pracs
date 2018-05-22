"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_7.Car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    words = []
    for word in range(n):
        words.append(s)
    return " ".join(words)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # TODO: 1. fix the repeat_string function above so that it passes the test
    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car("Rodeo")
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # TODO: 2. write assert statements to show if Car sets the fuel correctly
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car("blah", fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly"


run_tests()

# TODO: 3. Uncomment the following line and run the doctests
doctest.testmod()

# TODO: 4. Fix the failing is_long_word function
# (don't change the tests, but the function!)

# TODO: 5. Write and test a function to format a phrase as a sentence,
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests so that:
# 'hello' -> ''Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (that's valid!)
# then write the body of the function so that the tests pass


def format_sentence(string):
    """Formats a string into a sentence
    >>> format_sentence("this is a sentence")
    'This is a sentence.'
    >>> format_sentence("No need to fix this.")
    'No need to fix this.'
    >>> format_sentence("what ever, this stinks.")
    'What ever, this stinks.'
    >>> format_sentence("Capital letters are fun")
    'Capital letters are fun.'
    """
    new_string = ""
    new_string += string[:1].upper()
    new_string += string[1:]
    new_string += "."
    return new_string


print(format_sentence("whatever I want"))
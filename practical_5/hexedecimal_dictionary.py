COLOUR_HEXIDECIMAL_NUMBER = {"AliceBlue": "#f0f8ff", "Brown": "#a52a2a", "chartreuse1": "#7fff00", "coral": "#ff7f50",
                             "DarkGoldenrod": "#b8860b", "DarkGreen": "#006400", "DarkOrange": "#ff8c00",
                            "DarkSeaGreen": "#8fbc8f", "DarkSlateBlue": "#483d8b", "firebrick": "#b22222",
                             "ForestGreen": "#228b22"}

colour_input = input("Type in a colour name: ")
while input != "":
    if colour_input in COLOUR_HEXIDECIMAL_NUMBER:
        print("{} has the hexidecimal number of: {}".format(colour_input, COLOUR_HEXIDECIMAL_NUMBER[colour_input]))
    else:
        print("That colour is not in the current dictionary, please input a new colour name")
    colour_input = input("Type in a colour name: ")

print("Finished")
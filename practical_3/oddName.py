"""Kyle"""
def main():
    name = input("Enter your name here: ")
    while name == "":
        print("Not a valid name")
        name = input("Enter your name here: ")
    frequency = int(input("How frequent do you want the names to be taken?: "))
    print(extract_characters(name, frequency))


def extract_characters(name, frequency):
    characters = []
    for character in range(0, len(name), frequency):
            characters.append(name[character])
    extracted_characters = " ".join(characters)
    return extracted_characters


main()
print("Done")

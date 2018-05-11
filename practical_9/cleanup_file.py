"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('C:\\Users\\evere-ka12w\\Documents\\cp_1404_pracs\\practical_9\\Lyrics\\Lyrics\\Christmas')
    # print a list of all files (test)
    print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')

    # loop through each file in the (original) directory
    for filename in os.listdir('.'):
        # ignore directories, just process files
        if not os.path.isdir(filename):
            new_name = get_fixed_filename(filename)
            print(new_name)

            # NOTE: These options won't just work...
            # they show you ways of renaming and moving files,
            # but you need to have valid filenames. You can't make a file with
            # a blank name, and on Windows you can't have files with the same
            # characters but different case (e.g. a.TXT and A.txt)
            # So, you need to get valid filenames before you can use these.

            # Option 1: rename file to new name - in place
            # os.rename(filename, new_name)

            # Option 2: move file to new place, with new name
            # shutil.move(filename, 'temp/' + new_name)

            # Processing subdirectories using os.walk()

            # os.chdir('..')  # .. means "up" one directory
            # for dir_name, subdir_list, file_list in os.walk('.'):
            #     print("In", dir_name)
            #     print("\tcontains subdirectories:", subdir_list)
            #     print("\tand files:", file_list)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # First, replace the spaces and .TXT (the easy part)
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    # TODO: step-by-step, consider the problem cases and solve them

    new_name = ""
    for index, character in enumerate(filename):
        try:
            if character.isalpha() and filename[index+1].isalpha():
                if filename[index+1].isupper():
                    new_name += character
                    new_name += "_"
                else:
                    if index > 0:
                        if new_name[-1] == "_":
                            new_name += character.upper()
                        else:
                            new_name += character
                    else:
                        new_name += character
            else:
                new_name += character
        except IndexError:
            new_name += "t"

    return new_name


main()

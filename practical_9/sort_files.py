import shutil
import os


def main():
    os.chdir("FilesToSort")
    print("Currently in{}".format(os.getcwd()))
    for dir_name, dir_list, file in os.walk(os.getcwd()):
        extension_types_and_directory = create_directories(file)
        move_files(file, extension_types_and_directory)
    print("All sorted! Have a nice day!")


def create_directories(file):
    directories = []
    extensions = []
    extension_and_directory = {}
    for filename in file:
        name_and_extension = filename.split(".")
        if name_and_extension[1] not in extensions:
            extensions.append(name_and_extension[1])
    for extension in extensions:
        directory_for_extension = input("Where do you want {} files?: ".format(extension))
        extension_and_directory[extension] = directory_for_extension
        if directory_for_extension not in directories:
            directories.append(directory_for_extension)
    for directory in directories:
        os.mkdir(directory)
    return extension_and_directory


def move_files(file, dictionary):
    for filename in file:
        for extension in dictionary:
            if extension == filename.split(".")[1]:
                shutil.move(filename, dictionary.get(extension))

main()

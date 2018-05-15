import shutil
import os


def main():
    os.chdir("C:\\Users\\kaeve\\Documents\\Files to transfer")
    print("Currently in{}".format(os.getcwd()))
    for dir_name, dir_list, file_list in os.walk(os.getcwd()):
        extension_types_and_directory = create_directories(file_list)
        move_files(file_list, extension_types_and_directory)
    print("All sorted! Have a nice day!")


def create_directories(file_list):
    directories = []
    extensions = []
    extension_and_directory = {}
    for filename in file_list:
        extension = filename.split(".")[1]
        if extension not in extensions:
            extensions.append(extension)
            directory_for_extension = input("Where do you want {} files?: ".format(extension))
            extension_and_directory[extension] = directory_for_extension
            if directory_for_extension not in directories:
                directories.append(directory_for_extension)
                os.mkdir(directory_for_extension)
    return extension_and_directory


def move_files(file_list, dictionary):
    for filename in file_list:
        extension = filename.split(".")[1]
        if extension in dictionary:
            shutil.move(filename, dictionary.get(extension))


main()

import shutil
import os


def main():
    os.chdir("FilesToSort")
    print(os.getcwd())
    extension_and_directory = {}
    directories = []
    extensions = []
    for dir_name, dir_list, file in os.walk(os.getcwd()):
        for filename in file:
            name_and_extension = filename.split(".")
            print(name_and_extension)
            if name_and_extension[1] not in extensions:
                extensions.append(name_and_extension[1])
        for extension in extensions:
            directory_for_extension = input("Where do you want {} files?: ".format(extension))
            extension_and_directory[extension] = directory_for_extension
            if directory_for_extension not in directories:
                directories.append(directory_for_extension)
        for directory in directories:
            os.mkdir(directory)
        for filename in file:
            for extension in extension_and_directory:
                if extension == filename.split(".")[1]:
                    shutil.move(filename, extension_and_directory.get(extension))
    print("All sorted! Have a nice day!")

main()

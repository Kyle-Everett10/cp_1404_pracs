usernames = ["jimbo", "gilston98", "derekf", "WhatSup"]
attempted_name = input("Enter your user name: ")
access_granted = False
for username in usernames:
    if attempted_name == username:
        access_granted = True

if access_granted is True:
    print("Access Granted")
else:
    print("Access denied")

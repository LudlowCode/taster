import hashlib
import sys

hashed_string = input("Please input the hashed string: ")

file_found=False
string_found=False

while not file_found:
    filename = input("What's your dictionary text file (eg dictionary.txt)? ")   
    try:
        file = open(filename)
        file_found = True
    except:
        continue

while not string_found:
    try:
        current_word = str(file.readline()).strip()
        print("Trying: "+str(current_word))
        if str((hashlib.md5(current_word.encode('utf-8')).hexdigest()))==hashed_string:
            print("Answer:"+current_word)
            string_found=True
        if len(current_word)<1:
            print("Word not found in list")
            break
    except:
        print("Error:", sys.exc_info()[0])
        quit

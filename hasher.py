import hashlib
#hashedString = input("Please input the hashed string")


while True:
    unhashedString = input("Please input the string: ")
    print(hashlib.md5(unhashedString.encode('utf-8')).hexdigest())

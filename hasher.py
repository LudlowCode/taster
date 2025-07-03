import hashlib
#hashedString = input("Please input the hashed string")

def hash(unhashed_string):
    return hashlib.md5(unhashed_string.encode('utf-8')).hexdigest()

while True:
    entered_string = input("Please input the string: ")
    print(hash(entered_string))

import hashlib

def hash(unhashed_string):
    return hashlib.md5(unhashed_string.encode('utf-8')).hexdigest()

def pad_to_4_digits(int_to_pad):
    return str(int_to_pad).zfill(4)
    print("HI") 

while True:
    entered_string = input("Please guess the secret to receive a hash digest: ")
    print(hash(entered_string))


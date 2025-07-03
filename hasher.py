import hashlib

def hash(unhashed_string):
    return hashlib.md5(unhashed_string.encode('utf-8')).hexdigest()

# while True:
#     entered_string = input("Please input the string: ")
#     print(hash(entered_string))
counter=1
while counter <=9999:
    if hash("{:04d}".format(counter))=="43dd49b4fdb9bede653e94468ff8df1e":
        print(counter)
    counter+=1
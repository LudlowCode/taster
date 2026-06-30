################# DON'T BOTHER READING THIS SECTION ~##############################
import hashlib

def hash(unhashed_string):
    return hashlib.md5(unhashed_string.encode('utf-8')).hexdigest()
def pad_to_4_digits(int_to_pad):
    return str(int_to_pad).zfill(4)



################ THIS IS THE RELEVANT SECTION #####################################

hash1 = "81dc9bdb52d04dc20036dbd8313ed055"
hash2 = "43dd49b4fdb9bede653e94468ff8df1e"
hash3 = "4a7d1ed414474e4033ac29ccb8653d9b"
hash4 = "b26747fc8cb2170baa866b315cf58b7c"

attempt = 0

while attempt < 10: # this might need changing!
    actual_attempt = pad_to_4_digits(attempt)
    if hash(actual_attempt) == hash1:
        print("WE GOT ONE!")
        print(actual_attempt)
    attempt = attempt + 1
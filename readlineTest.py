import hashlib
import sys


filename = "adjectives.txt"   
try:
    file = open(filename,)
    file_found = True
except:
    print("Error")
i=0
while not i==10:
    current_word = file.readline()
    print("Trying: "+current_word)
    i+=1


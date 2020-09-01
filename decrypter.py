import time
import hashlib

from itertools import product
from string import ascii_lowercase

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
          ,"0","1","2","3","4","5","6","7","8","9",".","-","_",":",";"]

found_hash = None
word = ""

def decrypt_password(hash, length):
    global word, found_hash
    runtime = 0

    while True:

        for c in product(ascii_lowercase,repeat=length):

            word = ''.join(c)
            found_hash = hashlib.md5(str.lower(word)).hexdigest()

            print("checking... [" + str(word) + "] doesn't match")

            if hash == found_hash:
                print(word + " is the password \nRuntime: " + str(runtime))
                break

        break

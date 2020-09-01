import time
import hashlib

from itertools import product
from string import ascii_lowercase

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

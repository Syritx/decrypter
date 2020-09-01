import time
import hashlib as h

from itertools import product
from string import ascii_lowercase

found_hash = None
word = ""

def decrypt_password(hash):
    global word, found_hash
    max_length = 20

    while True:

        for l in range(max_length):
            for c in product(ascii_lowercase,repeat=l):
                word = ''.join(c)
                found_hash = h.md5(word).hexdigest()

                if hash == found_hash:
                    print(word + " is the password")
                    found = True
                    break
                else: print("checking [" + word + "]")

            if found:
                break
        break


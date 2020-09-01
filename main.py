import decryptor as d
import hashlib

password = "hello"
encrypted_password = hashlib.md5(str.lower(password)).hexdigest()

d.decrypt_password(encrypted_password,len(list(password)))
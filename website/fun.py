import hashlib

# hashing the password to database
def hash_pass(string):
    salt = "n72ZtCNReDyteD2ABECe"
    pw = string+salt
    h = hashlib.md5(pw.encode())
    return h.hexdigest()


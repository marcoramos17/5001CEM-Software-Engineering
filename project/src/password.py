# For secure salt generation
import secrets
# For hashing algorithms
import hashlib

def generate_salt() -> str:
    # Create byte string of length 32 which is considered
    #   reasonably cryptographically secure according
    #   to the 'secrets' module docs which can be found at
    #   https://docs.python.org/3/library/secrets.html
    return secrets.token_hex(32)

def hash_password(f_pwd: str, f_salt: str) -> bytes:
    # Generate a password, given an input, and a salt
    # We are using SHA256, and running 100000 times
    f_hashedPassword = hashlib.pbkdf2_hmac(
        'sha256', 
        f_pwd.encode('utf-8'), 
        bytes.fromhex(f_salt), 
        100000)
    return f_hashedPassword

# Example uses of the above functions

if __name__ == "__main__":
    print("Password file ran from main!\n"
          "This file defines functions to generate salts\n"
          "and hash passwords, it also shows how to use the\n"
          "same function to check a password.\n")
    ## Create a constant salt for testing
    ex1_salt = generate_salt()
    ## Create our true hashed
    ex1_hashed = hash_password('test1234', ex1_salt)

    ## Compare true hash to other input passwords
    ### True password   (True)
    print(ex1_hashed == hash_password('test1234', ex1_salt))
    ### Wrong salt      (False)
    print(ex1_hashed == hash_password('test1234', generate_salt()))
    ### Wrong password  (False)
    print(ex1_hashed == hash_password('4',        ex1_salt))
    ### Wrong password  (False)
    print(ex1_hashed == hash_password('test123',  ex1_salt))
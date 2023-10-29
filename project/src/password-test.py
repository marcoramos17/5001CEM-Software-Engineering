import unittest
from password import *

salt = generate_salt()
# Test a standard password
stdHashed = hash_password('test123456', salt)
# Test password of min length 
minHashed = hash_password('12345678', salt)
# Test a password of max length
maxHashed = hash_password('123456789abcdefghikl', salt)
# Test password with symbols
symHashed = hash_password('123456$"£^$(^', salt)

passwords = {'test123456' : stdHashed,
             '12345678': minHashed,
             '123456789abcdefghikl' : maxHashed,
             '123456$"£^$(^' : symHashed}

class PasswordTesting(unittest.TestCase):
    # Test that salts are created
    def test_salt_generation(self):
        # Define our hex check
        hex_check = None
        try:
            # If the salt is a hex value, then update
            hex_check = int(salt, 16)
        except Exception:
            # Else ignore
            pass
        # Check that salt is in hex
        self.assertIsNotNone(hex_check)
        # This really follows, but oh well
        self.assertIsNotNone(salt)
        # Check types
        self.assertEqual(type(salt), str)


    def test_salt_length(self):
        # Check lengths
        self.assertEqual(len(bytes.fromhex(salt)), 32)

    def test_correct_password(self):
        # Test that each hashed password passes when checked
        for password, hash in passwords.items():
            with self.subTest(password = password, hash = hash):
                self.assertEqual(hash_password(password, salt), hash)

    def test_incorrect_password(self):
        # Test that when comparing password to wrong
        #   password the hashes should not match
        for password, hash in passwords.items():
            with self.subTest(password = password):
                self.assertNotEqual(hash_password(password + "blah", salt), hash)


    def test_incorrect_salt(self):
        # Check that incorrect salts fail the hashing
        for password, hash in passwords.items():
            with self.subTest(password = password):
                self.assertNotEqual(hash_password(password, generate_salt()), hash)
        

    def test_incorrect_pair(self):
        # Test that when both portions are wrong the test fails
        for password, hash in passwords.items():
            with self.subTest(password = password):
                self.assertNotEqual(hash_password(password + "blah", generate_salt()), hash)

if __name__ == '__main__':
    unittest.main()
import base64
import hashlib
import os


class PasswordHelper:
    def get_hash(self, plain):
        plain_bytes = plain.encode('utf-8')
        return hashlib.sha512(plain_bytes).hexdigest()
    
    def get_salt(self):
        return str(base64.b64encode(os.urandom(20)))
    
    def validate_password(self, plain, salt, expected):
        return self.get_hash(plain + salt) == expected

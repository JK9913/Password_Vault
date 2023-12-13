from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64, os
import hashlib

# This is a function that will derive the key in real time. This is so that the key won't have to be stored in a datatable as that is very unsecure.
def derive_key(user_password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(user_password.encode()))
    return key


def encrypt_data(data_to_encrypt, key):
    cipher = Fernet(key)
    return cipher.encrypt(data_to_encrypt.encode())


def decrypt_data(data_to_decrypt, key):
    cipher = Fernet(key)
    return cipher.decrypt(data_to_decrypt).decode()

def create_random_salt():
    salt = os.urandom(16)
    return salt.hex()

def hash_password(password):
    password_encode = password.encode("utf-8")
    password_hash = hashlib.sha256(password_encode).hexdigest()

    return password_hash

#print(create_random_salt())

#hidden_data = "Testing"
#key = derive_key('Password123',b'12ffrgssdf21')

#print(f"Original data: {hidden_data}")
#print(f"Encrypted ciphertext: {encrypt_data(hidden_data, key)}")
#print("Decrypted data: " + decrypt_data(encrypt_data(hidden_data, key), key))



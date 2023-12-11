from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64

def derive_key_from_password(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Use a key size compatible with Fernet (256 bits)
        salt=salt,
        iterations=100000,  # Adjust based on desired computational cost
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

# Example usage:
password = "user_password"
user_salt = b'user_unique_salt'

# Derive key from password and salt
key = derive_key_from_password(password, user_salt)

# Use the key with Fernet for encryption and decryption
cipher = Fernet(key)
plaintext = "Sensitive information"
encrypted_data = cipher.encrypt(plaintext.encode())
decrypted_data = cipher.decrypt(encrypted_data).decode()

print("Original Data:", plaintext)
print("Encrypted Data:", encrypted_data)
print("Decrypted Data:", decrypted_data)
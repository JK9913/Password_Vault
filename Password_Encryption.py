from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import urlsafe_b64decode, urlsafe_b64encode

# This is a function that will derive the key in real time. This is so that the key won't have to be stored in a datatable as that is very unsecure.
def derive_key(user_password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    return urlsafe_b64decode(kdf.derive(user_password.encode()))


def encrypt_data(data_to_be_encrypted, master_password, salt):
    key = derive_key(master_password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CFB8(), backend=default_backend()) # CF = Cipher Feedback with size 8 bits, backend spcifies the cryptographic backend to be used.
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data_to_be_encrypted.encode()) + encryptor.finalize()

    return urlsafe_b64encode(ciphertext)

def decrypt_data(data_to_be_decrypted, master_password, salt):
    # Creating the key using the derive_key function
    key = derive_key(master_password, salt)
    # Create the cipher text
    cipher = Cipher(algorithms.AES(key), modes.CFB8(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(urlsafe_b64decode(data_to_be_decrypted)) + decryptor.finalize()
    
    return decrypted_data.decode()

password = "12341234"
salt = b'salting'

original_data = "testingPassword"
encrypted_data = encrypt_data(original_data, password, salt)

decrypted_data = decrypt_data(encrypted_data, password, salt)

print("Original Data:", original_data)
print("Encrypted Data:", encrypted_data)
print("Decrypted Data:", decrypted_data)



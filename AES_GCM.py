#_AES_GCM
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

def encrypt(plaintext, password):
    print("Step 1: Generating a random Initialization Vector (IV)...")
    iv = os.urandom(12)
    print("IV:", iv.hex())
    
    print("\nStep 2: Deriving a key from the provided password using PBKDF2 with SHA256...")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 256 bits
        salt=os.urandom(16),
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    print("Derived key:", key.hex())
    
    print("\nStep 3: Creating AES-GCM cipher with the derived key and IV...")
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    print("\nStep 4: Encrypting the plaintext using AES-GCM...")
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    print("Ciphertext:", ciphertext.hex())
    
    print("\nStep 5: Getting the authentication tag...")
    tag = encryptor.tag
    print("Tag:", tag.hex())
    
    print("\nEncryption completed successfully!")
    
    return iv, ciphertext, tag

def decrypt(iv, ciphertext, tag, password):
    print("\nStep 1: Deriving a key from the provided password using PBKDF2 with SHA256...")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 256 bits
        salt=os.urandom(16),
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    print("Derived key:", key.hex())
    
    print("\nStep 2: Creating AES-GCM cipher with the derived key, IV, and authentication tag...")
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    
    print("\nStep 3: Decrypting the ciphertext using AES-GCM...")
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    print("Plaintext:", plaintext.decode())
    
    print("\nDecryption completed successfully!")
    
    return plaintext

# Example usage
plaintext = b"Hello, AES-GCM!"
password = "my_password"

print("Encrypting the plaintext...")
iv, ciphertext, tag = encrypt(plaintext, password)

print("\nDecrypting the ciphertext...")
decrypted_text = decrypt(iv, ciphertext, tag, password)

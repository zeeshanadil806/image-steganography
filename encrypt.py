from cryptography.fernet import Fernet

# Generate a new key and store it securely
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_message(message):
    return cipher.encrypt(message.encode())

def decrypt_message(encrypted_message):
    return cipher.decrypt(encrypted_message).decode()

# Example Usage
# encrypted = encrypt_message("Hello Secret")
# print(decrypt_message(encrypted))

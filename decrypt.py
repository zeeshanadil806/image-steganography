from cryptography.fernet import Fernet

# Make sure to use the same key as encryption!
key = Fernet.generate_key()
cipher = Fernet(key)

def decrypt_message(encrypted_message):
    try:
        return cipher.decrypt(encrypted_message).decode()
    except:
        return "❌ Decryption Failed! Invalid Key or Corrupted Data."

# Example Usage
# encrypted = encrypt_message("Hello Secret")
# print(decrypt_message(encrypted))

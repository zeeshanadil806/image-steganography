from encode import encode_image
from decode import decode_image
from encrypt import encrypt_message
from decrypt import decrypt_message
from detect import detect_steganography
def main():
    print("\n🔒 Advanced Steganography Tool 🔒")
    print("1. Encode a Message into an Image")
    print("2. Decode a Hidden Message from an Image")
    print("3. Encrypt a Message")
    print("4. Decrypt a Message")
    print("5. Detect Steganography in an Image")
    print("6. Exit")
    
    choice = input("\nEnter your choice: ")
    if choice == "1":
        image_path = input("Enter image file path: ")
        message = input("Enter message to hide: ")
        output_path = "stego_image.png"
        encode_image(image_path, message, output_path)
        print(f"✅ Message encoded and saved as {output_path}")
    
    elif choice == "2":
        image_path = input("Enter image file path: ")
        decoded_message = decode_image(image_path)
        print(f"✅ Hidden Message: {decoded_message}")
    
    elif choice == "3":
        message = input("Enter message to encrypt: ")
        encrypted_msg = encrypt_message(message)
        print(f"✅ Encrypted Message: {encrypted_msg}")
    
    elif choice == "4":
        encrypted_msg = input("Enter encrypted message: ")
        decrypted_msg = decrypt_message(encrypted_msg.encode())
        print(f"✅ Decrypted Message: {decrypted_msg}")
    
    elif choice == "5":
        image_path = input("Enter image file path: ")
        detect_steganography(image_path)
    
    elif choice == "6":
        print("Exiting... ✅")
        exit()
    
    else:
        print("❌ Invalid Choice! Please Try Again.")

if __name__ == "__main__":
    main()

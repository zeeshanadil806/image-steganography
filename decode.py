from PIL import Image

def decode_image(image_path):
    img = Image.open(image_path)
    if img.mode == 'RGBA':
        img = img.convert('RGB')

    pixels = img.load()
    
    binary_message = ""
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            binary_message += str(r & 1)  # Extract LSB
    
    # Convert binary to text
    message_bits = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message = ''.join(chr(int(b, 2)) for b in message_bits)
    print(message_bits)
    # Stop at the end marker
    if 'þ' in message:
        message = message.split('þ')[0]

    print("✅ Decoded Message:", message)
    return message

from PIL import Image

def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    binary_message = ''.join(format(ord(i), '08b') for i in message) + '1111111111111110'  # End marker
    pixels = img.load()
    print("Binary Message :",binary_message)

    idx = 0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if idx < len(binary_message):
                r, g, b = pixels[i, j]
                r = (r & 0xFE) | int(binary_message[idx])  # Modify LSB
                pixels[i, j] = (r, g, b)
                idx += 1

    img.save(output_path)
    print(f"✅ Message encoded and saved to {output_path}")
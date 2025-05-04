import tkinter as tk
from tkinter import filedialog
from encode import encode_image
from decode import decode_image

def browse_file():
    filename = filedialog.askopenfilename()
    return filename

def encode_action():
    image_path = browse_file()
    message = input("Enter message: ")
    encode_image(image_path, message, "stego_image.png")
    print("Encoding Complete.")

def decode_action():
    image_path = browse_file()
    print("Decoded Message:", decode_image(image_path))

root = tk.Tk()
root.title("Steganography Tool")

tk.Button(root, text="Encode Message", command=encode_action).pack()
tk.Button(root, text="Decode Message", command=decode_action).pack()

root.mainloop()

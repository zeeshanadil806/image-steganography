import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_steganography(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply DCT (Discrete Cosine Transform) to detect anomalies
    dct_transformed = cv2.dct(np.float32(img))
    plt.imshow(dct_transformed, cmap='gray')
    plt.title('Steganography Detection')
    plt.show()
    
    print("If you see unusual pixel patterns, steganography might be used.")

# Example Usage
# detect_steganography('output.png')

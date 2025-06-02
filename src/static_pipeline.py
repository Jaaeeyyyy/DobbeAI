import cv2
import numpy as np

def static_process(image):
    # Ensure grayscale
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Normalize to 8-bit uint if needed
    if image.dtype != np.uint8:
        image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    # Histogram Equalization
    equalized = cv2.equalizeHist(image)

    return equalized

import cv2
import numpy as np
import os

def visualize_comparison(original, static_img, adaptive_img, filename=None):
    # Ensure all images are uint8 grayscale
    images = []
    for img in [original, static_img, adaptive_img]:
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if img.dtype != np.uint8:
            img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        images.append(img)

    # Resize to same dimensions
    height = min(img.shape[0] for img in images)
    width = min(img.shape[1] for img in images)
    images = [cv2.resize(img, (width, height)) for img in images]

    comparison = cv2.hconcat(images)

    if filename:
        cv2.imwrite(filename, comparison)
    else:
        cv2.imshow("Comparison: Original | Static | Adaptive", comparison)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

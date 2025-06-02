import numpy as np
import cv2

def compute_brightness(image):
    return np.mean(image)

def compute_rms_contrast(image):
    return np.std(image)

def compute_laplacian_variance(image):
    lap = cv2.Laplacian(image, cv2.CV_64F)
    return lap.var()

def compute_noise_estimation(image):
    lap = cv2.Laplacian(image, cv2.CV_64F)
    noise = np.median(np.abs(lap - np.median(lap)))
    return noise

def compute_all_metrics(image):
    brightness = compute_brightness(image)
    contrast = compute_rms_contrast(image)
    sharpness = compute_laplacian_variance(image)
    noise = compute_noise_estimation(image)
    return {'brightness': brightness, 'contrast': contrast, 'sharpness': sharpness, 'noise': noise}

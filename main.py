import argparse
import os
import cv2  # For saving images
from src.dicom_utils import read_dicom
from src.static_pipeline import static_process
from src.adaptive_pipeline import adaptive_process
from src.image_metrics import compute_all_metrics
from src.evaluator import visualize_comparison

def process_images(input_path, mode):
    files = [f for f in os.listdir(input_path) if f.endswith('.dcm')]
    processed_dir = os.path.join('results', 'processed')
    comparison_dir = os.path.join('results', 'comparison')
    os.makedirs(processed_dir, exist_ok=True)
    os.makedirs(comparison_dir, exist_ok=True)

    for f in files:
        print(f"Processing {f} ...")
        image, ds = read_dicom(os.path.join(input_path, f))

        static_img = static_process(image)

        if mode == 'static':
            processed = static_img
        else:
            metrics = compute_all_metrics(image)
            processed = adaptive_process(image)

        # Save processed image
        processed_save_path = os.path.join(processed_dir, os.path.splitext(f)[0] + '_processed.png')
        if processed.dtype != 'uint8':
            processed = cv2.normalize(processed, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')
        cv2.imwrite(processed_save_path, processed)

        # Save comparison image
        comparison_save_path = os.path.join(comparison_dir, os.path.splitext(f)[0] + '_comparison.png')
        visualize_comparison(image, static_img, processed, filename=comparison_save_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dental X-ray Preprocessing Pipeline")
    parser.add_argument('--input', type=str, required=True, help='Input folder containing DICOM images')
    parser.add_argument('--mode', choices=['static', 'adaptive'], default='adaptive', help='Processing mode')
    args = parser.parse_args()
    process_images(args.input, args.mode)

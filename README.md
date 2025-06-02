
# DobbeAI Dental X-ray Preprocessing Pipeline

## Problem Understanding
This project aims to preprocess dental X-ray images to enhance their quality before downstream analysis such as caries detection or bone loss assessment. The preprocessing includes static and adaptive pipelines to improve image clarity, contrast, and noise reduction. Effective preprocessing helps improve the performance of AI models analyzing these images.

## Dataset Description
The dataset contains dental X-ray images in both DICOM (.dcm) and RVG (.rvg) formats. Note that RVG files were manually converted to DICOM format before processing to maintain compatibility with the pipeline, as direct RVG handling is not supported in this project.

## Methodology

### Image Quality Metrics
Several image quality metrics such as brightness, contrast, and sharpness (via Laplacian variance) are computed to inform the adaptive preprocessing pipeline.

### Static Preprocessing Baseline
The static pipeline applies fixed image enhancement methods such as histogram equalization and CLAHE to all images uniformly.

### Adaptive Preprocessing Pipeline
The adaptive pipeline uses computed image quality metrics to decide dynamically which enhancement steps to apply per image. For example, images with low sharpness or contrast may undergo stronger enhancement steps.

### Machine Learning / Deep Learning Approach
(Not implemented in this version; the framework can be extended to include ML/DL models for adaptive parameter tuning or image enhancement.)

## Results & Evaluation
- Quantitative metrics were calculated but not included here for brevity.
- Visual comparisons between Original, Static, and Adaptive processed images are saved in `results/comparisons`.
- Processed images are saved in `results/processed`.

## Discussion & Future Work
Challenges included handling different file formats and ensuring image data types compatibility with OpenCV functions. Future improvements may include automated RVG conversion, ML-based adaptive enhancement, and integration with downstream diagnostic models.

## Instructions

### Environment Setup
1. Create and activate a virtual environment.
2. Install dependencies using: pip install -r requirements.txt
   
### Running the Pipeline
Run the main script with: python main.py --input dataset_folder --mode adaptive


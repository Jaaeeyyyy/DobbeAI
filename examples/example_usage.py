from src.dicom_utils import read_dicom
from src.static_pipeline import static_process
from src.adaptive_pipeline import adaptive_process
from src.evaluator import visualize_comparison

image, ds = read_dicom('dataset/sample.dcm')
static_img = static_process(image)
adaptive_img = adaptive_process(image)
visualize_comparison(image, static_img, adaptive_img)

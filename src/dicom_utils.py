import pydicom
import numpy as np

def read_dicom(path):
    ds = pydicom.dcmread(path)
    img = ds.pixel_array
    if ds.PhotometricInterpretation == "MONOCHROME1":
        img = np.max(img) - img
    img = img.astype('uint8')
    return img, ds

import numpy as np

def calculate_contrast(img) -> int:
	"""
	Calculate the contrast of a grayscale image.
	Args:
		img (numpy.ndarray): 2D array representing a grayscale image with pixel values between 0 and 255.
	"""
	min_val = 255
    max_val = 0
    for i in img:
        for e in i:
            min_val = min(e, min_val)
            max_val = max(e, max_val)
    return max_val - min_val
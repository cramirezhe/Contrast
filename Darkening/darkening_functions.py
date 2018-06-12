import cv2
import numpy as np

# for the moment assume that the input image is uint8
lamb = 255.0

def cos_darkening(image):
	# Make sure you are using a Numpy Array
	if not isinstance(image, np.ndarray):
		return None
	# return the processed image
	z = lamb * (1.0 - np.cos(np.pi*image.astype("float")/(2*lamb)))
	return z.astype("uint8")
	
	
def exp_darkening(image, alpha=1.0):
	# Make sure you are using a Numpy Array
	if not isinstance(image, np.ndarray):
		return None
	# return the processed image
	A = lamb/(np.exp(alpha) - 1.0)
	z = A * (np.exp(alpha * image.astype("float")/lamb) - 1.0)
	return z.astype("uint8")
	



import cv2
import numpy as np

lamb = 255.0

def log_lighten(image, alpha=1.0, isFloat=False):
	if not isinstance(image, np.ndarray):
		print("The first parameter must be a numpy array")
		return None
	if alpha < 1.0:
		print("alpha must be greater than one... Changing the value to 1.0")
		alpha = 1.0
	A = lamb / np.log(alpha * lamb + 1.0)
	z = A * np.log(alpha * image + 1)
	if isFloat:
		return z
	return z.astype(np.uint8)

def sin_lighten(image, isFloat=False):
	if not isinstance(image, np.ndarray):
		print("The image must be a numpy array")
		return None
	z = lamb * np.sin(np.pi * image / (2 * lamb))
	if isFloat:
		return z
	return z.astype(np.uint8)

def exp_lighten(image, alpha=1.0, isFloat=False):
	if not isinstance(image, np.ndarray):
		print("The first parameter must be a numpy array")
		return None
	if alpha <= 0:
		print("The second parameter must be greater than zero... Changing the value to default value")
		alpha = 0.5
	alpha = float(alpha)
	A = lamb / (1 - np.exp(-alpha))
	temp = alpha * image / lamb
	z = A * (1 - np.exp(-temp))
	if isFloat:
		return z
	return z.astype(np.uint8)

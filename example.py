# Author Carlos Ramirez
import cv2
from Darkening import cos_darkening
from Darkening import exp_darkening

image = cv2.imread('./image.jpg')

cosImage = cos_darkening(image)
expImage = exp_darkening(image, 2.2)

cv2.imshow("cos", cosImage)
cv2.imshow("exp", expImage)
cv2.waitKey(0)


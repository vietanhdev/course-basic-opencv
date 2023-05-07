import cv2
import numpy as np

# Read an image
img = cv2.imread('stop-sign.jpeg')

# Convert the image to the HSV color space
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the range of red color in HSV
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv_img, lower_red, upper_red)

lower_red = np.array([170, 50, 50])
upper_red = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv_img, lower_red, upper_red)

# Combine the two masks
mask = cv2.bitwise_or(mask1, mask2)

# Apply the mask to the original image
res = cv2.bitwise_and(img, img, mask=mask)

# Show the result
cv2.imshow('Image', img)
cv2.imshow('Mask', mask)
cv2.imshow('Result', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

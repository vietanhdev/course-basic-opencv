import cv2
import numpy as np

# Read the image
img = cv2.imread("wood_blur.png")

# Define the kernel for high-pass filtering
kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

# Apply the high-pass filter
sharpened_img = cv2.filter2D(img, -1, kernel)

# Display the result
cv2.imshow("Original Image", img)
cv2.imshow("High-pass Filtering", sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# Read an image
original_img = cv2.imread("stop-sign.jpeg")
img = original_img.copy()

# Scale the values of the red, green, and blue channels
img[:, :, 0] = img[:, :, 0] * 0.8  # Red channel
img[:, :, 1] = img[:, :, 1] * 1.05  # Green channel
img[:, :, 2] = img[:, :, 2] * 0.8  # Blue channel

# Show the result
cv2.imshow("Image", original_img)
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

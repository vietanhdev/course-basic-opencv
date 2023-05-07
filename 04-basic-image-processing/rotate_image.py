import cv2

# Read an image
img = cv2.imread("fruits.jpeg")

# Rotate the image
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Display the rotated image
cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image", rotated_img)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

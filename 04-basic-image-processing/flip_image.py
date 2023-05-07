import cv2

# Read an image
img = cv2.imread("fruits.jpeg")

# Flip the image horizontally
flipped_img = cv2.flip(img, 1)

# Display the flipped image
cv2.imshow("Original Image", img)
cv2.imshow("Flipped Image", flipped_img)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

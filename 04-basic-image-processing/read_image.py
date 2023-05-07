import cv2

# Read an image
img = cv2.imread("fruits.jpeg")

# Display the image
cv2.imshow("Image", img)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

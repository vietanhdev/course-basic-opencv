import cv2

# Read an image
img = cv2.imread("fruits.jpeg")

# Select a region of interest
roi = img[338:490, 320:480]

# Display the cropped image
cv2.imshow("Original Image", img)
cv2.imshow("Cropped Image", roi)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

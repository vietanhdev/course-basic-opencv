import cv2

# Read an image
img = cv2.imread("wood_blur.png")

# Apply Laplacian filter
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# Add the Laplacian filter output to the original image
sharpened_img = cv2.add(img, laplacian, dtype=cv2.CV_8UC3)

# Display the results
cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

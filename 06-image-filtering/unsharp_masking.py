import cv2

# Read an image
img = cv2.imread("wood_blur.png")

# Apply gaussian blur
blurred = cv2.GaussianBlur(img, (7, 7), 0)

# Calculate the unsharp image
sharpened_img = cv2.addWeighted(img, 2.0, blurred, -1.0, 0)

# Display the results
cv2.imshow("Original Image", img)
cv2.imshow("Unsharp Masking", sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

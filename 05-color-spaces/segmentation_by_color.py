import cv2

# Read a grayscale image
img = cv2.imread("ball.jpeg", cv2.IMREAD_GRAYSCALE)

# Apply Otsu's thresholding
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Show the result
cv2.imshow("Image", img)
cv2.imshow("Result", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

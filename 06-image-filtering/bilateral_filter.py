import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load and blur image
img = cv.imread('wood_gauss.jpg')
img2 = cv.imread('wood_salt_and_pepper.jpg')
blur = cv.bilateralFilter(img,9,75,75)
blur2 = cv.bilateralFilter(img2,9,75,75)

# Convert color from bgr (OpenCV default) to rgb
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
blur_rgb = cv.cvtColor(blur, cv.COLOR_BGR2RGB)
img_rgb2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)
blur_rgb2 = cv.cvtColor(blur2, cv.COLOR_BGR2RGB)

# Display
plt.subplot(221),plt.imshow(img_rgb),plt.title('Gauss Noise')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(blur_rgb),plt.title('Gauss Noise - Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img_rgb2),plt.title('Salt&Pepper Noise')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(blur_rgb2),plt.title('Salt&Pepper Noise - Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

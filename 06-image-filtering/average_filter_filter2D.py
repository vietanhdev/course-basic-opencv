import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load and blur image
img = cv.imread('rose_gauss.jpg')
img2 = cv.imread('rose_salt_and_pepper.jpg')
kernel = np.ones((5,5),np.float32)/25
blur = cv.filter2D(img,-1,kernel)
blur2 = cv.filter2D(img2,-1,kernel)

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

#High Pass filtering
import cv2
import numpy as np
from matplotlib import pyplot as plt

radius=10
image = cv2.imread('messi5.jpg',0)
fft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
        # Centralize fft, the generated dshift is still a three-dimensional array
dshift = np.fft.fftshift(fft)

        # Get the center pixel
rows, cols = image.shape[:2]
mid_row, mid_col = int(rows / 2), int(cols / 2)

        # Build mask, 256 bits, two channels
mask = np.zeros((rows, cols, 2), np.float32)
mask[mid_row - radius:mid_row + radius, mid_col - radius:mid_col + radius] = 1

        # Multiply the Fourier transform result by a mask
fft_filtering = dshift * mask
        # Inverse Fourier transform
ishift = np.fft.ifftshift(fft_filtering)
image_filtering = cv2.idft(ishift)
image_filtering = cv2.magnitude(image_filtering[:, :, 0], image_filtering[:, :, 1])
        # Normalize the inverse transform results (generally normalize the last step of image processing, except in special cases)
cv2.normalize(image_filtering, image_filtering, 0, 1, cv2.NORM_MINMAX)


plt.subplot(131),plt.imshow(image,  cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(image_filtering, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])

plt.show()
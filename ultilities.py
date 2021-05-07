import numpy as np
import cv2
import math
from matplotlib import pyplot as plt

def hpf(image, radius):
    n=1

    fft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
            # Centralize fft, the generated dshift is still a three-dimensional array
    dshift = np.fft.fftshift(fft)

            # Get the center pixel
    rows, cols = image.shape[:2]
    mid_row, mid_col = int(rows / 2), int(cols / 2)

            # Build ButterWorth high-pass filter mask

    mask = np.zeros((rows, cols, 2), np.float32)
    for i in range(0, rows):
        for j in range(0, cols):
                            # Calculate the distance from (i, j) to the center
            d = math.sqrt(pow(i - mid_row, 2) + pow(j - mid_col, 2))
            try:
                mask[i, j, 0] = mask[i, j, 1] = 1 / (1 + pow(radius / d, 2*n))
            except ZeroDivisionError:
                mask[i, j, 0] = mask[i, j, 1] = 0
            # Multiply the Fourier transform result by a mask
    fft_filtering = dshift * mask
            # Inverse Fourier transform
    ishift = np.fft.ifftshift(fft_filtering)
    image_filtering = cv2.idft(ishift)
    image_filtering = cv2.magnitude(image_filtering[:, :, 0], image_filtering[:, :, 1])
            # Normalize the inverse transform results (generally normalize the last step of image processing, except in special cases)
    cv2.normalize(image_filtering, image_filtering, 0, 1, cv2.NORM_MINMAX)

    return image_filtering

def lpf(image, radius):
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

    return image_filtering

if __name__ == '__main__':
    image = cv2.imread('messi5.jpg',0)
    lps_input = lpf(image,50)
    hps_input = hpf(image,50)
    print(image)
    print(lps_input)
    print(hps_input)
    plt.subplot(121),plt.imshow(image, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(lps_input, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

    plt.subplot(121),plt.imshow(image, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(hps_input, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()
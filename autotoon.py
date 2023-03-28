import cv2 as cv
import numpy as np

img = cv.imread('image.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edge = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 5)

edges = cv.dilate(edge, np.ones((9, 9), np.uint8))

color = cv.bilateralFilter(img, 15, 100, 10)
cartoon = cv.stylization(color, sigma_s=100, sigma_r=0.5)
cartoon2 = cv.stylization(color, sigma_s=1, sigma_r=100)

cv.imwrite('output.jpg', cv.bitwise_or(cartoon, cartoon2, mask=edges))
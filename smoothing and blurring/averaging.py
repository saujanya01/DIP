import cv2
import numpy as np
img=cv2.imread("/home/saujanya/OCR/practice/test_images/lion.jpg")
cv2.imshow("Original",img)
blur=cv2.blur(img,(15,15))
cv2.imshow("Averaging",blur)
blur=cv2.GaussianBlur(img,(15,15),0)
cv2.imshow("Gaussian Blur",blur)
blur=cv2.medianBlur(img,15)
cv2.imshow("Median Blur",blur)
blur=cv2.bilateralFilter(img,155,21,21)
cv2.imshow("Bilateral Filter",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
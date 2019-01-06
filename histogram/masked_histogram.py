from matplotlib import pyplot as plt
import cv2
import numpy as np
import plot_hist
img=cv2.imread("/home/saujanya/OCR/practice/test_images/lion.jpg")
cv2.imshow("Original",img)
mask=np.zeros(img.shape[:2],dtype="uint8")
cv2.rectangle(mask,(150,150),(600,600),255,-1)
cv2.imshow("Mask",mask)
plot_hist.color_hist(img,"Color Histogram",mask=mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
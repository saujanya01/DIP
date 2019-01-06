import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('/home/saujanya/OCR/practice/test_images/lion.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
eq=cv2.equalizeHist(img)
cv2.imshow("EQ",eq)
cv2.imshow("Equalised image",np.hstack([img,eq]))
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.figure()
plt.title("eq")
plt.xlabel("bins")
plt.ylabel("no of pixels")
hist=cv2.calcHist(eq,[0],None,[256],[0,256])
plt.plot(hist)
plt.show()

plt.figure()
plt.title("original image")
plt.xlabel("bins")
plt.ylabel("no of pixels")
hist=cv2.calcHist(img,[0],None,[256],[0,256])
plt.plot(hist)
plt.show()

plt.figure()
plt.title("Original image and eq")
plt.xlabel("bins")
plt.ylabel("no of pixels")
hist=cv2.calcHist(np.hstack([img,eq]),[0],None,[256],[0,256])
plt.plot(hist)
plt.show()
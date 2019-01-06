from matplotlib import pyplot as plt
import cv2
img=cv2.imread("/home/saujanya/OCR/practice/test_images/lion.jpg")
cv2.imshow("Original",img)

#Grayscale Histogram
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hist=cv2.calcHist(img,[0],None,[256],[0,256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
from matplotlib import pyplot as plt
import cv2
img=cv2.imread('/home/saujanya/OCR/practice/test_images/lion.jpg')
fig=plt.figure()
plt.title('3D Histogram')
plt.xlabel('x')
plt.ylabel('y')
hist=cv2.calcHist([img],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])
plt.show()
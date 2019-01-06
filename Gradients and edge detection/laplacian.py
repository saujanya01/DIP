import cv2
import numpy as np
img=cv2.imread("/home/saujanya/OCR/practice/test_images/coins.jpg")
cv2.imshow("Original",img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
lap=cv2.Laplacian(gray,cv2.CV_64F)
final=np.uint8(np.absolute(lap))
cv2.imshow("Final Image",final)
cv2.waitKey(0)
cv2.destroyAllWindows()
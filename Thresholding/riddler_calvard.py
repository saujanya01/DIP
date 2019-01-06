import cv2
import mahotas
import numpy as np
img=cv2.imread("/home/saujanya/OCR/practice/test_images/coins.jpg")
cv2.imshow("Original",img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gblur=cv2.GaussianBlur(img,(5,5),0)
T=mahotas.thresholding.rc(gblur)
print("Riddler Calvard : {}".format(T))
thresh=img.copy()
thresh[thresh>T]=255
thresh[thresh<255]=0
#thresh=cv2.bitwise_not(thresh)
cv2.imshow("Riddler Calvard",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
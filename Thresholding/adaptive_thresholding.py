import cv2
img=cv2.imread("/home/saujanya/OCR/practice/test_images/coins.jpg")
cv2.imshow('Original',img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Using Gaussian Blur Method
gblur=cv2.GaussianBlur(gray,(11,11),0)
cv2.imshow('Gaussian Blur',gblur)
#Simple mean method
thresh=cv2.adaptiveThreshold(gblur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow('Gaussian Blur,Simple Mean',thresh)
#Gaussian Mean Method or Weighted Mean Method
thresh=cv2.adaptiveThreshold(gblur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,15,3)
cv2.imshow("Gaussian Blur,Gaussian Mean",thresh)

#Using Median Blur
mblur=cv2.medianBlur(gray,9)
cv2.imshow("Median Blur",mblur)
#Simple Mean Method
thresh=cv2.adaptiveThreshold(mblur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,4)
cv2.imshow('Median Blur,Simple Mean',thresh)
#Gaussian Mean
thresh=cv2.adaptiveThreshold(mblur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,15,3)
cv2.imshow("Median Blur,Gaussian Mean",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
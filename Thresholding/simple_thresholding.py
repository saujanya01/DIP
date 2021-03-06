import cv2
img=cv2.imread("/home/saujanya/OCR/practice/test_images/coins.jpg")
cv2.imshow("Original",img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale",gray)
blur=cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow("Blurred Image",blur)
(T,thresh)=cv2.threshold(blur,70,255,cv2.THRESH_BINARY)
cv2.imshow("Thresholded image",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
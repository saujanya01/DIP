import cv2
import end
img=cv2.imread('/home/saujanya/OCR/practice/test_images/lion.jpg')
cv2.imshow("original",img)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",hsv)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)
lab=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
cv2.imshow("LAB",lab)
end.close(0)
import cv2
import numpy as np
import end

img=cv2.imread('/home/saujanya/OCR/practice/test_images/lion.jpg')
cv2.imshow('Original',img)

#masking
(h,w,c)=img.shape
h1=h//2
w1=w//2
M1=np.zeros(img.shape[:2],dtype="uint8")
M2=np.zeros(img.shape[:2],dtype="uint8")
rect=cv2.rectangle(M1,(w1-100,h1-100),(w1+100,h1+100),255,-1)
circle=cv2.circle(M2,(w1,h1),200,255,-1)
cv2.imshow('Rectangle',rect)
cv2.imshow('Circle',circle)
end.close(0)
mask_rect=cv2.bitwise_and(img,img,mask=rect)
mask_circle=cv2.bitwise_and(img,img,mask=circle)
#crop=mask[h-50:h+50,w-50:w+50]
cv2.imshow('Masked rectangle',mask_rect)
cv2.imshow('Masked circle',mask_circle)
#cv2.imshow('Cropped',crop)
end.close(0)

#splitting and merging
#splitting
(B, G, R)=cv2.split(img)
cv2.imshow("Blue",B)
cv2.imshow("Green",G)
cv2.imshow("Red",R)
end.close(0)
#merging
merged=cv2.merge([B,G,R])
cv2.imshow("Merged image",merged)
end.close(0)
#Method 2
zeros=np.zeros(img.shape[:2],dtype="uint8")
B1=cv2.merge([B,zeros,zeros])
G1=cv2.merge([zeros,G,zeros])
R1=cv2.merge([zeros,zeros,R])
cv2.imshow("blue",B1)
end.close(0)
cv2.imshow("Green",G1)
end.close(0)
cv2.imshow("Red",R1)
end.close(0)
#making of some figures usnig numpy
import numpy as np
import cv2
img=np.zeros((300,300,3), dtype="uint8")
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.rectangle(img,(0,0),(300,300),[255,255,0],25)
cv2.imshow('red line',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img=np.zeros((300,300,3),dtype="uint8")
x=img.shape[1]//2
y=img.shape[0]//2
print(x)
print(y)
for r in range (0,150,25):
    cv2.circle(img,(x,y),r,[255,255,255],-1)
cv2.imshow('cricle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img=np.zeros((300,300,3),dtype="uint8")
for r in range(0,1000):
    radius=np.random.randint(5,high=150)
    center=np.random.randint(0,high=300,size=(2,))
    color=np.random.randint(0,high=256,size=(3,)).tolist()
    cv2.circle(img,tuple(center),radius,color)
cv2.imshow('random circles',img)
print(center)
color=np.random.randint(0,high=256,size=(3)).tolist()
print(color)
cv2.waitKey(0)
cv2.destroyAllWindows()
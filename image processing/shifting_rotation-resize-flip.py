#image processing
import numpy as np
import cv2
import imutils
import end

#Original image
img=cv2.imread('/home/saujanya/OCR/practice/test_images/lion.jpg')
cv2.imshow('Original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#shifting of images
M=np.float32([[1,0,25],[0,1,50]])
shifted=cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
cv2.imshow('Shifted down and right',shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
#shifting using imutils
shifted=imutils.translate(img,50,75)
cv2.imshow('shifting using imutils',shifted)
end.close(0)

#Rotation of images
(h , w)=img.shape[:2]
center=(w//2 , h//2)
M=cv2.getRotationMatrix2D((w,h),45,1.0)
print('Rotation matrix\n',M)
rotated=cv2.warpAffine(img,M,(w,h))
cv2.imshow('Rotated by 45 degree',rotated)
end.close(0)
#rotation using imutils
rotated=imutils.rotate(img,180)
cv2.imshow('Rotation using imutils',rotated)
end.close(0)

#resizing of a image
(h,w)=img.shape[:2]
width=150
r=150/w
dim=(width,int(h*r))
resized=cv2.resize(img,(400,200),interpolation=cv2.INTER_AREA)
cv2.imshow('resized image',resized)
end.close(0)
#Resizing using imutils
resized=imutils.resize(img,50,None,cv2.INTER_LINEAR)
cv2.imshow('Resized using imutils',resized)
end.close(0)

#flipping of images
flip_1=cv2.flip(img,1)#Horizontal
flip_2=cv2.flip(img,0)#Vertical
flip_3=cv2.flip(img,-1)#Horizonatal and Vertical
cv2.imshow('Horizontal',flip_1)
cv2.imshow('vertically',flip_2)
cv2.imshow('horizontally and vertically',flip_3)
cv2.imshow('original',img)
end.close(0)

#corpping images
cropped_1=img[0:350,150:700]#img[height,width]
cv2.imshow('cropped image',cropped_1)
end.close(0)

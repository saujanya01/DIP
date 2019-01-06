#image arithmatic
import cv2
import numpy as np
import end
'''
print("max of 255: {}".format(cv2.add(np.uint8([200]),np.uint8([100]))))
print("max of 255 using numpy: {}".format(np.uint8([100])+np.uint8([200])))
'''
img=cv2.imread('/home/saujanya/OCR/practice/test_images/lion.jpg')
cv2.imshow('Original',img)
end.close(0)

#Using cv2.add and cv2.subtract
M=np.ones(img.shape,dtype="uint8")*100
added=cv2.add(img,M)
cv2.imshow('added using cv2',added)
end.close(0)

subtract=cv2.subtract(img,M)
cv2.imshow('subtracted using cv2',subtract)
end.close(0)

#numpy addition and subtraction
M=np.ones(img.shape,dtype='uint8')*100
added=img+M
subtract=img-M
cv2.imshow('Added using numpy',added)
end.close(0)
cv2.imshow('Subtracted using numpy',subtract)
end.close(0)
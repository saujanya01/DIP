import cv2
img=cv2.imread('/home/saujanya/OCR/practice/test_images/lion.jpg')
x=cv2.imshow('image',img)
print(x)
z=img[0,0]
(b, g, r) = img[0, 0]
s=img[0:55,0:55]
cv2.imshow('s',s)
img[0:50,0:50]=(0,255,255)
cv2.imshow('image1',img)
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r,g, b))
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

def translate(image,x,y):
    m=np.float32([[1,0,x],[0,1,y]])
    shifted=cv2.warpAffine(image,m,(image.shape[1],image.shape[0]))
    return shifted
def rotate(image, angle, center=None, scale=1.0):
    (h,w)=image.shape[:2]
    if center is None:
        center=(w//2,h//2)
    m=cv2.getRotationMatrix2D(center,angle,scale)
    rotated=cv2.warpAffine(image,m,(w,h))
    return rotated
def resize(image,width=None,height=None,inter=cv2.INTER_AREA):
    dim=None
    (h,w)=image.shape[:2]
    if width is None and height is None:
        dim=image.shape[:2]
    if width is None:
        r=height/float(h)
        dim=(int(r*w),height)
    elif height is None:
        r=width/float(w)
        dim=(width,int(r*h))
    else:
        dim=(width,height)
    resized=cv2.resize(image,dim,interpolation=inter)
    return resized
import cv2
import numpy as np
import end

M1=np.zeros((300,300),dtype="uint8")
M2=np.zeros((300,300),dtype="uint8")
rectangle=cv2.rectangle(M1,(25,25),(275,275),255,-1)
circle=cv2.circle(M2,(150,150),150,255,-1)
cv2.imshow("Rectangle",rectangle)
cv2.imshow("Circle",circle)
end.close(0)

bitwiseAnd=cv2.bitwise_and(rectangle,circle)
bitwiseOr=cv2.bitwise_or(rectangle,circle)
bitwiseXor=cv2.bitwise_xor(rectangle,circle)
bitwiseNot1=cv2.bitwise_not(circle)
bitwiseNot2=cv2.bitwise_not(rectangle)
cv2.imshow("and",bitwiseAnd)
cv2.imshow("or",bitwiseOr)
cv2.imshow("xor",bitwiseXor)
cv2.imshow("not of circle",bitwiseNot1)
cv2.imshow("not of rectangle",bitwiseNot2)
end.close(0)
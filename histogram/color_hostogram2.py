from matplotlib import pyplot as plt
import cv2
img=cv2.imread('/home/saujanya/OCR/practice/test_images/lion.jpg')
cv2.imshow('Original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
chan=cv2.split(img)
fig=plt.figure()

ax=fig.add_subplot(131)
hist=cv2.calcHist([chan[0],chan[1]],[0,1],None,[32,32],[0,256,0,256])
p=ax.imshow(hist,interpolation="nearest")
ax.set_title("2D plot between Blue and Green")
plt.colorbar(p)

ax=fig.add_subplot(132)
hist=cv2.calcHist([chan[1],chan[2]],[0,1],None,[32,32],[0,256,0,256])
p=ax.imshow(hist,interpolation="nearest")
ax.set_title("2D plot between Green and Red")
plt.colorbar(p)

ax=fig.add_subplot(133)
hist=cv2.calcHist([chan[0],chan[2]],[0,1],None,[32,32],[0,256,0,256])
p=ax.imshow(hist,interpolation="nearest")
ax.set_title("2D plot between Blue and Red")
plt.colorbar(p)

print("2D Histogram with shape: {}, and values: {}".format(hist.shape,hist.flatten().shape[0]))
from matplotlib import pyplot as plt
import cv2
img=cv2.imread('/home/saujanya/OCR/practice/test_images/lion.jpg')
chans=cv2.split(img)

colors=("b","g","r")
plt.figure()
plt.title("Color Histogram")
plt.xlabel("bins")
plt.ylabel("number of pixels")
for (chan,color) in zip(chans,colors):
    hist=cv2.calcHist(chan,[0],None,[256],[0,256])
    plt.plot(hist,color=color)
    plt.xlim([0,256])
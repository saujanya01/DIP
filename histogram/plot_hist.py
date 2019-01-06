from matplotlib import pyplot as plt
import cv2

def gray_hist(image,title,mask=None):
    plt.figure()
    plt.xlabel("Bins")
    plt.ylabel("Nunber of pixels")
    plt.title(title)
    hist=cv2.calcHist(image,[0],mask,[256],[0,256])
    plt.plot(hist)
    plt.show()
    plt.xlim([0,256])
    
def color_hist(image,title,mask=None):
    chans=cv2.split(image)
    colors=("b","g","r")    
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("Number of Pixels")
    for (chan,color) in zip(chans,colors):
        hist=cv2.calcHist([chan],[0],mask,[256],[0,256])
        plt.plot(hist)
        plt.show()
        plt.xlim([0,256])
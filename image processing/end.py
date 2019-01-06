import cv2
def close(time_in_ms):
    cv2.waitKey(time_in_ms)
    cv2.destroyAllWindows()
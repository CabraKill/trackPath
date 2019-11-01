import cv2
import os

cap = cv2.VideoCapture(0)
while True:
    #location = "C:\\Users\\Rapha\\Desktop\\Nova pasta\\CNN test\\data"
    location = "C:\\Users\\Rapha\\Desktop\\Citeng\\datasets\\inTheGround"
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
   
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('r'):
        location += "\\right"
        cv2.imwrite(location + "\\right" + str(len(os.listdir(location))) + ".jpg",frame)
        print("right saved" + str(len(os.listdir(location))))
    elif k == ord('f'):
        location += "\\left"
        cv2.imwrite(location + "\\left" + str(len(os.listdir(location))) + ".jpg",frame)
        print("left saved" + str(len(os.listdir(location))))
    elif k == ord('e'):
        location += "\\middle"
        cv2.imwrite(location + "\\middle" + str(len(os.listdir(location))) + ".jpg",frame)
        print("middle saved" + str(len(os.listdir(location))))
cap.release()
cv2.destroyAllWindows()
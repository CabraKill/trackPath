import cv2
from moveCar import carController

car = carController()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
   
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == 56: #UpKey
        car.toMiddle()
    elif k == 53: #DownKey
        car.toBottom()
    elif k == 52: #LeftKey
        car.toLeft()
    elif k == 54: #RightKey
        car.toRight()
    elif k == 32: #Space
        car.toStop()
    elif not k == 255:
        print(k)
cap.release()
cv2.destroyAllWindows()
import time
import cv2
import os
import winsound
import threading as th

pack = 40
delay = 4
delayBetween = 0.25
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
enablePrint = 0
configPrint = 'z'
counter=0
cap = cv2.VideoCapture(0)


def myth():
    count()
    global thread
    global enablePrint
    global configPrint
    print("Começooooou!!!")
    print(str(enablePrint) + ":" + str(configPrint))

    time.sleep(4)
    print("acabou")
    enablePrint = 0
    configPrint = 'z'
    winsound.Beep(2200, int(duration/3))
    time.sleep(0.1)
    winsound.Beep(2200, int(duration/3))
    time.sleep(0.1)
    print(location+"saved")
    print(str(enablePrint) + ":" + str(configPrint))

def stopThread():
    global thread
    thread.join()


thread = th.Thread(target=myth, daemon=True)


def count():

    for x in range(delay):
        time.sleep(1)
        print(x)
        winsound.Beep(frequency, duration)
    winsound.Beep(frequency, int(duration/3))
    time.sleep(0.1)
    winsound.Beep(frequency, int(duration/3))
    time.sleep(0.1)


def takePhoto(frame, location, name):
    location += name
    cv2.imwrite(location + name +
                str(len(os.listdir(location))) + ".jpg", frame)
    print("taken")


while True:
    #location = "C:\\Users\\Rapha\\Desktop\\Nova pasta\\CNN test\\data"
    location = "C:\\Users\\Rapha\\Desktop\\Citeng\\datasets\\inTheGround"
    ret, frame = cap.read()
    cv2.imshow("Video", frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('r'):
        configPrint = 'r'
        enablePrint = 1
        #if(not thread.run()):
            #thread.start()
        count()

    elif k == ord('f'):
        configPrint = 'f'
        enablePrint = 1
        #if(not thread.run()):
            #thread.start()
        count()
    elif k == ord('e'):
        configPrint = 'e'
        enablePrint = 1
        #if(not thread.isAlive()):
            #thread.run()
        count()
    elif enablePrint == 1:
        if configPrint == 'r':
            takePhoto(frame, location,"\\right")
        elif configPrint == 'f':
            takePhoto(frame, location,"\\left")
        elif configPrint == 'e':
            takePhoto(frame, location,"\\middle")
        
        counter += 1
        if(counter >= pack):
            configPrint = 'z'
            enablePrint = 0
            counter = 0
    else:
        print(".",end="")
cap.release()
cv2.destroyAllWindows()

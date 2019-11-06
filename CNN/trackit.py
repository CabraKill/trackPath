from keras.models import load_model
from keras.preprocessing.image import img_to_array
import argparse
import cv2
import numpy as np
from moveCar import carController
import time

time.sleep(5)
model = load_model("model")
car = carController()
currentMove = 3 #makes it stop
cap = cv2.VideoCapture(0)
lista = {
    0: "middle",
    1: "right",
    2: "left"
}

while True:
    ret, frame = cap.read()

    image = cv2.resize(frame, (28, 28))
    image = img_to_array(image)
    image = np.array(image, dtype="float") / 255.0
    image = image.reshape(-1, 28, 28, 3)
    predictionResult = model.predict(image)
    prediction = np.argmax(predictionResult)
    cv2.putText(img=frame, fontScale=1.5, color=(255, 0, 0),
                text="predict: {}[{}][{}]%".format(prediction, lista[prediction],predictionResult[0][prediction]),
                thickness=3, fontFace=cv2.FONT_HERSHEY_SIMPLEX, org=(50, 50))
    cv2.imshow("Video", frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    if prediction != currentMove:
        currenTmove = prediction
        if prediction == 0:
            car.toMiddle()
        elif prediction == 1:
            car.toRight()
        elif prediction == 2:
            car.toLeft()
        elif prediction == 3:
            currentMove == prediction
            car.toStop()

car.toStop()
cap.release()
cv2.destroyAllWindows()
#a= input()

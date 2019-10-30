from keras.models import load_model
from keras.preprocessing.image import img_to_array
import argparse
import cv2
import numpy as np

model = load_model("model")
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
    prediction = np.argmax(model.predict(image))
    cv2.putText(img=frame, fontScale=1, color=(255, 0, 0),
                text="predict: {}[{}]".format(prediction, lista[prediction]),
                thickness=2, fontFace=cv2.FONT_HERSHEY_SIMPLEX, org=(50, 50))
    cv2.imshow("Video", frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


#a= input()

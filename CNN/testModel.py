from tkinter import Tk
from tkinter.filedialog import askopenfilename
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import argparse
import cv2
import numpy as np

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected


image = cv2.imread(filename)
image = cv2.resize(image, (28, 28))
image = img_to_array(image)
image = np.array(image, dtype="float") / 255.0
image = image.reshape(-1, 28, 28, 3)
model = load_model("model")
prediction = np.argmax(model.predict(image))
print(prediction)
#a= input()
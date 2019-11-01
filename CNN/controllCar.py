from tkinter import *
import requests
from moveCar import carController

car = carController()
url = 'http://192.168.0.69/run'

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg.pack()
        
        self.stop = Button(self.widget1,text="Stop")
        self.stop.bind("<Button-1>", lambda a: car.toStop())
        self.stop.pack(side=TOP)
        
        self.left = Button(self.widget1,text="Left")
        self.left.bind("<Button-1>", lambda a: car.toLeft())
        self.left.pack(side=LEFT)

        self.middle = Button(self.widget1,text="Middle")
        self.middle.bind("<Button-1>", lambda a: car.toMiddle())
        self.middle.pack(side=LEFT)

        self.right = Button(self.widget1,text="Right")
        self.right.bind("<Button-1>", lambda a: car.toRight())
        self.right.pack(side=LEFT)

        self.bottom = Button(self.widget1,text="Bottom")
        self.bottom.bind("<Button-1>", lambda a: car.toBottom())
        self.bottom.pack(side=TOP)

root = Tk()
Application(root)
root.mainloop()
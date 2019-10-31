from tkinter import *
import requests

url = 'http://192.168.0.69/run'

def toStop(self):
    result = requests.get(url,params={'w0':0,'w1':0,'w2':0,'w3':0})
    print(result.text)

def toLeft(self):
    result = requests.get(url,params={'w0':1,'w1':0,'w2':0,'w3':1})
    print(result.text)

def toMiddle(self):
    result = requests.get(url,params={'w0':1,'w1':0,'w2':1,'w3':0})
    print(result.text)

def toRight(self):
    result = requests.get(url,params={'w0':0,'w1':1,'w2':1,'w3':0})
    print(result.text)

def toBottom(self):
    result = requests.get(url,params={'w0':0,'w1':1,'w2':0,'w3':1})
    print(result.text)

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg.pack()
        
        self.stop = Button(self.widget1,text="Stop")
        self.stop.bind("<Button-1>", toStop)
        self.stop.pack(side=TOP)
        
        self.left = Button(self.widget1,text="Left")
        self.left.bind("<Button-1>", toLeft)
        self.left.pack(side=LEFT)

        self.middle = Button(self.widget1,text="Middle")
        self.middle.bind("<Button-1>", toMiddle)
        self.middle.pack(side=LEFT)

        self.right = Button(self.widget1,text="Right")
        self.right.bind("<Button-1>", toRight)
        self.right.pack(side=LEFT)

        self.bottom = Button(self.widget1,text="Bottom")
        self.bottom.bind("<Button-1>", toBottom)
        self.bottom.pack(side=TOP)

root = Tk()
Application(root)
root.mainloop()
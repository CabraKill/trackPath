import requests

class carController:
    url = 'http://192.168.0.69/run'


    def toStop(self):
        result = requests.get(self.url,params={'w0':1,'w1':1,'w2':1,'w3':1})
        print(result.text)

    def toLeft(self):
        result = requests.get(self.url,params={'w0':1,'w1':0,'w2':0,'w3':1})
        print(result.text)

    def toMiddle(self):
        result = requests.get(self.url,params={'w0':1,'w1':0,'w2':1,'w3':0})
        print(result.text)

    def toRight(self):
        result = requests.get(self.url,params={'w0':0,'w1':1,'w2':1,'w3':0})
        print(result.text)

    def toBottom(self):
        result = requests.get(self.url,params={'w0':0,'w1':1,'w2':0,'w3':1})
        print(result.text)
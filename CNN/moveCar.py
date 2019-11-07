import requests


class carController:
    url = 'http://192.168.0.69/run'

    def toStop(self):
        try:
            result = requests.get(
                self.url, params={'w0': 0, 'w1': 0, 'w2': 0, 'w3': 0})#self.url, params={'w0': 1, 'w1': 1, 'w2': 1, 'w3': 1})
            print(result.text)
        except Exception as e:
            print(e)
        


    def toLeft(self):

        try:
            result = requests.get(
                self.url, params = {'w0': 255, 'w1': 0, 'w2': 0, 'w3': 0})#self.url, params = {'w0': 1, 'w1': 0, 'w2': 0, 'w3': 0})
            print(result.text)
        except Exception as e:
            print(e)
        

    def toMiddle(self):

        try:
            result=requests.get(
                self.url, params = {'w0': 255, 'w1': 0, 'w2': 255, 'w3': 0})#self.url, params = {'w0': 1, 'w1': 0, 'w2': 1, 'w3': 0})
            print(result.text)
        except Exception as e:
            print(e)
        

    def toRight(self):

        try:
            result=requests.get(
                self.url, params = {'w0': 0, 'w1': 0, 'w2': 255, 'w3': 0})#self.url, params = {'w0': 0, 'w1': 0, 'w2': 1, 'w3': 0})
            print(result.text)
        except Exception as e:
            print(e)
        

    def toBottom(self):

        try:
            result=requests.get(
                self.url, params = {'w0': 0, 'w1': 255, 'w2': 0, 'w3': 255})#self.url, params = {'w0': 0, 'w1': 1, 'w2': 0, 'w3': 1})
            print(result.text)
        except Exception as e:
            print(e)
        

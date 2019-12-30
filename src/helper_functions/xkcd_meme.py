import requests

#generate valid random number for comic id 
comicId = 200

class Meme(object):
    def __init__(self,comicId):
        self.comicId = comicId
        self.url = " http://xkcd.com/{0}/info.0.json".format(self.comicId)
    
    def getImageUrl(self):   
        try:
            self.query = requests.get(self.url)
            self.jsonData = self.query.json()
            return self.jsonData["img"]

        except:
            print("unable to get data")

    
    def getMemeData(self):
        try:
            self.query = requests.get(self.url)
            self.jsonData = self.query.json()
            return self.jsonData
        except:
            print("unable to get data")

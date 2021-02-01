import json

class ImdbEncoder(json.JSONEncoder):
 
    def default(self, obj):
        return obj.__dict__

class Imdb ():
    def __init__(self, movies):
        self.movies = movies

    def serialized(self, fileName):
        
        miString = json.dumps(self, cls=ImdbEncoder, indent=4)
        

        with open(fileName, 'w') as file:
            json.dump(json.loads(miString), file, indent=4)

    def deserialized(self, fileName):
        with open(fileName) as file:
            myDic = json.load(file)

        self.movies = myDic["movies"]



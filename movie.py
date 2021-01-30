import professional as professional

class Movie ():

    def __init__(self, title, releaseYear, nationality, genre):
        self.title = title
        self.releaseYear = releaseYear
        self.nationality = nationality
        self.genre = genre
        self.actors = []
        self.director = None
        self.writer = None
        self.language = ""
        self.platform = ""
        self.isMCU = False
        self.mainCharacterName = ""
        self.producer = ""
        self.distributor = ""
    
    def mostrarMovie (self):
        print("Title:", self.title)
        print("Release year:", self.releaseYear)
        for actor in self.actors:
            actor.mostrarTodo()
        self.director.mostrarTodo()
        self.writer.mostrarTodo()
        print("Language:", self.language)
        print("Platform:", self.platform)
        print("Is MCU:", self.isMCU)
        print("Main Character Name:", self.mainCharacterName)
        print("Producer:", self.producer)
        print("Distributor:", self.distributor)



class Professional() :

    def __init__(self, name, age, genre, weight, height, hairColour, eyeColour, race, isRetired, nationality, oscarsNumber, profession):
        self.name = name
        self.age= age
        self.genre= genre
        self.weight=weight
        self.height=height
        self.hairColour=hairColour
        self.eyeColour=eyeColour
        self.race=race
        self.isRetired=isRetired
        self.nationality=nationality
        self.oscarsNumber=oscarsNumber
        self.profession=profession
    
    def mostrarTodo(self):
        print('Su nombre es:', self.name)
        print('Su edad es: ', self.edad)
        print('Su género es:', self.genre)
        print('Su color de pelo es: ', self. hairColour)
        print('Su color de ojos es: ', self.eyeColour)
        print('Su raza es: ', self.race)
        print ('Su estado es: ', self.isRetired)
        print('Su nacionalidad es: ', self.nationality)
        print('Su número de oscars es: ', self.oscarsNumber)
        print('Su profesión es: ', self.profession)

import professional as prof
import movie as mov
import testProfessional as tProf

peli3 = mov.Movie("El señor de los Anillos", 2001, "Neozelandesa", "Aventuras")
peli3.actors = [tProf.profesional1, tProf.profesional2]
peli3.director = tProf.profesional3
peli3.writer = tProf.profesional4
peli3.language = "Inglés"
peli3.platform = "Cines"
peli3.isMCU = False
peli3.mainCharacterName = "Frodo"
peli3.producer = "Universal"
peli3.distributor = "New Line Cinema"

peli4 = mov.Movie("Harry Potter", 2003, "Inglesa", "Fantasía")
peli4.actors = [tProf.profesional4, tProf.profesional3]
peli4.director = tProf.profesional1
peli4.writer = tProf.profesional2
peli4.language = "Inglés"
peli4.platform = "Cines"
peli4.isMCU = False
peli4.mainCharacterName = "Harry Potter"
peli4.producer = "Warner"
peli4.distributor = "Sony"

peli3.mostrarMovie()
peli4.mostrarMovie()
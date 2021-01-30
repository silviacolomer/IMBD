import professional as prof
import movie as mov
import testProfessional as tProf

peli1=mov.Movie('Star Wars', 2000, 'Estadounidense', 'Ciencia Ficción')
peli1.actor= [tProf.profesional1,tProf.profesional3]
peli1.director=tProf.profesional3
peli1.writer=tProf.profesional1
peli1.language= 'Inglés'
peli1.platform= ' Netflix'
peli1.isMCU = 'FALSE'
peli1.mainCharacterName= 'Luke Skywalker'
peli1.producer = 'Warner'
peli1.distributor = 'Warner'

peli2=mov.Movie('Batman', 1990, 'Española', 'Acción')
peli2.actor= [tProf.profesional4,tProf.profesional4]
peli2.director=tProf.profesional3
peli2.writer=tProf.profesional2
peli2.language= 'Inglés'
peli2.platform= ' HBO'
peli2.isMCU = 'TRUE'
peli2.mainCharacterName= 'Batman'
peli2.producer = 'Universal'
peli2.distributor = 'Universal'


peli1.mostrarMovie()

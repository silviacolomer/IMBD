import imdb as imdb
import professional as prof
import movie as mov
import testMovie as tMov


title=input('Dime el título')
releaseYear= input('Dime el año de estreno')
nationality=input('Dime la nacionalidad')
genre=input('Dime el género')

peli5=mov.Movie(title,releaseYear,nationality,genre)

imdb5=imdb.Imdb([])

imdb5.deserialized('bbdd.json')

imdb5.movies.append(peli5)

imdb5.serialized('bbdd.json')


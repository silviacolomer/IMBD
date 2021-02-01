import imdb as imdb
import professional as prof
import movie as mov
import testMovie as tMov




imdb1 = imdb.Imdb([tMov.peli1, tMov.peli2, tMov.peli3, tMov.peli4])



imdb1.serialized("bbdd.json")

imdb2 = imdb.Imdb([])

imdb2.deserialized("bbdd.json")

print(imdb2.movies[0]["title"])

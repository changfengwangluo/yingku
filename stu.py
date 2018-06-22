import imdb


ia=imdb.IMDb()
m=ia.get_movie('0371746')
r=ia.get_movie_reviews('0371746')


print(r)


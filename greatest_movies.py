from bs4 import BeautifulSoup
import requests
from operator import itemgetter

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tags = soup.findAll(name="h3", class_ = "listicleItem_listicle-item__title__BfenH")
movies = []

for article_tag in article_tags:
    try:
        movie_name = article_tag.getText()
        movies.append(movie_name)
    except AttributeError:
        print("Item not found.")

movies = movies[::-1]

file = open("movies.txt", mode="w")

for movie in movies:
    file.write(f"{movie}\n")
    #print(movie)
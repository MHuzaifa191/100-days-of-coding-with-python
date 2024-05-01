from bs4 import BeautifulSoup
import requests
from operator import itemgetter

# import lxml

# with open("website.html", "r", encoding="utf-8") as file:
#     content = file.read()

# soup = BeautifulSoup(content, "html.parser")
# print(soup.title.string)


response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tags = soup.findAll(name="tr", class_ = "athing")
list_of_articles = []

for article_tag in article_tags:
    try:
        # print(article_tag)
        # print("\n")
        id = article_tag.get("id")
        article_text = article_tag.getText()
        article_link = article_tag.find(name="span", class_ ="titleline").find(name="a").get("href")
        article_score = soup.find(name="span", class_="score", id=f"score_{id}").getText()

        # print(article_text)
        # print(article_link)
        # print(article_score)

        dictionary = {
            "title" : article_text.replace('\n', '', 1),
            "link" : article_link,
            "score" : int(article_score.split()[0])
        }

        list_of_articles.append(dictionary)

    except AttributeError:
        print("An item wasn't available.")


# print(list_of_articles)
sorted_list = sorted(list_of_articles, key=itemgetter('score'), reverse=True)

for i in sorted_list:
    print(f"\n(Title) {i['title']}")
    print(f"(Link) {i['link']}")
    print(f"(Score) {i['score']}\n")
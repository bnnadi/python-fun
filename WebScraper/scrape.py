from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep # be nice
import json

BASE_URL = "http://plasticscolor.com"

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")

def get_category_links(section_url):
    soup = make_soup(section_url)
    blog = soup.find("div", "blog")
    category_links = [BASE_URL + items.a["href"] for items in blog.findAll("div","item")]
    return category_links

def get_category_winner(category_url):
    soup = make_soup(category_url)
    title = [h2.text for h2 in soup.findAll("div", attrs={"class","page-header"})]
    content = [p.text for p in soup.findAll(itemprop="articleBody")]
    return {"title": title,
            "news_url": category_url,
            "content": content}

if __name__ == '__main__':
    food_n_drink = ("http://plasticscolor.com/about/news.html")

    categories = get_category_links(food_n_drink)

    data = [] # a list to store our dictionaries
    for category in categories:
        winner = get_category_winner(category)
        data.append(winner)
        sleep(1) # be nice

    with  open('news.json','w') as text_file:
        json.dump(data,text_file)

    #print data


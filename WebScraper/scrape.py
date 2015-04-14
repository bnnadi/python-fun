from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep # be nice
import json

BASE_URL = "http://plasticscolor.com"

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")

def get_article_links(section_url):
    soup = make_soup(section_url)
    blog = soup.find("div", "blog")
    article_links = [BASE_URL + items.a["href"] for items in blog.findAll("div","item")]
    return article_links

def get_articles(article_url):
    soup = make_soup(article_url)
    title = [h2.text for h2 in soup.findAll("div", attrs={"class","page-header"})]
    content = [p.text for p in soup.findAll(itemprop="articleBody")]
    return {"title": title,
            "news_url": article_url,
            "content": content}

if __name__ == '__main__':
    news_articles = ("http://plasticscolor.com/about/news.html")

    articles = get_article_links(news_articles)

    data = [] # a list to store our articles
    for article in articles:
        info = get_articles(article)
        data.append(info)
        sleep(1) # be nice

    with  open('news.json','w') as text_file:
        json.dump(data,text_file)

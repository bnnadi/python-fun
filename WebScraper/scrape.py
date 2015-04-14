from lxml import html
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://plasticscolor.com/about/news/press-releases/120-interactive-design-application-shortens-time-to-market.html'
reponse = requests.get(url)
html = reponse.content

soup = BeautifulSoup(html)
article = soup.find('div', attrs={'class': 'item-page'})
with  open('news.txt','w') as text_file:
	text_file.write(article.prettify())


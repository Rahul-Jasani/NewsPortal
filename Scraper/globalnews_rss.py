
import requests
from bs4 import BeautifulSoup







def globalnews_rss(database):

    try:
        r = requests.get('https://globalnews.ca/feed/')
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            description = a.find('description').text
            published = a.find('pubDate').text
            category = []
            for i in a.findAll('category'):
                category.append(i.text)
    

#####################################################################################################
            database.uploadArticle(title, link, published, category, description, 'Global News')
#####################################################################################################

        return 
    except Exception as e:
        print('Scraping failed:  ')
        print(e)

import requests
from bs4 import BeautifulSoup







def ctvnews_lifestyle(database):

    try:
        r = requests.get('https://www.ctvnews.ca/rss/lifestyle/ctv-news-lifestyle-1.3407722')
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            description = a.find('description').text
            published = a.find('pubDate').text
            category = ['Lifestyle']
            source = 'CTV News'

            database.uploadArticle(title, link, published, category, description, source)

        return 
    except Exception as e:
        print('Scraping failed: ')
        print(e)
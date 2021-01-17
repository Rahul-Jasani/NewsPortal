import requests
from bs4 import BeautifulSoup







def ctvnews_sports(database):

    try:
        r = requests.get('https://www.ctvnews.ca/rss/sports/ctv-news-sports-1.3407726')
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            description = a.find('description').text
            published = a.find('pubDate').text
            category = ['Sports']
            source = 'CTV News'

            database.uploadArticle(title, link, published, category, description, source)

        return 
    except Exception as e:
        print('Scraping failed: ')
        print(e)
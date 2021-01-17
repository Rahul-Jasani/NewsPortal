import requests
from bs4 import BeautifulSoup







def ctvnews_canada(database):

    try:
        r = requests.get('https://www.ctvnews.ca/rss/ctvnews-ca-canada-public-rss-1.822284')
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            description = a.find('description').text
            published = a.find('pubDate').text
            category = ['Canada']
            source = 'CTV News'

            database.uploadArticle(title, link, published, category, description, source)

        return 
    except Exception as e:
        print('Scraping failed: ')
        print(e)
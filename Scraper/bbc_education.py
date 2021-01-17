import requests
from bs4 import BeautifulSoup







def bbcnews_education(database):

    try:
        r = requests.get('http://feeds.bbci.co.uk/news/education/rss.xml')
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            description = a.find('description').text
            published = a.find('pubDate').text
            category = ['Education']
            source = 'BBC News'

            database.uploadArticle(title, link, published, category, description, source)

        return 
    except Exception as e:
        print('Scraping failed: ')
        print(e)
        
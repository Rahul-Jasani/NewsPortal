from constants import Constants

def preferences_from_request(request):
    preferences = [
        (True if request.cookies.get(Constants.CATEGORIES[i]) == 'True' else False)
        for i in range(Constants.num_categories())
    ]
    preferences = dict(zip(Constants.CATEGORIES, preferences))

    formatted_preferences = list()

    for key, value in preferences.items():
        formatted_preferences.append({'title': key, 'active': value})

    return formatted_preferences

def active_preferences(request):
    preferences = [
        (True if request.cookies.get(Constants.CATEGORIES[i]) == 'True' else False)
        for i in range(Constants.num_categories())
    ]
    preferences = dict(zip(Constants.CATEGORIES, preferences))
    return [key for key, value in preferences.items() if value]

def articles_from_db(connector, categories):
    articles_by_category = [
        connector.getByCategory(category) for category in categories
    ]
    posts = list()

    for article_category in articles_by_category:
        for article in article_category:
            post = {
                'title': article.title,
                'source': article.source,
                'content': article.description,
                'date_posted': article.pubdate,
                'link': article.link,
            }
            posts.append(post)

    return posts

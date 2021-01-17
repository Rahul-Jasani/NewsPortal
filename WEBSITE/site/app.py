from flask import Flask
from flask import make_response, redirect, render_template, request, url_for

from constants import Constants
from DBConnector import DBConnector
from forms import PreferencesForm
from utils import preferences_from_request, articles_from_db, active_preferences

app = Flask(__name__)
app.config['SECRET_KEY'] = 'boo_radley'


# Test posts for testing.
# posts = [
#     {
#         'author': 'Scout Finch',
#         'title': 'Life in Maycomb',
#         'content': 'Life in Maycomb is fun.',
#         'date_posted': 'April 20, 2018',
#         'link': 'https://www.google.com'
#     },
#     {
#         'author': 'Atticus Finch',
#         'title': 'The Courthouse',
#         'content': 'The courthouse is not good.',
#         'date_posted': 'April 21, 2018',
#         'link': 'https://www.google.com'
#     }
# ]

connector = DBConnector()


@app.route("/")
@app.route("/home")
def home():
    if request.cookies.get(Constants.CATEGORIES[0]) is None:
        # No cookies are saved for this person's news preferences.
        return redirect(url_for('preferences'))

    # Get a dictionary of users preferences.
    preferences = preferences_from_request(request)
    # Get a list of all the categories that the user wants to see.
    active_categories = active_preferences(request)
    return render_template('home.html',
                           posts=articles_from_db(connector, active_categories),
                           sidebar_preferences=preferences)

@app.route("/about")
def about():
    return render_template('about.html',
                           title='About',
                           sidebar_preferences=preferences_from_request(request))

@app.route("/preferences", methods=['GET', 'POST'])
def preferences():
    form = PreferencesForm()

    print(form.category1.data)
    print(form.category2.data)
    print(form.category3.data)
    print(form.category4.data)
    print(form.category5.data)
    print(form.category6.data)
    print(form.category7.data)
    print(form.category8.data)
    print(form.category9.data)
    print(form.category10.data)
    print(form.category11.data)

    if (
        form.category1.data or
        form.category2.data or
        form.category3.data or
        form.category4.data or
        form.category5.data or
        form.category6.data or
        form.category7.data or
        form.category8.data or
        form.category9.data or
        form.category10.data or
        form.category11.data
    ):
        response = make_response(redirect('/home'))
        response.set_cookie(Constants.CATEGORIES[0], str(form.category1.data))
        response.set_cookie(Constants.CATEGORIES[1], str(form.category2.data))
        response.set_cookie(Constants.CATEGORIES[2], str(form.category3.data))
        response.set_cookie(Constants.CATEGORIES[3], str(form.category4.data))
        response.set_cookie(Constants.CATEGORIES[4], str(form.category5.data))
        response.set_cookie(Constants.CATEGORIES[5], str(form.category6.data))
        response.set_cookie(Constants.CATEGORIES[6], str(form.category7.data))
        response.set_cookie(Constants.CATEGORIES[7], str(form.category8.data))
        response.set_cookie(Constants.CATEGORIES[8], str(form.category9.data))
        response.set_cookie(Constants.CATEGORIES[9], str(form.category10.data))
        response.set_cookie(Constants.CATEGORIES[10], str(form.category11.data))
        return response

    return render_template('preferences.html',
                           title='Preferences',
                           sidebar_preferences=preferences_from_request(request),
                           form=form)


if __name__ == '__main__':
    app.run(debug=True)

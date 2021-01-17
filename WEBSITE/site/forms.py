from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms import BooleanField

from constants import Constants

class PreferencesForm(FlaskForm):
    category1 = BooleanField(Constants.CATEGORIES[0])
    category2 = BooleanField(Constants.CATEGORIES[1])
    category3 = BooleanField(Constants.CATEGORIES[2])
    category4 = BooleanField(Constants.CATEGORIES[3])
    category5 = BooleanField(Constants.CATEGORIES[4])
    category6 = BooleanField(Constants.CATEGORIES[5])
    category7 = BooleanField(Constants.CATEGORIES[6])
    category8 = BooleanField(Constants.CATEGORIES[7])
    category9 = BooleanField(Constants.CATEGORIES[8])
    category10 = BooleanField(Constants.CATEGORIES[9])
    category11 = BooleanField(Constants.CATEGORIES[10])
    submit = SubmitField("Save Preferences")

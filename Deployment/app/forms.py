from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class DataForm(FlaskForm):
    budget = FloatField('Whats the budget of the movie?')
    popularity = FloatField('Whats the popularity of the movie?')
    cast_size = IntegerField("What's the cast size of the movie?", validators=[NumberRange(min=0,max=10000)])
    runtime = IntegerField("What's the runtime of the movie?", validators=[NumberRange(min=0,max=1000)])
    has_collection = IntegerField('Does the movie have a collection? 1=Yes  0=No', validators=[NumberRange(min=0, max=1)])
    crew_size = IntegerField("What's the crew size of the movie?", validators=[NumberRange(min=0,max=10000)])
    has_homepage = IntegerField('Does the movie have a homepage? 1=Yes  0=No', validators=[NumberRange(min=0, max=1)])
    us_production = IntegerField('Is the movie made in USA? 1=Yes  0=No', validators=[NumberRange(min=0, max=1)])
    is_en_original_language = IntegerField('Is english the Original language? 1=Yes 0=No', validators=[NumberRange(min=0, max=1)])

    submit = SubmitField('Submit')



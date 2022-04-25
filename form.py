from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name = StringField('name', [DataRequired()])
    price = FloatField('price', [DataRequired()])
    quantity = IntegerField('quantity', [DataRequired()])
    submit = SubmitField('Submit')
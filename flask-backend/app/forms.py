from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, BooleanField, DecimalField, SubmitField
from wtforms.validators import NumberRange, DataRequired
from .models import types

class PokemansForm(FlaskForm):
    number = IntegerField(validators=[DataRequired()])
    attack = IntegerField(validators=[DataRequired()])
    defense = IntegerField(validators=[DataRequired()])
    imageUrl = StringField(validators=[DataRequired()])
    name = StringField(validators=[DataRequired()])
    type = StringField(validators=[DataRequired()])
    moves = StringField(validators=[DataRequired()])
    encounterRate = DecimalField(places=2,validators=[NumberRange(min=0.00,max=9.99),DataRequired()] )
    catchRate = DecimalField(places=2,validators=[NumberRange(min=0.00,max=9.99),DataRequired()] )
    captured = BooleanField(validators=[DataRequired()])
    submit = SubmitField()

class ItemsForm(FlaskForm):
    happieness = IntegerField(validators=[DataRequired()])
    imageUrl = StringField(validators=[DataRequired()])
    name = StringField(validators=[DataRequired()])
    price = IntegerField(validators=[DataRequired()])
    submit = SubmitField()

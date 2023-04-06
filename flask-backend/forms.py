from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField

types = [
    "fire",
    "electric",
    "normal",
    "ghost",
    "psychic",
    "water",
    "bug",
    "dragon",
    "grass",
    "fighting",
    "ice",
    "flying",
    "poison",
    "ground",
    "rock",
    "steel",]

class PokemansForm(FlaskForm):
    number = IntegerField()
    attack = IntegerField()
    defense = IntegerField()
    imageUrl = StringField()
    name = StringField()
    type = SelectField(choices=types)
    moves = StringField()
    encounterRate = 
    catchRate = 
    captured = 
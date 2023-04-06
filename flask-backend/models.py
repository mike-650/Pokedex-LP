from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

db = SQLAlchemy()

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


class Pokemon(db.Models):
    __tablename__ = 'Pokemons'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    items = db.relationship('Item', backref='create_pokemon', lazy=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255),unique=True ,nullable=False)
    type = db.Column(db.ENUM(types), nullable=False)
    moves = db.Column(db.String(255), nullable=False)
    encounterRate = db.Column(db.Numeric(3,2),default=1.00 , nullable=False)
    catchRate = db.Column(db.Numeric(3,2), default=1.00 , nullable=False)
    captured = db.Column(db.Boolean, default=False ,nullable=False)
    createdAt = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    updatedAt = db.Column(db.Date, default=datetime.utcnow, nullable=False)


class Item(db.Models):
    __tablename__ = 'Items'
    
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    happieness = db.Column(db.Integer, nullable=False) 
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    pokemonId = db.Column(db.Integer, db.ForeignKey('pokemans.id'), nullable=False,)
    createdAt = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    updatedAt = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    
class PokemanType(db.models):
    

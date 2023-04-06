import json
from flask import Blueprint
from ..models import Pokemon

pokemonBp = Blueprint('pokemon', __name__)

@pokemonBp.route('/api/pokemon')
def getPokemons():
  all_pokemons = Pokemon.query.all()
  print(all_pokemons)
  class PokemonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Pokemon):
            return {'name': obj.name, 'type': obj.type, 'id': obj.id, 'imageUrl': '', 'number': obj.number, 'captured': obj.captured}
        return json.JSONEncoder.default(self, obj)

  return json.dumps(all_pokemons, cls=PokemonEncoder)

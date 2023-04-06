from app.models import db, Pokemon
from sqlalchemy.sql import text


def seed_pokemons():
    pokemon1 = Pokemon(
        number=1,
        imageUrl='/images/pokemon_snaps/1.svg',
        name='Bulbasaur',
        attack=49,
        defense=49,
        type='grass',
        moves='tackle,vine whip',
        captured=True
    )

    pokemon2 = Pokemon(
        number=2,
        imageUrl='/images/pokemon_snaps/2.svg',
        name='Ivysaur',
        attack=62,
        defense=63,
        type='grass',
        moves='tackle,vine whip',
        captured=True
    )

    pokemon3 = Pokemon(
        number=3,
        imageUrl='/images/pokemon_snaps/3.svg',
        name='Venusaur',
        attack=82,
        defense=83,
        type='grass',
        moves='tackle,vine whip',
        captured=True
    )

    pokemon4 = Pokemon(
        number=4,
        imageUrl='/images/pokemon_snaps/4.svg',
        name='Charmander',
        attack=52,
        defense=43,
        type='fire',
        moves='tackle,vine whip',
        captured=True
    )
    pokemon5 = Pokemon(
        number=5,
        imageUrl='/images/pokemon_snaps/5.svg',
        name='Charmeleon',
        attack=64,
        defense=58,
        type='fire',
        moves='tackle,vine whip',
        captured=True
    )
    pokemon6 = Pokemon(
        number=6,
        imageUrl='/images/pokemon_snaps/6.svg',
        name='Charizard',
        attack=84,
        defense=78,
        type='fire',
        moves='tackle,vine whip',
        captured=True
    )
    pokemon7 = Pokemon(
        number=7,
        imageUrl='/images/pokemon_snaps/7.svg',
        name='Squirtle',
        attack=48,
        defense=65,
        type='water',
        moves='tackle,vine whip',
        captured=True
    )
    pokemon8 = Pokemon(
        number=8,
        imageUrl='/images/pokemon_snaps/8.svg',
        name='Wartortle',
        attack=63,
        defense=80,
        type='water',
        moves='tackle,vine whip',
        captured=True
    )
    pokemon9 = Pokemon(
        number=9,
        imageUrl='/images/pokemon_snaps/9.svg',
        name='Blastoise',
        attack=83,
        defense=100,
        type='water',
        moves='tackle,vine whip',
        captured=True
    )
    pokemon10 = Pokemon(
        number=10,
        imageUrl='/images/pokemon_snaps/10.svg',
        name='Caterpie',
        attack=30,
        defense=35,
        type='bug',
        moves='tackle,vine whip',
        captured=True
    )
    pokemon11 = Pokemon(
        number=11,
        imageUrl='/images/pokemon_snaps/12.svg',
        name='Butterfree',
        attack=45,
        defense=50,
        type='bug',
        moves='tackle,vine whip',
        captured=True
    )
    pokemon12 = Pokemon(
        number=12,
        imageUrl='/images/pokemon_snaps/1.svg',
        name='Lucario',
        attack=49,
        defense=49,
        type='grass',
        moves='tackle,vine whip',
        captured=True
    )
    pokemon13 = Pokemon(
        number=13,
        imageUrl='/images/pokemon_snaps/1.svg',
        name='Goobo',
        attack=49,
        defense=49,
        type='grass',
        moves='tackle,vine whip',
        captured=True
    )
    pokemon14 = Pokemon(
        number=14,
        imageUrl='/images/pokemon_snaps/1.svg',
        name='Coolo',
        attack=49,
        defense=49,
        type='grass',
        moves='tackle,vine whip',
        captured=True
    )
    pokemon15 = Pokemon(
        number=15,
        imageUrl='/images/pokemon_snaps/1.svg',
        name='Boolo',
        attack=49,
        defense=49,
        type='grass',
        moves='tackle,vine whip',
        captured=True
    )

    all_pokemons = [pokemon1, pokemon2, pokemon3, pokemon4,
                    pokemon5, pokemon6, pokemon7,
                    pokemon8, pokemon9, pokemon10,
                    pokemon11, pokemon12, pokemon13,
                    pokemon14, pokemon15]
    add_pokemons = [db.session.add(pokemon) for pokemon in all_pokemons]
    db.session.commit()
    return all_pokemons


def undo_pokemons():
    db.session.execute(text('DELETE FROM Pokemons'))
    db.session.commit()

from flask.cli import AppGroup
from .pokemons import seed_pokemons, undo_pokemons
from .items import seed_items, undo_items


seed_commands = AppGroup('seed')


@seed_commands.command('all')
def seed():
    seed_pokemons()
    seed_items()
    print('Seeds Complete! :)')

@seed_commands.command('undo')
def undo():
    undo_items()
    undo_pokemons()
    print('Undo Complete! :)')

from app.models import db, Item
from sqlalchemy.sql import text


def seed_items():
    item1 = Item(
        happieness=70,
        imageUrl='https://i.kym-cdn.com/photos/images/original/002/527/308/03b',
        name='Berry',
        price=10,
        pokemonId=1
    )

    item2 = Item(
        happieness=70,
        imageUrl='https://i.kym-cdn.com/photos/images/original/002/527/308/03b',
        name='Berry',
        price=10,
        pokemonId=1
    )

    item3 = Item(
        happieness=70,
        imageUrl='https://i.kym-cdn.com/photos/images/original/002/527/308/03b',
        name='Berry',
        price=10,
        pokemonId=1
    )

    item4 = Item(
        happieness=70,
        imageUrl='https://i.kym-cdn.com/photos/images/original/002/527/308/03b',
        name='Berry',
        price=10,
        pokemonId=1
    )

    item5 = Item(
        happieness=70,
        imageUrl='https://i.kym-cdn.com/photos/images/original/002/527/308/03b',
        name='Berry',
        price=10,
        pokemonId=1
    )

    item6 = Item(
        happieness=70,
        imageUrl='https://i.kym-cdn.com/photos/images/original/002/527/308/03b',
        name='Berry',
        price=10,
        pokemonId=1
    )

    item7 = Item(
        happieness=70,
        imageUrl='https://i.kym-cdn.com/photos/images/original/002/527/308/03b',
        name='Berry',
        price=10,
        pokemonId=1
    )

    item8 = Item(
        happieness=70,
        imageUrl='https://i.kym-cdn.com/photos/images/original/002/527/308/03b',
        name='Berry',
        price=10,
        pokemonId=1
    )

    item9 = Item(
        happieness=70,
        imageUrl='https://i.kym-cdn.com/photos/images/original/002/527/308/03b',
        name='Berry',
        price=10,
        pokemonId=1
    )

    item10 = Item(
        happieness=70,
        imageUrl='https://i.kym-cdn.com/photos/images/original/002/527/308/03b',
        name='Berry',
        price=10,
        pokemonId=1
    )

    all_items = [item1, item2, item3, item4,
                item5, item6, item7, item8, item9, item10]
    add_items = [db.session.add(item) for item in all_items]
    db.session.commit()
    return all_items


def undo_items():
    db.session.execute(text('DELETE FROM Items'))
    db.session.commit()

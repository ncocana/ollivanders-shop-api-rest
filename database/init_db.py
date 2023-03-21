import sqlite3

connection = sqlite3.connect('database.db')


with open('database/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

rows = [('+5 Dexterity Vest', 10, 20, 'ConjuredItem'),
        ('Aged Brie', 2, 0, 'AgedBrie'),
        ('Elixir of the Mongoose', 5, 7, 'NormalItem'),
        ('Sulfuras; Hand of Ragnaros', 0, 80, 'Sulfuras'),
        ('Sulfuras; Hand of Ragnaros', -1, 80, 'Sulfuras'),
        ('Backstage passes to a TAFKAL80ETC concert', 15, 20, 'Backstage'),
        ('Backstage passes to a TAFKAL80ETC concert', 10, 49, 'Backstage'),
        ('Backstage passes to a TAFKAL80ETC concert', 5, 49, 'Backstage'),
        ('Conjured Mana Cake', 3, 6, 'ConjuredItem')]

cur.executemany("INSERT INTO inventory (name, sell_in, quality, class_object) VALUES (?, ?, ?, ?)",
            rows
            )

connection.commit()

connection.close()
from flask import Flask, render_template, request
from logic.GildedRose import *

# Turns this file into a Flask application.
app = Flask(__name__)

INVENTORY = {
    1: {'name':'+5 Dexterity Vest', 'sell_in': 10, 'quality': 20, 'class': 'ConjuredItem'},
    2: {'name':'Aged Brie', 'sell_in': 2, 'quality': 0, 'class': 'AgedBrie'},
    3: {'name':'Elixir of the Mongoose', 'sell_in': 5, 'quality': 7, 'class': 'NormalItem'},
    4: {'name':'Sulfuras; Hand of Ragnaros', 'sell_in': 0, 'quality': 80, 'class': 'Sulfuras'},
    5: {'name':'Sulfuras; Hand of Ragnaros', 'sell_in': -1, 'quality': 80, 'class': 'Sulfuras'},
    6: {'name':'Backstage passes to a TAFKAL80ETC concert', 'sell_in': 15, 'quality': 20, 'class': 'Backstage'},
    7: {'name':'Backstage passes to a TAFKAL80ETC concert', 'sell_in': 10, 'quality': 49, 'class': 'Backstage'},
    8: {'name':'Backstage passes to a TAFKAL80ETC concert', 'sell_in': 5, 'quality': 49, 'class': 'Backstage'},
    9: {'name':'Conjured Mana Cake', 'sell_in': 3, 'quality': 6, 'class': 'ConjuredItem'}
}

dictClasses = {"Sulfuras; Hand of Ragnaros": "Sulfuras",
                         "Aged Brie": "AgedBrie",
                         "Backstage passes to a TAFKAL80ETC concert": "Backstage",
                         "Conjured Mana Cake": "ConjuredItem",
                         "+5 Dexterity Vest": "ConjuredItem",
                         "Normal Item": "NormalItem"}

@app.route('/')
def index():
    return render_template("home/index.html")

@app.route('/inventory', methods=["GET", "POST"])
def inventory():
    if request.method == "GET":
        return render_template("home/inventory.html", inventory=INVENTORY)
    if request.method == "POST":
        INVENTORY_LIST = []
        INVENTORY_UPDATE = []
        # for item in INVENTORY:
        #     INVENTORY_LIST.append([INVENTORY[item]['name'], int(INVENTORY[item]['sell_in']), int(INVENTORY[item]['quality'])])
        #     name = INVENTORY[item]['name']
        #     sell_in = INVENTORY[item]['sell_in']
        #     quality = INVENTORY[item]['quality']
        for item in INVENTORY:
            name = INVENTORY[item]['name']
            sell_in = INVENTORY[item]['sell_in']
            quality = INVENTORY[item]['quality']
            try:
                classItem = dictClasses[name]
            # If the item's name is not in 'dictClasses',
            # it means is a Normal Item.
            except KeyError:
                classItem = dictClasses["Normal Item"]
            itemObject = globals()[classItem](name, sell_in, quality)
            # itemObject = ConjuredItem('+5 Dexterity Vest', 10, 20)
            itemObject.update_quality()
            i = str(itemObject).find(',', str(itemObject).find(',', str(itemObject).find("'") + 1) + 1)
            values = [v.strip() for v in str(itemObject).split(',')]
            # s = str(itemObject)
            # itemTuple = eval(s)
            INVENTORY_UPDATE.append(values)

        # for key in INVENTORY:
            # # Get the values of name, sell_in and quality from the dictionary
            # name = INVENTORY[key]['name']
            # sell_in = INVENTORY[key]['sell_in']
            # quality = INVENTORY[key]['quality']
            # # Create an instance of Item with these values as parameters
            # try:
            #     nameItem = name
            #     classItem = dictClasses[nameItem]
            # # If the item's name is not in 'dictClasses',
            # # it means is a Normal Item.
            # except KeyError:
            #     classItem = dictClasses["Normal Item"]
            # item = GildedRose(eval(classItem + str(tuple([name, sell_in, quality]))))
            # # Update the values of sell_in and quality using some logic (this depends on your class definition)
            # item.update_quality()
            # INVENTORY_UPDATE.append([name, sell_in, quality])
        return render_template("home/inventory-update.html", inventory_update=INVENTORY_UPDATE)

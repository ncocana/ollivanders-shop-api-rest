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

@app.route('/')
def index():
    return render_template("home/index.html")

@app.route('/inventory', methods=["GET", "POST"])
def inventory():
    if request.method == "POST":

        for item in INVENTORY:
            
            #Saves the values of the dictionary.
            name = INVENTORY[item]['name']
            sell_in = INVENTORY[item]['sell_in']
            quality = INVENTORY[item]['quality']
            classItem = INVENTORY[item]['class']

            itemObject = globals()[classItem](name, sell_in, quality)
            itemObject.update_quality()

            values = [v.strip() for v in str(itemObject).split(',')]

            INVENTORY[item]['sell_in'] = int(values[1])
            INVENTORY[item]['quality'] = int(values[2])
            
            return render_template("home/inventory-update.html")

    return render_template("home/inventory.html", inventory=INVENTORY)

from flask import Flask, render_template, request

# Turns this file into a Flask application.
app = Flask(__name__)

INVENTORY = {
    1: {'name':'+5 Dexterity Vest', 'sell_in': 10, 'quality': 20},
    2: {'name':'Aged Brie', 'sell_in': 2, 'quality': 0},
    3: {'name':'Elixir of the Mongoose', 'sell_in': 5, 'quality': 7},
    4: {'name':'Sulfuras, Hand of Ragnaros', 'sell_in': 0, 'quality': 80},
    5: {'name':'Sulfuras, Hand of Ragnaros', 'sell_in': -1, 'quality': 80},
    6: {'name':'Backstage passes to a TAFKAL80ETC concert', 'sell_in': 15, 'quality': 20},
    7: {'name':'Backstage passes to a TAFKAL80ETC concert', 'sell_in': 10, 'quality': 49},
    8: {'name':'Backstage passes to a TAFKAL80ETC concert', 'sell_in': 5, 'quality': 49},
    9: {'name':'Conjured Mana Cake', 'sell_in': 3, 'quality': 6}
}

@app.route('/')
def index():
    return render_template("home/index.html")

@app.route('/inventory')
def inventory():
    return render_template("home/inventory.html", inventory=INVENTORY)
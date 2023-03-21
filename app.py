from flask import Flask, render_template, request
from logic.GildedRose import *
from database import db

# Turns this file into a Flask application.
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home/index.html")

@app.route('/inventory', methods=["GET", "POST"])
def inventory():

    INVENTORY = db.get_all_inventory()

    if request.method == "POST":

        for item in INVENTORY:
            
            #Saves the values of the database.
            id_item = item['id']
            name = item['name']
            sell_in = item['sell_in']
            quality = item['quality']
            class_item = item['class_object']

            # Creates an object of its respective class and proceeds to update it.
            # itemObject = globals()[classItem](name, sell_in, quality)
            item_object = eval(class_item + str((name, sell_in, quality)))
            item_object.update_quality()

            # Converts "itemObject" to string and splits it by its commas.
            values = [v.strip() for v in str(item_object).split(',')]

            # Updates the values "sell_in" and "quality" in the database.
            db.update_item(int(values[1]), int(values[2]), id_item)
            
            # Shows a page with a message indicating the succesful of the update.
            return render_template("home/inventory-update.html")

    # Shows the inventory's current state if the request's method is "GET".
    return render_template("home/inventory.html", inventory=INVENTORY)

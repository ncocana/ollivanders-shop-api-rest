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
            item_object = eval(class_item + str((name, sell_in, quality)))
            item_object.update_quality()

            # Converts "item_object" to string and splits it by its commas.
            values = [v.strip() for v in str(item_object).split(',')]

            # Updates the values "sell_in" and "quality" in the database.
            db.update_item(int(values[1]), int(values[2]), id_item)
            
        # Shows a page with a message indicating the succesful of the update.
        return render_template("home/inventory-update.html")

    # Shows the inventory's current state if the request's method is "GET".
    return render_template("home/inventory.html", inventory=INVENTORY)

@app.route('/inventory/create', methods=["GET", "POST"])
def create():

    classes_list = ['NormalItem', 'ConjuredItem', 'AgedBrie', 'Sulfuras', 'Backstage']

    if request.method == "POST":

        name = request.form.get("name")
        sell_in = request.form.get("sell_in")
        quality = request.form.get("quality")
        class_object = request.form.get("class_object")

        if not name or not sell_in or not quality or class_object not in classes_list:
            return render_template("home/invalid-form.html")
        
        db.create_item(name, sell_in, quality, class_object)

        # Shows a page with a message indicating the succesful of the update.
        return render_template("home/inventory-update.html")

    return render_template("home/create-item.html", classes=set(classes_list))

@app.route('/inventory/delete', methods=["GET", "DELETE"])
def delete():

    if request.method == "DELETE":

        INVENTORY = db.get_all_inventory()
        id_item_list = [item['id'] for item in INVENTORY]

        data_request = request.form['id']

        if data_request != "":
            id_item = int(data_request)

            db.delete_item(id_item)

        return id_item_list

    if request.method == "GET":
        return render_template("home/delete-item.html")

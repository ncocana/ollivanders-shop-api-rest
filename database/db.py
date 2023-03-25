import sqlite3
from flask import abort


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_all_inventory():
    conn = get_db_connection()
    INVENTORY = conn.execute("SELECT * FROM inventory").fetchall()
    conn.close()
    return INVENTORY


# Method not used.
# def get_item(id):
#     conn = get_db_connection()
#     item = conn.execute('SELECT * FROM inventory WHERE id = ?',
#                         (id,)).fetchone()
#     conn.close()

#     if item is None:
#         abort(404)

#     return item


def update_item(sell_in, quality, id):
    conn = get_db_connection()
    conn.execute(
        "UPDATE inventory SET sell_in = ?, quality = ? WHERE id = ?",
        (sell_in, quality, id),
    )
    conn.commit()
    conn.close()


def create_item(name, sell_in, quality, class_object):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO inventory (name, sell_in, quality, class_object) VALUES (?, ?, ?, ?)",
        (name, sell_in, quality, class_object),
    )
    conn.commit()
    conn.close()


def delete_item(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM inventory WHERE id = ?", (id,))
    conn.commit()
    conn.close()

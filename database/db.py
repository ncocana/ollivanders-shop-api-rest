import sqlite3


def get_db_connection():
    try:
        conn = sqlite3.connect("database.db")
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:  # pragma: no cover
        print(f"Error connecting to database: {e}")
        return None


def get_all_inventory():
    conn = get_db_connection()
    INVENTORY = conn.execute("SELECT * FROM inventory").fetchall()
    conn.close()
    return INVENTORY


def get_item_by_id(id):
    conn = get_db_connection()
    item = conn.execute("SELECT * FROM inventory WHERE id = ?", (id,)).fetchone()
    conn.close()
    return item


def get_item_by_name(name):
    conn = get_db_connection()
    item = conn.execute("SELECT * FROM inventory WHERE name = ?", (name,)).fetchone()
    conn.close()
    return item


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

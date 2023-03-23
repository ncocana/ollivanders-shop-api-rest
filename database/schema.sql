DROP TABLE IF EXISTS inventory;

CREATE TABLE inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sell_in INT NOT NULL,
    quality INT NOT NULL,
    class_object TEXT NOT NULL
);

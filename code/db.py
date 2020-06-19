import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                 username text,
                  email text,
                  password text
                  )""")

        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, username, email, password):
        self.cur.execute("INSERT INTO users VALUES (NULL, ?, ?, ?)",
                         (username, email, password))
        self.conn.commit()

    def remove_by_name(self, username):
        self.cur.execute("DELETE FROM users WHERE username=?", (username,))
        self.conn.commit()

    def update(self, username, email, password):
        self.cur.execute("UPDATE users SET username = ?, email = ?, password = ? WHERE username = ?",
                         (username, email, password))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


db = Database('code_assistant.db')
db.insert("4GB DDR4 Ram", "John Doe", "Microcenter", "160")
db.insert("Asus Mobo", "Mike Henry", "Microcenter", "360")
db.insert("500w PSU", "Karen Johnson", "Newegg", "80")
db.insert("2GB DDR4 Ram", "Karen Johnson", "Newegg", "70")
db.insert("24 inch Samsung Monitor", "Sam Smith", "Best Buy", "180")
db.insert("NVIDIA RTX 2080", "Albert Kingston", "Newegg", "679")
db.insert("600w Corsair PSU", "Karen Johnson", "Newegg", "130")
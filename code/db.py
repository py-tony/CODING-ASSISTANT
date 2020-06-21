import sqlite3
import datetime


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username text unique,
                email text unique,
                password text,
                date_and_time text
                )""")

        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM users")
        rows = self.cur.fetchall()
        return rows

    def insert(self, username, email, password):
        try:
            self.cur.execute("INSERT INTO users VALUES (NULL, ?, ?, ?, ?)",
                         (username, email, password, datetime.datetime.now()))
            self.conn.commit()
            return
        except Exception as e:
            return e, "already exist please use valid credentials"

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

# insert_result = db.insert("test", "test@pyton", "12345")

print(db.fetch())
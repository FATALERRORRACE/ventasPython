import sqlite3
import config

class Db:
    def __init__(self):
        self.conn = sqlite3.connect(config.DB_FILE)

    def close(self):
        if self.conn:
            self.conn.close()

    def query(self, query, params=None):
        if self.conn is None:
            raise Exception("Database connection is not established.")

        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        if query.strip().lower().startswith("select"):
            result = cursor.fetchall()
            return result
        elif query.strip().lower().startswith(("insert", "update", "delete")):
            self.conn.commit()
            return cursor

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
        self.conn.commit()
        return cursor

import sqlite3
import os
import hashlib

class DataBase:
    def __init__(self):
        self.PARENT_PATH = 'assets/images/.cache/.database'
        self.database = "universal_scrapper.db"
        conn = sqlite3.connect(os.path.join(self.PARENT_PATH, self.database))
        conn.execute('CREATE TABLE IF NOT EXISTS url_key_parser (url STRING, unique_key STRING)')
        conn.close()

    def connector(self):
        conn = sqlite3.connect(os.path.join(self.PARENT_PATH, self.database))
        return conn
    
    def parse_key(self, url):
        unique_key = hashlib.sha256(str(url).encode('utf-8')).hexdigest()
        conn = self.connector()
        cursor = conn.cursor()
        cursor.execute("SELECT unique_key FROM url_key_parser WHERE unique_key = '{}'".format(unique_key))
        unique_key_db = cursor.fetchone()
        if not unique_key_db:
            print("[INFO] Unique Key Not Exists.")
            cursor.execute("INSERT INTO url_key_parser (url, unique_key) VALUES ('{0}', '{1}')".format(url, unique_key))
            conn.commit()
        else:
            unique_key = unique_key_db[0]
            print("[INFO] Unique Key Exists.")
        cursor.close()
        conn.close()
        return unique_key

    def get_urls(self):
        conn = self.connector()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM url_key_parser")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        if data:
            return dict(data)
        return 0

    def is_url_in_db(self, url):
        conn = self.connector()
        cursor = conn.cursor()
        cursor.execute("SELECT unique_key FROM url_key_parser WHERE url = '{}'".format(url))
        unique_key_db = cursor.fetchone()
        cursor.close()
        conn.close()
        if unique_key_db:
            print("[INFO] URL EXISTS")
            return unique_key_db[0]
        else:
            print("[INFO] URL NOT EXISTS")
            return False


# DataBase().get_urls()
import mysql.connector


class MYSQLClient:
    def __init__(self):
        self.conn = self.get_connection()

    def get_connection(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="test",
            passwd="test",
            database='demo'
        )
        return mydb

    def table_exist(self, table_name):
        my_cursor = self.conn.cursor()
        my_cursor.execute("SHOW TABLES")
        for t in my_cursor:
            if t[0] == table_name:
                return True
        return False

    def create_table(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)

    def insert_all(self, sql, values):
        print(sql)
        insert_cursor = self.conn.cursor()
        insert_cursor.executemany(sql, values)
        self.conn.commit()
        print(insert_cursor.rowcount, "was inserted.")

    def query_all(self, sql):
        query_cursor = self.conn.cursor()
        query_cursor.execute(sql)
        return query_cursor.fetchall()

    def update_all(self, sql, val):
        update_cursor = self.conn.cursor()
        update_cursor.execute(sql, val)
        self.conn.commit()
        print(update_cursor.rowcount, "record(s) affected")

from PySide6.QtSql import QSqlDatabase, QSqlQuery


class Database:
    def __init__(self, db_name: str):
        self.db_name = db_name

    def __enter__(self):
        # Initialize the database connection
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./resource/database.db')

        # Open the database connection
        if not self.db.open():
            print("Unable to connect to the database")
            raise RuntimeError("Database connection failed")
        return self

    def select(self, name):
        data_list = []
        query = QSqlQuery()
        query.exec(f"SELECT * FROM {self.db_name} WHERE NAME = '{name}'")
        while query.next():
            for i in range(0, 7):
                data_list.append(query.value(i))
        return data_list

    def select_col(self, column: int) -> list[str]:
        data_list = []
        query = QSqlQuery()
        query.exec(f"SELECT * FROM {self.db_name} ORDER BY NAME DESC")
        while query.next():
            data_list.append(query.value(column))
        return data_list

    def insert(self, name, detail_1, detail_2, detail_3, detail_4, detail_5):
        query = QSqlQuery()
        query.exec(
            f"""INSERT INTO {self.db_name} (NAME, DETAIL_1, DETAIL_2, DETAIL_3, DETAIL_4, DETAIL_5) 
            VALUES ('{name}', '{detail_1}', '{detail_2}', '{detail_3}', '{detail_4}', '{detail_5}')""")

    def delete(self, name):
        query = QSqlQuery()
        query.exec(
            f"""DELETE FROM {self.db_name} WHERE NAME = '{name}'""")

    def __exit__(self, exc_type, exc_value, traceback):
        # Close the database connection when exiting the context
        self.db.close()


if __name__ == "__main__":
    with Database('addressee') as db_context:
        print(db_context.select('ซันมินิมาร์ท'))
        # for row in db_context.select(1):
        #     print(row)
        # if 'ตัวอย่า' in db_context.select(1):
        #     print('yes')

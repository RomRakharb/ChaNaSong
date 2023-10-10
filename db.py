from PySide6.QtSql import QSqlDatabase, QSqlQuery


class Database:
    def __init__(self, db_name: str):
        self.db_name = db_name.upper()
    def __enter__(self):
        # Initialize the database connection
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database.db')

        # Open the database connection
        if not self.db.open():
            print("Unable to connect to the database")
            raise RuntimeError("Database connection failed")
        return self

    def select(self, column: int) -> list[str]:
        data_list = []
        query = QSqlQuery()
        query.exec(f"SELECT * FROM {self.db_name} ORDER BY NAME DESC")
        while query.next():
            data_list.append(query.value(column))
        return data_list

    def __exit__(self, exc_type, exc_value, traceback):
        # Close the database connection when exiting the context
        self.db.close()


if __name__ == "__main__":
    with Database('addressee') as db_context:
        for row in db_context.select(1):
            print(row)

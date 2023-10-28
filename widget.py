from PySide6.QtWidgets import QApplication, QComboBox, QCompleter
from PySide6.QtCore import Qt, QStringListModel
from PySide6.QtGui import QFont

from db import Database

font = 'Arial'
font_size = 20

class SearchableComboBox(QComboBox):
    def __init__(self, table: str):
        super().__init__()
        self.table = table
        with Database(table) as db_context:
            items = db_context.select(1)
        self.setEditable(True)
        self.setMaxVisibleItems(5)

        self.completer = QCompleter(items)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchContains)

        self.setCompleter(self.completer)

        self.addItems(items)

        self.clearEditText()
        self.setFont(QFont(font, font_size))
        popup = self.completer.popup()
        popup.setFont(QFont(font, font_size))

    def reset(self):
        self.clearEditText()
        with Database(self.table) as db_context:
            items = db_context.select(1)
        self.clear()
        self.addItems(items)
        self.clearEditText()

        model = QStringListModel()
        model.setStringList(items)
        self.completer.setModel(model)


# class AddresseeDetail:


def on_item_selected(item):
    print(f"Selected item: {item}")


if __name__ == "__main__":
    app = QApplication([])
    fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]
    combo = SearchableComboBox('ADDRESSEE')
    combo.reset()
    combo.show()
    # combo.activated.connect(lambda: on_item_selected(combo.currentText()))
    app.exec()

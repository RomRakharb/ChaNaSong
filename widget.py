from PySide6.QtWidgets import QApplication, QComboBox, QCompleter
from PySide6.QtCore import Qt


class ComboBox(QComboBox):
    def __init__(self, item):
        super().__init__()

        self.setEditable(True)
        self.setMaxVisibleItems(5)

        completer = QCompleter(item)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)

        self.setCompleter(completer)

        self.addItems(item)

        self.clearEditText()


def on_item_selected(item):
    print(f"Selected item: {item}")


if __name__ == "__main__":
    app = QApplication([])
    items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]
    combo = ComboBox(items)
    combo.show()

    combo.activated.connect(lambda: on_item_selected(combo.currentText()))

    app.exec()

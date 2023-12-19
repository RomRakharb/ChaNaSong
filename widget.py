from PySide6.QtWidgets import QApplication, QComboBox, QCompleter, QMessageBox, QLineEdit, QVBoxLayout, QInputDialog
from PySide6.QtCore import Qt, QStringListModel

from db import Database


class SearchableComboBox(QComboBox):
    def __init__(self, table: str):
        super().__init__()
        self.table = table
        with Database(table) as db_context:
            items = db_context.select_col(1)
        self.setEditable(True)
        self.setMaxVisibleItems(5)

        self.completer = QCompleter(items)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchContains)

        self.setCompleter(self.completer)

        self.addItems(items)

        self.clearEditText()
        # popup = self.completer.popup()

    def reset(self):
        self.clearEditText()
        with Database(self.table) as db_context:
            items = db_context.select_col(1)
        self.clear()
        self.addItems(items)
        self.clearEditText()

        model = QStringListModel()
        model.setStringList(items)
        self.completer.setModel(model)


def confirm_delete():
    msg_box = QMessageBox()

    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setText("ต้องการลบรายการนี้ ใช่หรือไม่")
    msg_box.setWindowTitle("ลบรายการ")

    ok_button = msg_box.addButton("ยืนยัน", QMessageBox.AcceptRole)
    cancel_button = msg_box.addButton("ยกเลิก", QMessageBox.RejectRole)

    result = msg_box.exec()

    if msg_box.clickedButton() == ok_button:
        return True
    elif msg_box.clickedButton() == cancel_button:
        return False


def not_send_name():
    user_input, ok_pressed = QInputDialog.getText(None, "Input Dialog", "Please enter your name:")
    if ok_pressed:
        return f"({user_input})"
    else:
        return "()"


def on_item_selected(item):
    print(f"Selected item: {item}")


if __name__ == "__main__":
    app = QApplication([])
    not_send_name()
    # fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]
    # combo = SearchableComboBox('ADDRESSEE')
    # combo.reset()
    # combo.show()
    # combo.activated.connect(lambda: on_item_selected(combo.currentText()))
    app.exec()

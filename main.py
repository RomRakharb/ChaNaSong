from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
    QLineEdit,
    QLabel,
    QFormLayout,
    QVBoxLayout,
    QHBoxLayout,
    QCheckBox,
)

from pdf import envelope, a4
from db import Database
from widget import SearchableComboBox

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("จ่าหน้าซอง")

        # start outer layout
        layout = QHBoxLayout()

        # start left layout
        left_layout = QFormLayout()
        left_layout.setVerticalSpacing(10)
        self.name_cbb = SearchableComboBox('addressee')
        self.name_cbb.activated.connect(self.name_selected)
        self.name_le = QLineEdit()
        self.detail_1 = QLineEdit()
        self.detail_2 = QLineEdit()
        self.detail_3 = QLineEdit()
        self.detail_4 = QLineEdit()
        self.detail_5 = QLineEdit()
        left_layout.addRow("", self.name_cbb)
        self.org_name_lb = QLabel("ชื่อหน่วยงาน: ")
        left_layout.addRow(self.org_name_lb, self.name_le)
        self.start_lb = QLabel("เรียน")
        left_layout.addRow(self.start_lb, self.detail_1)
        left_layout.addRow("", self.detail_2)
        left_layout.addRow("", self.detail_3)
        left_layout.addRow("", self.detail_4)
        left_layout.addRow("", self.detail_5)
        # finish left layout

        # start right layout
        right_layout = QVBoxLayout()
        self.print_bt = QPushButton("พิมพ์")
        self.print_bt.released.connect(self.print)
        self.reset_bt = QPushButton("รีเซ็ต")
        self.reset_bt.released.connect(self.reset)
        self.edit_bt = QPushButton("แก้ไข")
        self.edit_bt.released.connect(self.edit)
        self.add_bt = QPushButton("เพิ่ม")
        self.add_bt.released.connect(self.add)
        self.delete_bt = QPushButton("ลบ")
        self.delete_bt.released.connect(self.delete)
        self.a4_chb = QCheckBox("ขนาด A4")
        self.not_send_chb = QCheckBox("ไม่ส่ง")

        for button in [self.print_bt, self.reset_bt, self.edit_bt, self.add_bt, self.delete_bt]:
            button.setAutoDefault(True)

        right_layout.addWidget(self.print_bt)
        right_layout.addWidget(self.reset_bt)
        right_layout.addWidget(self.edit_bt)
        right_layout.addWidget(self.add_bt)
        right_layout.addWidget(self.delete_bt)
        right_layout.addWidget(self.a4_chb)
        right_layout.addWidget(self.not_send_chb)
        # finish right layout

        layout.addLayout(left_layout)
        layout.addLayout(right_layout)
        # finish outer layout

        self.set_font()
        self.reset()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def name_selected(self, text):
        if isinstance(text, int):
            data = self.name_cbb.itemText(text)
        else:
            data = text.data()
        with Database('ADDRESSEE') as db_context:
            for row, value in enumerate(db_context.select_col(1)):
                if value == data:
                    self.name_cbb.setEditText(db_context.select_col(1)[row])
                    self.name_le.setText(db_context.select_col(1)[row])
                    self.detail_1.setText(db_context.select_col(2)[row])
                    self.detail_2.setText(db_context.select_col(3)[row])
                    self.detail_3.setText(db_context.select_col(4)[row])
                    self.detail_4.setText(db_context.select_col(5)[row])
                    self.detail_5.setText(db_context.select_col(6)[row])

    @staticmethod
    def set_font():
        font_path = "./resource/THSarabunNew.ttf"
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font_size = 28
        app_font = QFont(font_family, font_size)
        QApplication.setFont(app_font)

    def print(self):
        if self.name_le != "":
            with Database('ADDRESSEE') as db_context:
                envelope(db_context.select(self.name_le.text()))

    def reset(self):
        self.line_state(False)
        self.line_clear()
        self.button_state(True)

        self.name_cbb.setEnabled(True)
        self.name_cbb.clear()
        with Database('ADDRESSEE') as db_context:
            for row in db_context.select_col(1):
                self.name_cbb.addItem(row)
        self.name_cbb.clearEditText()
        self.name_cbb.setFocus()

    def edit(self):
        if self.print_bt.isEnabled() and self.name_le.text() != "" and self.detail_1.text() != "":
            self.line_state(True)
            self.button_state(False, [1])
            self.name_cbb.setEnabled(False)
        elif self.name_le.text() != "" and self.detail_1.text() != "":
            with Database('ADDRESSEE') as db_context:
                if self.name_le.text() in db_context.select_col(1) and self.name_le.text() != self.name_cbb.currentText():
                    return None
                db_context.delete(self.name_cbb.currentText())
                db_context.insert(
                    self.name_le.text(),
                    self.detail_1.text(),
                    self.detail_2.text(),
                    self.detail_3.text(),
                    self.detail_4.text(),
                    self.detail_5.text())
                self.reset()

    def add(self):
        if self.print_bt.isEnabled():
            self.line_state(True)
            self.line_clear()
            self.button_state(False, [2])
            self.name_cbb.clear()
            self.name_cbb.setEnabled(False)
        elif self.name_le.text() != "" and self.detail_1.text() != "":
            with Database('ADDRESSEE') as db_context:
                if self.name_le.text() in db_context.select_col(1):
                    return None
                db_context.insert(
                    self.name_le.text(),
                    self.detail_1.text(),
                    self.detail_2.text(),
                    self.detail_3.text(),
                    self.detail_4.text(),
                    self.detail_5.text())
                self.reset()

    def delete(self):
        if self.print_bt.isEnabled() and self.name_le.text() != "" and self.detail_1.text() != "":
            with Database('ADDRESSEE') as db_context:
                db_context.delete(self.name_le.text())
                self.reset()

    def line_state(self, state: bool):
        le_list = [
            self.name_le,
            self.detail_1,
            self.detail_2,
            self.detail_3,
            self.detail_4,
            self.detail_5
        ]
        for each_widget in le_list:
            each_widget.setEnabled(state)

    def line_clear(self):
        le_list = [
            self.name_le,
            self.detail_1,
            self.detail_2,
            self.detail_3,
            self.detail_4,
            self.detail_5
        ]
        for each_widget in le_list:
            each_widget.clear()

    def button_state(self, state: bool, except_button=[]):
        button_list = [
            self.print_bt,
            self.edit_bt,
            self.add_bt,
            self.delete_bt,
            self.a4_chb,
            self.not_send_chb
        ]
        for index, value in enumerate(button_list):
            if index in except_button:
                value.setEnabled(not state)
            else:
                value.setEnabled(state)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()

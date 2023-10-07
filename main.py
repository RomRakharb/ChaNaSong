from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QComboBox,
    QWidget,
    QLineEdit,
    QLabel,
    QListWidget,
    QFormLayout,
    QVBoxLayout,
    QHBoxLayout,
    QCheckBox,
)

import sys
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zong")

        test_list = ["One", "Two", "Three"]
        font = 'Arial'
        font_size = 20

        # start outer layout
        layout = QHBoxLayout()

        # start left
        left_layout = QFormLayout()
        left_layout.setVerticalSpacing(10)
        self.title_cbb = QComboBox()
        self.title_cbb.setEditable(True)
        self.title_cbb.addItems(test_list)
        self.title_cbb.currentIndexChanged.connect(self.index_changed)
        self.title_cbb.currentTextChanged.connect(self.text_changed)
        self.title_le = QLineEdit()
        self.line_one_le = QLineEdit()
        self.line_two_le = QLineEdit()
        self.line_three_le = QLineEdit()
        self.line_four_le = QLineEdit()
        self.line_five_le = QLineEdit()
        left_layout.addRow("", self.title_cbb)
        self.org_name_lb = QLabel("ชื่อหน่วยงาน: ")
        left_layout.addRow(self.org_name_lb, self.title_le)
        self.start_lb = QLabel("เรียน")
        left_layout.addRow(self.start_lb, self.line_one_le)
        left_layout.addRow("", self.line_two_le)
        left_layout.addRow("", self.line_three_le)
        left_layout.addRow("", self.line_four_le)
        left_layout.addRow("", self.line_five_le)
        # finish left

        # start middle
        self.all_list = QListWidget()
        self.all_list.addItems(test_list)
        # finish middle

        # start right
        right_layout = QVBoxLayout()
        self.print_bt = QPushButton("Print")
        self.reset_bt = QPushButton("Reset")
        self.reset_bt.released.connect(self.reset)
        self.edit_bt = QPushButton("Edit")
        self.add_bt = QPushButton("Add")
        self.delete_bt = QPushButton("Delete")
        self.a4_chb = QCheckBox("ขนาด A4")
        self.not_send_chb = QCheckBox("ไม่ส่ง")
        right_layout.addWidget(self.print_bt)
        right_layout.addWidget(self.reset_bt)
        right_layout.addWidget(self.edit_bt)
        right_layout.addWidget(self.add_bt)
        right_layout.addWidget(self.delete_bt)
        right_layout.addWidget(self.a4_chb)
        right_layout.addWidget(self.not_send_chb)
        # finish right

        layout.addLayout(left_layout)
        layout.addWidget(self.all_list)
        layout.addLayout(right_layout)
        # finish outer layout

        self.set_font()
        self.reset()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def index_changed(self, index):  # index is an int stating from 0
        print(index)

    def text_changed(self, text):  # text is a str
        print(text)

    def set_font(self):
        font = 'Arial'
        font_size = 20
        widget_list = [
            self.title_cbb,
            self.title_le,
            self.line_one_le,
            self.line_two_le,
            self.line_three_le,
            self.line_four_le,
            self.line_five_le,
            self.org_name_lb,
            self.start_lb,
            self.all_list,
            self.print_bt,
            self.reset_bt,
            self.edit_bt,
            self.add_bt,
            self.delete_bt,
            self.a4_chb,
            self.not_send_chb
        ]
        for each_widget in widget_list:
            each_widget.setFont(QFont(font, font_size))

    def reset(self):
        widget_list = [
            self.title_le,
            self.line_one_le,
            self.line_two_le,
            self.line_three_le,
            self.line_four_le,
            self.line_five_le
        ]
        for each_widget in widget_list:
            each_widget.setText("")
            each_widget.setDisabled(True)
        self.title_cbb.setEditText("--เลือกหัวข้อ--")

        conn = sqlite3.connect('database.db')
        with conn:
            cursor = conn.cursor()
            data = cursor.execute('''SELECT TITLE FROM ADDRESSEE''')
        for row in data:
            self.title_cbb.addItems(row)
            self.all_list.addItems(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
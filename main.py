from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
    QLineEdit,
    QLabel,
    QListWidget,
    QFormLayout,
    QVBoxLayout,
    QHBoxLayout,
    QCheckBox,
)

from db import Database
from widget import ComboBox

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zong")

        # start outer layout
        layout = QHBoxLayout()

        # start left
        left_layout = QFormLayout()
        left_layout.setVerticalSpacing(10)
        with Database('addressee') as db_context:
            self.name_cbb = ComboBox(db_context.select(1))
        self.name_cbb.activated.connect(self.name_selected)
        self.name_le = QLineEdit()
        self.line_one = QLineEdit()
        self.line_two = QLineEdit()
        self.line_three = QLineEdit()
        self.line_four = QLineEdit()
        self.line_five = QLineEdit()
        left_layout.addRow("", self.name_cbb)
        self.org_name_lb = QLabel("ชื่อหน่วยงาน: ")
        left_layout.addRow(self.org_name_lb, self.name_le)
        self.start_lb = QLabel("เรียน")
        left_layout.addRow(self.start_lb, self.line_one)
        left_layout.addRow("", self.line_two)
        left_layout.addRow("", self.line_three)
        left_layout.addRow("", self.line_four)
        left_layout.addRow("", self.line_five)
        # finish left

        # start middle
        self.name_list = QListWidget()
        self.name_list.activated.connect(self.name_selected)
        # finish middle

        # start right
        right_layout = QVBoxLayout()
        self.print_bt = QPushButton("Print")
        self.reset_bt = QPushButton("Reset")
        self.reset_bt.released.connect(self.reset)
        self.edit_bt = QPushButton("Edit")
        self.edit_bt.released.connect(self.edit)
        self.add_bt = QPushButton("Add")
        self.add_bt.released.connect(self.add_mode)
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
        layout.addWidget(self.name_list)
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
        with Database('addressee') as db_context:
            for row, value in enumerate(db_context.select(1)):
                if value == data:
                    self.name_cbb.setEditText(db_context.select(1)[row])
                    self.name_le.setText(db_context.select(1)[row])
                    self.line_one.setText(db_context.select(2)[row])
                    self.line_two.setText(db_context.select(3)[row])
                    self.line_three.setText(db_context.select(4)[row])
                    self.line_four.setText(db_context.select(5)[row])
                    self.line_five.setText(db_context.select(6)[row])

    def set_font(self):
        font = 'Arial'
        font_size = 20
        widget_list = [
            self.name_cbb,
            self.name_le,
            self.line_one,
            self.line_two,
            self.line_three,
            self.line_four,
            self.line_five,
            self.org_name_lb,
            self.start_lb,
            self.name_list,
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
        self.line_state(False)
        self.button_state(True)

        self.name_cbb.setEnabled(True)
        self.name_cbb.clear()
        self.name_list.setEnabled(True)
        self.name_list.clear()
        with Database('addressee') as db_context:
            for row in db_context.select(1):
                self.name_cbb.addItem(row)
                self.name_list.addItem(row)
        self.name_cbb.setEditText("")

    def edit(self):
        if self.name_le.text() == "":
            print('pass')
        else:
            self.name_cbb.setDisabled(True)
            self.print_bt.setDisabled(True)

            self.name_le.setEnabled(True)
            self.line_one.setEnabled(True)
            self.line_two.setEnabled(True)
            self.line_three.setEnabled(True)
            self.line_four.setEnabled(True)
            self.line_five.setEnabled(True)
        pass

    def add_mode(self):
        if self.print_bt.isEnabled():
            self.line_state(True)
            self.button_state(False, [2])
            self.name_cbb.setEditText('')
            self.name_cbb.setEnabled(False)
        else:
            if self.name_le.text() != "" and self.name_le.text() != "":
                print('add')

    def line_state(self, state: bool):
        le_list = [
            self.name_le,
            self.line_one,
            self.line_two,
            self.line_three,
            self.line_four,
            self.line_five
        ]
        for each_widget in le_list:
            each_widget.setText("")
            each_widget.setEnabled(state)

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

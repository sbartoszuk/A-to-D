#!/usr/bin/env python3

'''module: dialogWindows'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget

try:
    import dataImportExport as dataIE
except:
    from modules import dataImportExport as dataIE

class CAcceptDialog(QDialog):

    accepted = pyqtSignal(bool)

    def __init__(self, phrase, btn_1_text, btn_2_text):
        super().__init__()

        font = QFont('Coolvetica Rg', 17)

        self.setWindowTitle('Accept')

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        container_layout = QVBoxLayout(self)
        container_frame = QFrame()
        container_frame.setStyleSheet('background: black;'
                                      'border-radius: 30px;')
        container_frame.setContentsMargins(70, 10, 70, 10)
        container_layout.addWidget(container_frame)

        layout = QVBoxLayout()
        layout.setSpacing(20)
        container_frame.setLayout(layout)

        layout.addSpacerItem(QSpacerItem(0, 20))

        comunicate = QLabel(phrase)
        comunicate.setFont(font)
        comunicate.setStyleSheet('color: white;')
        layout.addWidget(comunicate)

        btn_container = QFrame()
        layout.addWidget(btn_container)
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(30)
        btn_container.setLayout(btn_layout)

        btn_1 = QPushButton(btn_1_text, self)
        #btn_1.clicked.connect(self.siema)
        btn_2 = QPushButton(btn_2_text, self)
        #btn_2.clicked.connect(self.siema)

        for button in [btn_1, btn_2]:
            button.setFixedHeight(35)
            button.setStyleSheet('QPushButton{'
                                    'background: white;'
                                    'border-radius: 10px;'
                                  '}'
                                  'QPushButton:hover{'
                                    'background: rgb(180, 180, 180);'
                                  '}'
                                  'QPushButton:pressed{'
                                    'background: gray;'
                                  '}'
                                  )
            button.setFont(font)

        btn_layout.addWidget(btn_1)
        btn_layout.addWidget(btn_2)
        layout.addSpacerItem(QSpacerItem(0, 20))

        btn_1.clicked.connect(self.accept_action)
        btn_2.clicked.connect(self.reject_action)
    
    def accept_action(self):
        self.accepted.emit(True)
        self.close()

    def reject_action(self):
        self.accepted.emit(False)
        self.close()

class OkDialog(QDialog):
    def __init__(self, phrase):
        super().__init__()

        self.setWindowTitle('Warning')

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        font = QFont('Coolvetica Rg', 17)

        container_layout = QVBoxLayout(self)
        container_frame = QFrame()
        container_frame.setStyleSheet('background: black;'
                                      'border-radius: 30px;')
        container_frame.setContentsMargins(70, 10, 70, 10)
        container_layout.addWidget(container_frame)

        layout = QVBoxLayout()
        layout.setSpacing(30)
        container_frame.setLayout(layout)

        comunicate = QLabel(phrase)
        comunicate.setContentsMargins(0, 20, 0, 0)
        comunicate.setStyleSheet('color: white;')
        comunicate.setFont(font)
        layout.addWidget(comunicate)

        confirm_btn = QPushButton('ok')
        confirm_btn.setFixedHeight(35)
        confirm_btn.setStyleSheet('QPushButton{'
                                    'background: white;'
                                    'border-radius: 10px;'
                                  '}'
                                  'QPushButton:hover{'
                                    'background: rgb(180, 180, 180);'
                                  '}'
                                  'QPushButton:pressed{'
                                    'background: gray;'
                                  '}'
                                  )
        confirm_btn.setFont(font)
        confirm_btn.clicked.connect(self.accept)
        layout.addWidget(confirm_btn)

        layout.addSpacerItem(QSpacerItem(1,20))

class EnterDialog(QDialog):

    textEntered = pyqtSignal(str)

    def __init__(self, phrase):
        super().__init__()

        self.setWindowTitle('Enter data')

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        container_layout = QVBoxLayout(self)
        container_frame = QFrame()
        container_frame.setStyleSheet('background: black;'
                                      'border-radius: 30px;')
        container_frame.setContentsMargins(70, 10, 70, 10)
        container_layout.addWidget(container_frame)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.setSpacing(30)
        container_frame.setLayout(layout)

        font = QFont('Coolvetica Rg', 17)
        self.setFont(font)

        label = QLabel(phrase)
        label.setStyleSheet('color: white;')
        label.setFont(font)
        label.setAlignment(Qt.AlignHCenter)
        layout.addWidget(label)

        self.line_edit = QLineEdit(self)
        self.line_edit.setAlignment(Qt.AlignHCenter)
        self.line_edit.setPlaceholderText('new name')
        self.line_edit.setMaxLength(13)
        layout.addWidget(self.line_edit)
        
        ok_button = QPushButton("ok", self)
        ok_button.clicked.connect(self.accept_input)
        layout.addWidget(ok_button)
        layout.addSpacerItem(QSpacerItem(1, 25))

        for item in [ok_button, self.line_edit]:
            item.setFixedHeight(35)
            item.setFont(font)

        self.line_edit.setStyleSheet('border-radius: 15px;'
                                    'background: white;'
                                    'color: black;'
                                    'padding-left: 20px;'
                                    'padding-right: 20px;')

        ok_button.setStyleSheet('QPushButton{'
                                    'border-radius: 15px;'
                                    'background: white;'
                                    'color: black;'
                                    'padding-left: 20px;'
                                    'padding-right: 20px;'
                                '}'
                                'QPushButton:hover{'
                                  'background: rgb(180, 180, 180);'
                                '}'
                                    'QPushButton:pressed{'
                                    'background: gray;'
                                '}')
    def accept_input(self):
        entered_text = self.line_edit.text()
        if entered_text != '':
          if self.fileNameCheck(entered_text):
            if dataIE.RListCheck(entered_text):
              self.textEntered.emit(entered_text)
              self.accept()

    def fileNameCheck(self, name):
        non_acceptable_chars = [None , '\\' , '/' , ':' , '*' , '?' , '"' , '<' , '>' , '|']

        if name[0] == ' ' or name[-1] == ' ':
            return False
        elif name[-1] == '.':
            return False
        for i in range(len(name)):
            if name[i] in non_acceptable_chars:
                return False
        return True
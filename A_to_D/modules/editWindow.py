#!/usr/bin/env python3

'''module: editWindow'''

import getpass
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtGui import QIntValidator
try:
    import dataImportExport as dataIE
except:
    from modules import dataImportExport as dataIE


class CWindowEdit(QFrame):
    def __init__(self):
        super(CWindowEdit, self).__init__()

        font_big = QtGui.QFont('Coolvetica Rg', 15)
        font_small = QtGui.QFont('Coolvetica Rg', 12)
        font_time = QtGui.QFont('Arial', 12)
        
        self.setStyleSheet('background-color: rgba(141, 168, 167, 90);'
                               'border-radius: 20')
        self.setFixedHeight(570)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        layout.setSpacing(20)
        self.setLayout(layout)

        layout.addSpacerItem(QSpacerItem(10, 5))

        top_but_frm = QFrame()
        top_but_frm.setStyleSheet('background-color: rgba(141, 168, 167, 90);'
                               'border-radius: 20')
        top_but_frm.setContentsMargins(0,0,0,10)
        layout.addWidget(top_but_frm)
        top_but_lay = QVBoxLayout()
        top_but_lay.setSpacing(12)
        top_but_frm.setLayout(top_but_lay)


        self.import_btn = QPushButton('import tasks')
        export_btn = QPushButton('export tasks')
        self.add_btn = QPushButton('+')
        self.remove_btn = QPushButton('-')
        self.reset_btn = QPushButton('reset')

        for i, button in enumerate([self.import_btn, export_btn, self.add_btn, self.remove_btn, self.reset_btn]):
            
            if i < 2:
                button.setStyleSheet('QPushButton{'
                                        'background: rgb(178, 157, 209);'
                                        'color: white;'
                                        'border-radius: 15px;'
                                    '}'
                                    'QPushButton:hover{'
                                    'background: rgb(165, 145, 190);'
                                    '}'
                                    'QPushButton:pressed{'
                                    'background: gray;'
                                    '}'
                                    )
                button.setFixedHeight(50)
                button.setFixedWidth(300)
                button.setFont(font_big)
                top_but_lay.addWidget(button)
            else:
                if i > 3:
                    button.setFixedWidth(280)
                    button.setFixedHeight(30)
                    button.setFont(font_small)
                    button.setStyleSheet('QPushButton{'
                                            'background: rgb(178, 157, 209);'
                                            'color: white;'
                                            'border-radius: 10px;'
                                        '}'
                                        'QPushButton:hover{'
                                        'background: rgb(165, 145, 190);'
                                        '}'
                                        'QPushButton:pressed{'
                                        'background: gray;'
                                        '}'
                                        )
                else:
                    button.setFixedWidth(135)
                    button.setFixedHeight(30)
                    button.setFont(font_big)
                    button.setStyleSheet('QPushButton{'
                                            'background: white;'
                                            'color: black;'
                                            'border-radius: 10px;'
                                        '}'
                                        'QPushButton:hover{'
                                        'background: rgb(165, 145, 190);'
                                        '}'
                                        'QPushButton:pressed{'
                                        'background: gray;'
                                        '}'
                                        )
                    
        layout.addSpacerItem(QSpacerItem(10, 30))
        
        edit_frm = QFrame()
        edit_frm.setStyleSheet('background-color: rgba(141, 168, 167, 90);'
                               'border-radius: 20')
        layout.addWidget(edit_frm, alignment=Qt.AlignHCenter)

        edit_layout = QVBoxLayout()
        edit_layout.setAlignment(Qt.AlignTop)
        edit_frm.setLayout(edit_layout)

        self.task_place_holder = QLineEdit()
        self.task_place_holder.setPlaceholderText('enter task')
        self.task_place_holder.setMaxLength(17)
        self.task_place_holder.setFixedWidth(280)
        self.task_place_holder.setFixedHeight(70)
        self.task_place_holder.setStyleSheet('background: white;'
                                        'color: rgb(120,120,120);'
                                        'border-radius: 20px;'
                                        'padding-left: 25px;'
                                        'padding-right: 25px;'
                                        'selection-background-color: rgb(142, 59, 255);')
        self.task_place_holder.setFont(font_big)
        self.task_place_holder.setAlignment(Qt.AlignCenter)
        edit_layout.addWidget(self.task_place_holder, alignment=Qt.AlignHCenter)
        edit_layout.addSpacerItem(QSpacerItem(10, 10))

        task_time_frame = QFrame()
        task_time_frame.setFixedWidth(280)
        task_time_frame.setStyleSheet('background: white;'
                                      'border-radius: 20')
        edit_layout.addWidget(task_time_frame, alignment=Qt.AlignCenter)
        task_time_layout = QHBoxLayout()
        task_time_layout.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
        task_time_frame.setLayout(task_time_layout)

        self.hour_place_holder = QLineEdit()
        self.minute_place_holder = QLineEdit()
        int_only = QIntValidator(self)
        self.hour_place_holder.setPlaceholderText('hh')
        self.minute_place_holder.setPlaceholderText('mm')

        for holder in [self.hour_place_holder, self.minute_place_holder]:
            holder.setFixedHeight(50)
            holder.setFont(font_time)
            holder.setFixedWidth(60)
            holder.setStyleSheet('background: rgb(230,230,230);'
                                'color: rgb(120,120,120);'
                                'border-radius: 20px;'
                                'selection-background-color: rgb(142, 59, 255);')
            holder.setMaxLength(2)
            holder.setValidator(int_only)
            holder.setAlignment(Qt.AlignCenter)
        
        task_time_layout.addWidget(self.hour_place_holder, alignment=Qt.AlignCenter)
        task_time_layout.addWidget(QLabel(':'), alignment=Qt.AlignCenter)
        task_time_layout.addWidget(self.minute_place_holder, alignment=Qt.AlignCenter)

        func_btn_frm = QFrame()
        func_btn_frm.setStyleSheet('background: rgba(0,0,0,0)')
        edit_layout.addWidget(func_btn_frm)
        func_btn_layout = QHBoxLayout()
        func_btn_frm.setLayout(func_btn_layout)
        
        func_btn_layout.addWidget(self.add_btn)
        func_btn_layout.addWidget(self.remove_btn)
        edit_layout.addWidget(self.reset_btn, alignment=Qt.AlignHCenter)

        edit_layout.addSpacerItem(QSpacerItem(10, 30))

        export_btn.clicked.connect(self.ExportData)
        
    def ExportData(self):
        options = QFileDialog.Options()
        file_dialog = QFileDialog()
        file_dialog.setOptions(options)
        username = getpass.getuser()
        file_dialog.setDirectory('C:/Users/' + username +'/Desktop')
        file_dialog.setNameFilter("Swipe Plan Data(*.plan)")
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()[0]
            dataIE.DSaveAs(selected_files)
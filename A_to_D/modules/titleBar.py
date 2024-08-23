#!/usr/bin/env python3 

'''module: titleBar'''

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import os
                    
class Build(QFrame):
    __tsk_w = 300-30 - 70 - 80 + 40 + 30 + 10
    __tsk_h = 20
    __tsk_rad = '10'

    def __init__(self):
        super(Build, self).__init__()

        if os.path.exists('../resources/graphics'):
            mini_path = '../'
        else:
            mini_path = ''

        self.label = QLabel()
        self.label.setFixedWidth(Build.__tsk_w)
        self.label.setFixedHeight(Build.__tsk_h)
        
        self.close_btn = QPushButton()
        self.close_btn.setFixedWidth(12)
        self.close_btn.setFixedHeight(12)

        self.maximize_btn = QPushButton()
        self.maximize_btn.setFixedWidth(48)
        self.maximize_btn.setFixedHeight(12)

        self.close_btn.setStyleSheet('QPushButton{'
                                        'background-image : url(' + mini_path + 'resources/graphics/close_btn.png);'
                                    '}'
                                    'QPushButton:hover{'
                                        'background-image : url(' + mini_path + 'resources/graphics/close_btn_hover.png);'
                                    '}'
                                     )

        self.maximize_btn.setStyleSheet('QPushButton{'
                                        'background-image : url(' + mini_path + 'resources/graphics/maximize_btn.png);'
                                    '}'
                                    'QPushButton:hover{'
                                        'background-image : url(' + mini_path + 'resources/graphics/maximize_btn_hover.png);'
                                    '}'
                                     )
        
        layout = QHBoxLayout()
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        
        layout.addWidget(self.label)
        layout.addWidget(self.maximize_btn)
        layout.addWidget(self.close_btn)
        self.setLayout(layout)  
        self.setStyleSheet(
            'border-radius: ' + Build.__tsk_rad + 'px;'
            'background: white;'
            )

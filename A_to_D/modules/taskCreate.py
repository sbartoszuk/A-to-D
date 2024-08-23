#!/usr/bin/env python3 

'''module: taskCreate'''

from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from datetime import datetime, timedelta

class NCBox(QFrame):
    def __init__(self, type, time):
        super(NCBox, self).__init__()
        
        def tF(time):
            return '0'*(2 - len(str(time))) + str(time)
        
        font = QtGui.QFont('Coolvetica Rg', 15)
        font2 = QtGui.QFont('Comic Sans', 11)
        self.setFont(font)
        self.setFixedHeight(30)
        self.setStyleSheet(
            'border-radius: 15px;'
            'background: rgb(205, 195, 219);'
            'color: rgb(131, 38, 166);'
            )
        self.setContentsMargins(17, 0, 15, 0)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

        time_now = datetime.now()
        task_length = timedelta(minutes=int(time))
        time_end = time_now + task_length
        
        h_now = tF(time_now.hour)
        m_now = tF(time_now.minute)
        
        h_end = tF(time_end.hour)
        m_end = tF(time_end.minute)

        type_label = QLabel()
        time_label = QLabel()

        for label in [type_label, time_label]: 
            label.setStyleSheet('border-radius: 0px;')
            label.setFixedHeight(30)
            label.setContentsMargins(0,0,0,0)

        type_label.setFont(font)
        type_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        time_label.setFont(font2)
        time_label.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        
        type_label.setText(type)
        self.layout.addWidget(type_label)
        
        if time != '0':
            if type == 'now':
                time_label.setText(h_now + ':' + m_now + ' - ' + h_end + ':' + m_end)
            elif type == 'next':
                time_label.setText(h_end + ':' + m_end)
            self.layout.addWidget(time_label)
        '''
        else:
            time_label.setText('')
            self.layout.addWidget(time_label)
            self.layout.removeWidget(time_label)
            '''
        
class routineBox(QFrame):
    __tsk_w = 300
    __tsk_h = 50
    __tsk_rad = '20'
    def __init__(self, name, empty=False):
        super(routineBox, self).__init__()
        font = QtGui.QFont('Coolvetica Rg', 15)

        self.setFixedWidth(routineBox.__tsk_w)
        self.setFixedHeight(routineBox.__tsk_h)
        self.setContentsMargins(0, 0, 0, 0)
        
        self.setStyleSheet('QFrame{'
            'border-radius: ' + routineBox.__tsk_rad + 'px;'
            'background: white;'
            'color: rgb(140, 156, 156);'
            '}'
            )
        
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        if not empty:
            self.edit_btn = QPushButton()
            self.edit_btn.setObjectName('edit_btn')
            self.del_btn = QPushButton()
            self.del_btn.setObjectName('del_btn')

            for button in [self.edit_btn, self.del_btn]:
                button.setFixedHeight(self.__tsk_h)
                button.setFixedWidth(self.__tsk_h)
                button.setStyleSheet('QPushButton{'
                                    'background: rgba(0,0,0,0);'
                                    '}'
                                    'QPushButton:hover{'
                                    'background: rgba(0,0,0,0);'
                                    '}'
                                    )
                
            edit_btn_layout = QHBoxLayout()
            del_btn_layout = QHBoxLayout()

            for lay in [edit_btn_layout, del_btn_layout]:
                lay.setContentsMargins(0,0,0,0)
                lay.setAlignment(Qt.AlignCenter | Qt.AlignCenter)

            self.edit_btn.setLayout(edit_btn_layout)
            self.del_btn.setLayout(del_btn_layout)

            edit_icon = QLabel()
            del_icon = QLabel()
            width = 25
            heigth = 10
            opacity = 100
            opacity_hover = 255
            for icon in [edit_icon, del_icon]:
                icon.setFixedHeight(heigth)
                icon.setFixedWidth(width)
                if icon == edit_icon:
                    icon.setStyleSheet( 'QLabel{'
                                        'background: rgba(0, 0, 255, ' + str(opacity) + ');'
                                        'border-radius: ' + str(heigth//2) + ';'
                                        '}'
                                        'QLabel:hover{'
                                        'background: rgba(0, 0, 255, ' + str(opacity_hover) + ');'
                                        '}'
                                    )
                    edit_btn_layout.addWidget(icon)
                else:
                    icon.setStyleSheet( 'QLabel{'
                                        'background: rgba(142, 59, 255, ' + str(opacity) + ');'
                                        'border-radius: ' + str(heigth//2) + ';'
                                        '}'
                                        'QLabel:hover{'
                                        'background: rgba(142, 59, 255, ' + str(opacity_hover) + ');'
                                        '}'
                                    )
                    del_btn_layout.addWidget(icon)

        self.text_btn = QPushButton(name)
        self.text_btn.setFont(font)
        self.text_btn.setFixedHeight(self.__tsk_h)
        self.text_btn.setStyleSheet('background: rgba(0,0,0,0);'
                                    'color: rgb(140, 156, 156);'
                                    )
        if not empty:
            self.layout.addWidget(self.edit_btn)
        
        self.layout.addWidget(self.text_btn)
        
        if not empty:
            self.layout.addWidget(self.del_btn)

class taskBox(QLabel):
    __tsk_w = 300
    __tsk_h = 50
    __tsk_rad = '20'
    def __init__(self, phrase):
        super(taskBox, self).__init__()
        #font = QFont('Monoround', 15)
        #font = QFont('Mesmerize Cd Eb', 15)
        #font = QtGui.QFont('Streetvertising', 12)
        font = QtGui.QFont('Coolvetica Rg', 15)

        self.managed = True

        self.setFont(font)
        self.setFixedWidth(taskBox.__tsk_w)
        self.setFixedHeight(taskBox.__tsk_h)
        self.setText(phrase)
        
        self.setStyleSheet(
            'border-radius: ' + taskBox.__tsk_rad + 'px;'
            'background: white;'
            'padding-left: 30;'
            'color: rgb(140, 156, 156);' 
            )
        drop_shadow = QGraphicsDropShadowEffect()
        drop_shadow.setBlurRadius(20)
        drop_shadow.setColor(QtGui.QColor(141, 168, 167, 120))
        drop_shadow.setOffset(3, 4)
        self.setGraphicsEffect(drop_shadow)
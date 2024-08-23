import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from modules import taskCreate as tskCreate
from modules import dataImportExport as dataIE
from modules import workWindow as workWin
from modules import editWindow as edWin
from modules import routinesWindow as rouWin

win_w = 320
win_h = 800

class CWindowBox(QWidget):
    def __init__(self) -> None:
        super(CWindowBox, self).__init__()

        self.setWindowTitle('Swipe Plan')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.main_layout = QHBoxLayout(self)
        self.main_layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)

        self.content = workWin.CWindowContent()
        self.routines = rouWin.CWindowRoutines()
        self.edit = edWin.CWindowEdit()

        self.main_layout.addWidget(self.routines, alignment=QtCore.Qt.AlignTop)
        self.main_layout.addWidget(self.content, alignment=QtCore.Qt.AlignTop)
        self.main_layout.addWidget(self.edit, alignment=QtCore.Qt.AlignTop)

        self.animation_duration = 300  # milliseconds
        self.opacity_effect1 = QGraphicsOpacityEffect()
        self.opacity_effect1.setOpacity(0)
        self.opacity_effect2 = QGraphicsOpacityEffect()
        self.opacity_effect2.setOpacity(0)

        self.routines.setGraphicsEffect(self.opacity_effect1)
        self.edit.setGraphicsEffect(self.opacity_effect2)

        self.setLayout(self.main_layout)
        self.c_maximized = False

        self.content.title_bar.label.mousePressEvent = self.MouseClick
        self.content.title_bar.label.mouseMoveEvent = self.MoveWindow
        self.content.title_bar.close_btn.clicked.connect(self.exit) 
        self.content.title_bar.maximize_btn.clicked.connect(self.MinMaxSwitch)
        self.clickPos = QtCore.QPoint(0,0)

        self.edit.import_btn.clicked.connect(self.content.ImportData)
        self.edit.add_btn.clicked.connect(lambda: self.content.AddTask(self.edit.task_place_holder.text(),
                                                                       self.edit.hour_place_holder.text(),
                                                                       self.edit.minute_place_holder.text()))
        self.edit.add_btn.clicked.connect(lambda: self.edit.task_place_holder.setText(''))
        self.edit.add_btn.clicked.connect(lambda: self.edit.hour_place_holder.setText(''))
        self.edit.add_btn.clicked.connect(lambda: self.edit.minute_place_holder.setText(''))
        
        self.edit.reset_btn.clicked.connect(self.content.EmptyTasks)
        self.edit.remove_btn.clicked.connect(self.content.DelTask)

        self.routines.updated.connect(self.RoutinesFilterRefresh)

        self.RoutinesFilterRefresh()

    def RoutinesFilterRefresh(self):
        for routine in self.routines.routines:
            routine.text_btn.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            self.SelectRoutine(obj)
        return super().eventFilter(obj, event)
    
    def SelectRoutine(self, obj):
        if obj.text() != 'no saved routines':
            name = obj.parent().text_btn.text()
            dataIE.RLoadToData(name)
            self.content.loadData()
    def MinMaxSwitch(self, event):
        if self.c_maximized:
            self.fadeOutContent()
            self.c_maximized = False
        else:
            self.fadeInContent()
            self.c_maximized = True

    
    def fadeInContent(self):
        self.opacity_effect1.setOpacity(0.0)
        self.animation = QPropertyAnimation(self.opacity_effect1, b"opacity")
        self.animation.setDuration(self.animation_duration)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.start()
        self.opacity_effect2.setOpacity(0.0)
        self.animation2 = QPropertyAnimation(self.opacity_effect2, b"opacity")
        self.animation2.setDuration(self.animation_duration)
        self.animation2.setStartValue(0.0)
        self.animation2.setEndValue(1.0)
        self.animation2.start()

    def fadeOutContent(self):
        self.animation = QPropertyAnimation(self.opacity_effect1, b"opacity")
        self.animation.setDuration(self.animation_duration)
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.start()
        self.animation2 = QPropertyAnimation(self.opacity_effect2, b"opacity")
        self.animation2.setDuration(self.animation_duration)
        self.animation2.setStartValue(1.0)
        self.animation2.setEndValue(0.0)
        self.animation2.start()


    def MoveWindow(self, event):
        self.move(self.pos() + event.globalPos() - self.clickPos)
        self.clickPos = event.globalPos()
        event.accept()
        pass
    def MouseClick(self, event):
        self.clickPos = event.globalPos()
        pass
    def exit(self):
        sys.exit()


AppHandler = QApplication(sys.argv)
App = CWindowBox()
App.show()
sys.exit(AppHandler.exec_())
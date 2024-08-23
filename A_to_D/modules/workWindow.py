#!/usr/bin/env python3 

'''module: workWindow'''

import getpass
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
try:
    import taskCreate as tskCreate
    import titleBar as tBar
    import dataImportExport as dataIE
except:
    from modules import taskCreate as tskCreate
    from modules import titleBar as tBar
    from modules import dataImportExport as dataIE

class CWindowContent(QFrame):
    def __init__(self):
        super(CWindowContent, self).__init__()
        
        blur = QGraphicsBlurEffect()
        blur.setBlurRadius(10)

        container_frame = QFrame()
        container_frame.setStyleSheet("background-color: rgba(217, 242, 247, 0);" +
                           'border-radius: 20px;')
        background_frame = QFrame()
        background_frame.setStyleSheet("background-color: rgba(141, 168, 167, 90);"
                           'border-radius: 20px;')
        background_frame.setGraphicsEffect(blur)

        container_layout = QGridLayout(self)
        container_layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)
        container_layout.addWidget(background_frame,0,0)
        container_layout.addWidget(container_frame,0,0)

        self.layout = QVBoxLayout(container_frame)
        self.layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)
        self.layout.setSpacing(12)

        self.title_bar = tBar.Build()
        self.layout.addWidget(self.title_bar)
        
        self.tasks = []

        self.loadData()

        self.reset_pos = 9

    def ImportData(self):
        selected_files = False
        options = QFileDialog.Options()
        file_dialog = QFileDialog()
        file_dialog.setOptions(options)
        username = getpass.getuser()
        file_dialog.setDirectory('C:/Users/' + username +'/Desktop')
        file_dialog.setNameFilter("Swipe Plan Data(*.plan)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()[0]
            dataIE.CDImport(selected_files)
        self.loadData()

    def loadData(self):
        if len(self.tasks) > 0:
            for item in self.tasks:
                self.layout.removeWidget(item)
            self.tasks = []
        try:    self.layout.removeWidget(self.now)
        except:     pass
        try:    self.layout.removeWidget(self.next)
        except:     pass
        self.tasks_data = dataIE.DImport()

        self.all_tasks_data = len(self.tasks_data)
        if self.all_tasks_data == 0:
            self.EmptyTasks()
        else:
            self.now = tskCreate.NCBox('now', self.tasks_data[0][1])
            self.next = tskCreate.NCBox('next', self.tasks_data[0][1])
            
            self.layout.addWidget(self.now)
        for i in range(10):
            if i < len(self.tasks_data):
                if i == 1 and len(self.tasks_data) > 1:
                    self.layout.addWidget(self.next)
                task = tskCreate.taskBox(self.tasks_data[i][0])
                self.tasks.append(task)
                self.layout.addWidget(task)
                task.installEventFilter(self)
            else:
                break
        self.act_count = 0
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            self.CMousePress(event)
        elif event.type() == QtCore.QEvent.MouseMove:
            self.TaskSlide(event, obj)
        elif event.type() == QtCore.QEvent.MouseButtonRelease:
            self.CMouseRelease(event, obj)
        return super().eventFilter(obj, event)

    def CMousePress(self, event):
        self.clickPos = event.x()
        
    def TaskSlide(self, event, obj):
        obj.move(obj.pos() + 
                                 QtCore.QPoint(event.x(), 0) - 
                                 QtCore.QPoint(self.clickPos, 0))
    def DelTask(self):
        if len(self.tasks) <= 1:
            self.EmptyTasks()
        else:
            if len(self.tasks) == 2:
                self.layout.removeWidget(self.next)
            self.layout.removeWidget(self.tasks[-1])
            self.tasks = self.tasks[:-1]
            self.tasks_data = self.tasks_data[:-1]
            self.all_tasks_data -= 1
            dataIE.DUpdate(self.tasks_data)

    def EmptyTasks(self):
            if len(self.tasks) > 0:
                for item in self.tasks:
                    self.layout.removeWidget(item)
                self.tasks = []
            try:    self.layout.removeWidget(self.now)
            except:     pass
            try:    self.layout.removeWidget(self.next)
            except:     pass
            self.act_count = 0
            task = tskCreate.taskBox('no more tasks')
            self.tasks.append(task)
            self.layout.addWidget(task)
            dataIE.DReset()

    def AddTask(self, text, hour, minute):
        if text != '':
            if hour == '':
                hour = 0
            if minute == '':
                minute = 0

            hour = int(hour)
            minute = int(minute)

            self.tasks_data = dataIE.DImport()
            self.tasks_data.append([text, str(hour*60 + minute)])

            #try: self.layout.removeWidget(self.now)
            #except: pass
            #try: self.layout.removeWidget(self.next)
            #except: pass

            if len(self.tasks) == 1 and self.tasks[0].text() == 'no more tasks':
                    self.layout.removeWidget(self.tasks[0])
                    self.tasks = []
                    self.all_tasks_data = 0
                    self.now = tskCreate.NCBox('now', self.tasks_data[0][1])
                    self.next = tskCreate.NCBox('next', self.tasks_data[0][1])
                    self.layout.addWidget(self.now)
            elif len(self.tasks) == 1:
                self.layout.addWidget(self.next)
                self.next.show()
            task = tskCreate.taskBox(text)
            self.tasks.append(task)
            task.installEventFilter(self)
            
            if (self.all_tasks_data - self.act_count) < 10:
                self.layout.addWidget(task)
            self.all_tasks_data += 1
            
            dataIE.DUpdate(self.tasks_data)

    def CMouseRelease(self, event, obj):
        empty = False
        first = False
        if obj.pos().x() < -300 or obj.pos().x() > 320:

            if obj == self.tasks[0]:
                first = True
            self.layout.removeWidget(obj)
            for i in range(len(self.tasks)):
                if self.tasks[i] == obj:
                    self.tasks_data.pop(i)
            self.tasks.remove(obj)
            self.act_count += 1
            dataIE.DUpdate(self.tasks_data)
            self.all_tasks_data -= 1

            if len(self.tasks) < 1:
                empty = True
                self.EmptyTasks()
            
            elif empty == False:
                if first:
                    self.layout.removeWidget(self.now)
                    self.now = tskCreate.NCBox('now', self.tasks_data[0][1])
                    self.layout.insertWidget(1, self.now)

                    self.layout.removeWidget(self.next)
                    self.next = tskCreate.NCBox('next', self.tasks_data[0][1])
                    self.layout.insertWidget(3, self.next)
                    if len(self.tasks) == 1:
                        if len(self.tasks_data) > 0:
                            self.next.hide()
                            self.layout.removeWidget(self.next)
                elif len(self.tasks) != 1:
                    self.layout.removeWidget(self.now)
                    self.layout.insertWidget(1, self.now)
                    self.layout.removeWidget(self.next)
                    self.layout.insertWidget(3, self.next)
                    
                elif len(self.tasks) == 1:
                        if len(self.tasks_data) > 0:
                            self.layout.removeWidget(self.next)

            if self.all_tasks_data >= 10+self.act_count:
                shift = self.all_tasks_data - len(self.tasks_data)
                task = tskCreate.taskBox(self.tasks_data[10 + self.act_count-1-shift][0])
                self.tasks.append(task)
                self.layout.addWidget(task)
                task.installEventFilter(self)
                
        elif obj.pos().x() != self.reset_pos:
            obj.move( QtCore.QPoint(self.reset_pos, obj.pos().y()))
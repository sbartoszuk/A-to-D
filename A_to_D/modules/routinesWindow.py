#!/usr/bin/env python3

'''module: routinesWindow'''


import getpass
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QEvent
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
try:
    import dataImportExport as dataIE
    import taskCreate as tskCreate
    import dialogWindows as cdWin
except:
    from modules import dataImportExport as dataIE
    from modules import taskCreate as tskCreate
    from modules import dialogWindows as cdWin


class CWindowRoutines(QFrame):

    updated = pyqtSignal(bool)

    def __init__(self):
        super(CWindowRoutines, self).__init__()

        font_1 = QtGui.QFont('Coolvetica Rg', 15)


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

        self.import_btn = QPushButton('import routines')
        self.save_btn = QPushButton('save as routine')

        for button in [self.import_btn, self.save_btn]:
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
            button.setFont(font_1)
            top_but_lay.addWidget(button)
                    
        layout.addSpacerItem(QSpacerItem(10, 30))

        rout_frm = QFrame()
        rout_frm.setStyleSheet('background-color: rgba(141, 168, 167, 90);'
                               'border-radius: 20')
        rout_frm.setFixedHeight(330)
        layout.addWidget(rout_frm, alignment=Qt.AlignHCenter)

        self.rout_layout = QVBoxLayout()
        self.rout_layout.setAlignment(Qt.AlignTop)
        self.rout_layout.setSpacing(12)
        rout_frm.setLayout(self.rout_layout)

        self.import_btn.clicked.connect(self.ImportData)
        self.save_btn.clicked.connect(self.SaveRout)

        self.routines = []
        self.RefreshRouts()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            if obj.objectName() == 'del_btn':
                self.DelRoutine(event, obj)
            if obj.objectName() == 'edit_btn':
                self.EditRoutine(event, obj)
        return super().eventFilter(obj, event)

    def EditRoutine(self, event, obj):
        dialog = cdWin.EnterDialog('enter new name of routine')
        dialog.textEntered.connect(lambda x: self.EditRoutineData(x, obj))
        dialog.exec_()

    def EditRoutineData(self, new_name, obj):
        current_name = obj.parent().text_btn.text()
        obj.parent().text_btn.setText(new_name)
        dataIE.RRename(current_name, new_name)
        
    def DelRoutine(self, event, obj):

        self.del_accepted = False
        
        del_dialog = cdWin.CAcceptDialog('are you sure that you want to delete routine?', 'delete', 'cancel')
        del_dialog.accepted.connect(self.delCheck)
        del_dialog.exec_()
        
        
        if self.del_accepted:
            name = obj.parent().text_btn.text()
            dataIE.RDelete(name)
            obj.parent().deleteLater()
            self.routines.remove(obj.parent())
            self.rout_layout.update()
            self.RefreshRouts()

        self.updated.emit(True)
        
    def delCheck(self, result):
            self.del_accepted = result


    def RefreshRouts(self):
        if self.routines != []:
            for item in self.routines:
                try:
                    self.rout_layout.removeWidget(item)
                except: 
                    pass
        self.routines_list = dataIE.RListImport()
        self.routines = []
        if self.routines_list != []:
            
            for routine in self.routines_list:
                temp_rout = tskCreate.routineBox(routine)
                self.routines.append(temp_rout)
            for routine in self.routines:
                routine.del_btn.installEventFilter(self)
                routine.edit_btn.installEventFilter(self)
                self.rout_layout.addWidget(routine)
        elif self.routines_list == []:
            
            temp_rout = tskCreate.routineBox('no saved routines', True)
            self.routines.append(temp_rout)
            self.rout_layout.addWidget(self.routines[0])

    
    def RoutQuanCheck(self):
        num = len(dataIE.RListImport())
        if num <= 4:
            return True
        else:
            pop_up = cdWin.OkDialog('you can add only 5 routines')
            pop_up.exec_()
            return False

    def SaveRout(self):
        if self.RoutQuanCheck():
            dataIE.RDSave()
            self.RefreshRouts()
            self.updated.emit(True)

    def ImportData(self):
        if self.RoutQuanCheck():
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
                dataIE.RDImport(selected_files)
            
            self.RefreshRouts()
            self.updated.emit(True)
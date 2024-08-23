#!/usr/bin/env python3

'''module: dataImportExport'''

import os
import shutil

if os.path.exists('../data'):
    path = os.path.abspath('../data/data.plan')
    rout_path = os.path.abspath('../data/routines')
else:
    path = os.path.abspath('data/data.plan')
    rout_path = os.path.abspath('data/routines')

path = path.replace('\\', '/')
rout_path = rout_path.replace('\\', '/')

def DImport():
    with open(path, 'r', encoding='utf-8') as file:
        all_data = file.read().split('\n')
    text_dat = []
    
    if all_data[0] != '':
        for line in all_data:
            temp_line = line.split(';')
            text_dat.append(temp_line)
    return text_dat

def RDelete(routine):
    os.remove(rout_path + '/' + routine + '.plan')

def RListImport():
    rout_list = []
    temp_list = os.listdir(rout_path)
    
    for item in temp_list:
        temp_item = item.split('.')
        name, extension = temp_item[0], temp_item[1]
        if extension == 'plan':
            rout_list.append(name)
    
    return rout_list

def RListCheck(name):
    temp_list = os.listdir(rout_path)
    for item in temp_list:
        temp_item = item.split('.')
        temp_item = temp_item[0]
        if name == temp_item:
            return False
    return True

def CDImport(selected_file):
    if selected_file != path:
        shutil.copy2(selected_file, path)
def RDImport(selected_file):
    file_name = selected_file.split('/')
    file_name = file_name[-1]
    if selected_file != rout_path + '/' + file_name:
        shutil.copy2(selected_file, rout_path + '/' + file_name)

    with open(path, 'r') as file:
        print(file.read())

def DSaveAs(selected_file):
    shutil.copy2(path, selected_file)

def DReset():
    with open(path, 'w', encoding='utf-8') as file:
        file.write('')
        
def RDSave():
    shutil.copy2(path, rout_path + '/saved_routine.plan')

def DUpdate(tasks):
    with open(path, 'w', encoding='utf-8') as file:
        file.write('')
    with open(path, 'a', encoding='utf-8') as file:
        for i, task in enumerate(tasks):
            file.write(';'.join(task))
            if i != len(tasks)-1:
                file.write('\n')

def RRename(old_name, new_name):
    os.rename(rout_path + '/' + old_name + '.plan', rout_path + '/' + new_name + '.plan')

def RLoadToData(name):
    name = '/' + name + '.plan'
    shutil.copy2(rout_path + name, path)
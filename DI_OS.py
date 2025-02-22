# -*- coding: utf-8 -*-

from windows import *
import csv

OS = None

while len(see_rows()) < 1:
    OS = OperatingSystem()
    welcome(OS)

def pick_logins():
    with open('csv_info/login.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for column, row in enumerate(reader):
            if column == 0:
                OS.U___.append(row[0])
                OS.P___.append(row[1])
            if column == 1:
                OS.U___.append(row[0])
                OS.P___.append(row[1])
            if column == 2:
                OS.U___.append(row[0])
                OS.P___.append(row[1])
            if column == 3:
                OS.U___.append(row[0])
                OS.P___.append(row[1])
            if column == 4:
                OS.U___.append(row[0])
                OS.P___.append(row[1])

while True:
    if len(see_rows()) > 0:
        if not OS:
            OS = OperatingSystem()
        pick_logins()
        login(OS)
    elif len(see_rows()) == 0:
        break

    if OS.U_home >= 0:
        exit()
    else:
        OS = None
        pass

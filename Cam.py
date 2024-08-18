import pyautogui
import PySimpleGUI as sg
import cv2
import numpy as np
import os
from win32api import GetSystemMetrics
import tkinter as tk
from tkinter import simpledialog
import mysql.connector
import sys

screenSize = (GetSystemMetrics(0), GetSystemMetrics(1))

def AddRecord(Name):
    con = mysql.connector.connect(host="localhost", user="root", passwd="Admin")
    cur = con.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS Images")
    cur.execute("USE Images")
    cur.execute("CREATE TABLE IF NOT EXISTS Imgs(ImageName VARCHAR(40))")
    sql = "INSERT INTO Imgs VALUES('%s')"%(Name)
    cur.execute(sql)
    con.commit()

def main():
    sg.theme('Black')

    layout = [[sg.Text('Camera', size=(GetSystemMetrics(0), 1), justification='center', font='Helvetica 20')],
              [sg.Image(filename='', key='image')],
              [sg.Button('Start', size=(GetSystemMetrics(0), 1), font='Arial 14')],
              [sg.Button('Stop', size=(GetSystemMetrics(0), 1), font='Arial 14')],
              [sg.Button('Exit', size=(GetSystemMetrics(0), 1), font='Arial 14')],
              [sg.Button('Screenshot', size=(GetSystemMetrics(0), 1), font='Arial 14')]]

    window = sg.Window('Camera app', layout, location=(0, 0), size=screenSize)

    cap = cv2.VideoCapture(0)
    recording = False
    cap.set(3, GetSystemMetrics(0)/2)
    cap.set(4, GetSystemMetrics(1)/2)

    while True:
        event, values = window.read(timeout=20)

        if event == 'Start':
            recording = True

        elif event == 'Screenshot':
            myScreenshot = pyautogui.screenshot()
            imgName = simpledialog.askstring(title="YourName", prompt="Enter your name: ")
            path = 'images' + '\\' + imgName + '.jpg'
            myScreenshot.save(path)
            AddRecord(imgName)

        elif event == 'Stop':
            recording = False
            img = np.full((480, 640), 255)
            imgbytes = cv2.imencode('.png', img)[1].tobytes()
            window['image'].update(data=imgbytes)

        elif recording:
            ret, frame = cap.read()
            imgbytes = cv2.imencode('.png', frame)[1].tobytes()
            window['image'].update(data=imgbytes)

        elif event == 'Exit' or event == sg.WIN_CLOSED:
            os.system("TASKKILL /F /IM python.exe")
            break

main()

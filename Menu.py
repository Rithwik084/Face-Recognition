import PySimpleGUI as sg
import os
from win32api import GetSystemMetrics

Bsize = int(GetSystemMetrics(0))

def mainProgram():
    sg.theme('DarkAmber')
    layout = [[sg.Text("PROJECT FACIAL RECOGNITION", size=(GetSystemMetrics(0),5), justification = 'center', font = 'Helvetica 20')],
              [sg.Image(filename='',key='image')],
              [sg.Button('INSERT A NEW RECORD' , size=(Bsize, 1), font='Arial 14')],
              [sg.Button('MANAGE RECORDS' , size=(Bsize, 1) , font='Arial 14')],
              [sg.Button('START RECORDING' , size=(Bsize, 1) , font='Arial 14')],
              [sg.Button('EXIT' , size=(Bsize, 1) , font='Arial 14')]]
    window = sg.Window('CS PROJECT Face-Recognizer', layout, location=(0, 0), size=(GetSystemMetrics(0),GetSystemMetrics(1)))

    while True:
        
            event, values = window.read(timeout=20)

            if event == 'EXIT' or event == sg.WIN_CLOSED:
                window.close()
                break

            elif event == 'INSERT A NEW RECORD':
                os.system('python Cam.py')

            elif event == 'START RECORDING':
                os.system('python FR.py')

            elif event == 'MANAGE RECORDS':
                os.system('python Record.py')
            

mainProgram()

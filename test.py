from traceback import clear_frames
import PySimpleGUI as sg

#Veribals for input
#x = sg.InputText()
#y = sg.InputText()

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1'), sg.InputText() ],
            [sg.Text('Enter something on Row 2'), sg.InputText() ],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Pc Reapair forms', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, InputL = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered', InputL[0] , 'and' , InputL[1])

window.close()
import calendar
from datetime import date
from subprocess import call
from traceback import clear_frames
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import CalendarButton

#Veribals for input
#x = sg.InputText()
#y = sg.InputText()

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Image('workshop logo.png')],
            [sg.CalendarButton(button_text=('Choose Date'), format=('%d/%m/%Y') , target=('-CAL-')) , 
                sg.InputText( key=('-CAL-') )],
            [sg.Image('pngwing.com1.png' ) , sg.Text('Contact Detail:'), sg.InputText() ],
            [sg.Text('               Name of contact person') , sg.InputText() ],
            [sg.Text('Enter something on Row 2'), sg.InputText() ],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Pc Reapair forms', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, InputL = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered', InputL[2] , 'and' , InputL[3] , InputL[4] )#Images counts to number of inputs. this is only the Text inputs
    print('The date is:' , )

window.close()
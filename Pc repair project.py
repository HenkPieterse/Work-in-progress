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
#x = sg.popup_get_date(title=('Choose Date'))
# All the stuff inside your window.
layout = [  [sg.Image('images/workshop logo.png')],
            [sg.In(key='-CAL-', visible=True, readonly=True) , sg.CalendarButton(button_text=('Choose Date') , format=('%d/%m/%Y') , target=('-CAL-')) , 
                ],#sg.InputText( key=('-CAL-') ) ],
            [sg.Text('Job number:'), sg.InputText() ],
            [sg.Image('images/pngwing.com1.png' ) , sg.Text('Contact Detail:'), sg.InputText() ],
            [sg.Text('               Name of contact person') , sg.InputText() ],
            [sg.Text('Repair detail:'), sg.InputText() ],
            [sg.Text('Action taken on repair:') , sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Pc Reapair forms' , layout , icon=('lh_logo_new1.png') )
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, InputL = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered', InputL[1] , 'and' , InputL[3] , InputL[4] , InputL[5] , InputL[6] )#Images counts to number of inputs. this is only the Text inputs
    #print('The date is:' , x )



window.close()

import PySimpleGUI as sg

sg.theme('DarkBrown5')


class Logs:

    def cik(x):
        return x*33

    layout=[[sg.T('Persistent window')],
        [sg.I(key='-IN-')],
        [sg.T(key='-OUT-')],
        [sg.B('Read'), sg.B('Write'), sg.Exit()]]

    window=sg.Window('Window that stays open', layout)

    while True:
        event, values=window.read()
    #print(event, values)
        if event==sg.WIN_CLOSED or event == 'Exit':
            break
        if event=='Write':
            rez=cik(float(values['-IN-']))

            window['-OUT-'].update(value=round(rez,2))

    window.close()
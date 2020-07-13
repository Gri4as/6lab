import PySimpleGUI as py
import os
import datetime

def get_result(device) -> list:
    files = os.listdir('logs/')
    result = []
    path = py.popup_get_folder('Choose logs path')
    for x in files:
        with open(path + '/' + x, 'r', encoding='utf-8') as file:
            i = file.readlines()
            for k in range(len(i)):
                i[k] = i[k].rstrip('\n')
            l = 0
            while (l<len(i)):
                if i[l] == '' or 'garbage' in i[l]:
                    del i[l]
                else:
                    l += 1
            for k in i:
                k = k.split(':')
                if k[1] == device:
                    dat = x[5:15].split('-')
                    dat = [int(a) for a in dat]
                    dat = datetime.datetime(dat[0], dat[1], dat[2], )
                    result.append(dat.strftime("%A, %d %B, %Y") + ', ' + ':'.join(x[16:21].split('-')) + ' - ' + k[2])
    return result

layout = [[py.Text('Name:'), py.InputText(key='name'), py.Button('OK')]]
wind = py.Window('Log check', layout)

while True:
    event, data = wind.read()
    if event == 'OK':
        py.popup_scrolled('\n'.join(get_result(data['name'])), title='Result')
    else:
        break
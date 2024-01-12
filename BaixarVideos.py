import PySimpleGUI as sg
from pytube import YouTube

sg.theme('Dark blue 16')

interface = [

    [sg.Titlebar("YOUTUBE DOWNLOAD", None, "red", "white")],
    [sg.Text('URL')],
    [sg.Input(size=(70, 15), key='url')],
    [sg.Button("download")]

]

janela = sg.Window('window', interface)

while True:
    evento, valor = janela.read()

    if valor == sg.WIN_CLOSED:
        break

    if evento == "download":
        link = janela["url"].get()
        video = YouTube(link)
        stream = video.streams.get_highest_resolution().download()
    print('Download realizado com sucesso!')
janela.close()

exit()


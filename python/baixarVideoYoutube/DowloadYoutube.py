import PySimpleGUI as sg
from pytube import YouTube

def executarDownload(link, path):
    video = YouTube(link)
    video.streams.get_highest_resolution().download(output_path=path)


layout = [[sg.Text("link para Download do vídeo"), sg.InputText('')],
          [sg.Text("Escolha a pasta para salvar"), sg.InputText(''),sg.FolderBrowse()],
          [sg.Button('Baixar'), sg.Button('Cancelar')]
          ]
janela = sg.Window("DownLoadYouTube", layout)

while True:
    event, values = janela.read()
    if event == 'Cancelar' or event == sg.WIN_CLOSED:
        break
    elif event == 'Baixar':
        executarDownload(values[0], values[1])
        sg.popup_ok("Video baixado com sucesso")
janela.close()

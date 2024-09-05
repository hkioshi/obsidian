import PySimpleGUI as sg
from PIL import Im

layout = [
    [sg.Menu([['Arquivo', ['Abrir', 'Fechar']], ['Ajuda', ['Sobre']]])],
    [sg.Image(key='-IMAGE-', size=(800, 600))],
]

window = sg.Window('Menu e Get File', layout, resizable=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Fechar':
        break
    elif event == 'Abrir':
        file_path = sg.popup_get_file('Selecione uma imagem', file_types=(("Imagens", "*.jpg *.png"),))
        if file_path:
            window['-IMAGE-'].update(filename=file_path)
    elif event == 'Sobre':
        sg.popup('Desenvolvido pelo BCC - 6 semestre.\n\n Thyago Quintas.')

window. Close()
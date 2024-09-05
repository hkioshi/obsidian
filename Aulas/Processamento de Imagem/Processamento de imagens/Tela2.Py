import PySimpleGUI as sg
from PIL import Image
import io

def resize_image(image_path):
    img = Image.open(image_path)
    img = img.resize((800, 600), Image.Resampling.LANCZOS) 
    return img

layout = [
    [sg.Menu([['Arquivo', ['Abrir', 'Fechar']], ['Ajuda', ['Sobre']]])],
    [sg.Image(key='-IMAGE-', size=(800, 600))],
]

window = sg.Window('Foto Shopping', layout, resizable=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Fechar':
        break
    elif event == 'Abrir':
        file_path = sg.popup_get_file('Selecione uma imagem', file_types=(("Imagens", "*.jpg *.png"),))
        if file_path:
            resized_img = resize_image(file_path)

            #Converte a imagem PIL para o formato que o PySimpleGUI
            img_bytes = io.BytesIO() #Permite criar objetos semelhantes a arquivos na memória RAM
            resized_img.save(img_bytes, format='PNG')
            window['-IMAGE-'].update(data=img_bytes.getvalue())

    elif event == 'Sobre':
        sg.popup('Desenvolvido pelo BCC - 6 semestre.\n\n Thyago Quintas.')

window.close()
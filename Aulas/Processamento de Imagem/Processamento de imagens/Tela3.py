import PySimpleGUI as sg
from PIL import Image
import io
import os

image_atual = None
image_path = None

def resize_image(img):
    maxW = window.size[0]
    width, height = img.size
    aspect_ratio = width/height
    novaLargura = maxW
    novaAltura = int(maxW / aspect_ratio)
    img = img.resize((novaLargura, novaAltura), Image.Resampling.LANCZOS) 
    return img

def metade(img):
    width, height = img.size
    
    
    width = int(width/2)
    height = int(height/2)  
    

    img = img.resize((width, height), Image.Resampling.LANCZOS) 
    img_bytes = io.BytesIO() #Permite criar objetos semelhantes a arquivos na memória RAM
    img.save(img_bytes, format='PNG')

    window['-IMAGE-'].update(data=img_bytes.getvalue())

def negativo():
    width, height = image_atual.size
    pixels = image_atual.load()
    previous_state = image_atual.copy()

    for w in range(width):
        for h in range(height):
            r,g,b = image_atual.getpixel((w,h))
            r = r - 50
            g = g - 50
            b = b - 50

            if(b > 255):
                b = 255
            if(r > 255):
                r = 255    
            if(g > 255):
                g = 255

            if(b < 0):
                b = 0
            if(r < 0):
                r = 0    
            if(g < 0):
                g = 0
            pixels[w,h] = (r,g,b)

            
    img_bytes = io.BytesIO() #Permite criar objetos semelhantes a arquivos na memória RAM
    image_atual.save(img_bytes, format='PNG')
    window['-IMAGE-'].update(data=img_bytes.getvalue())

def cinza():
        if image_atual:
            width, height = image_atual.size
            pixels = image_atual.load()
            previous_state = image_atual.copy()

            for w in range(width):
                for h in range(height):
                    r,g,b = image_atual.getpixel((w,h))
                    gray = int(0.3 *r + 0.6 * g + 0.1 *b)
                    pixels[w,h] = (gray,gray,gray)
        resized_img = resize_image(image_atual)
        img_bytes = io.BytesIO() #Permite criar objetos semelhantes a arquivos na memória RAM
        resized_img.save(img_bytes, format='PNG')
        window['-IMAGE-'].update(data=img_bytes.getvalue())

def open_image(filename):
    global image_atual
    global image_path
    image_path = filename
    image_atual = Image.open(filename)    
    
    resized_img = resize_image(image_atual)
    
    #Converte a image PIL para o formato que o PySimpleGUI
    img_bytes = io.BytesIO() #Permite criar objetos semelhantes a arquivos na memória RAM
    resized_img.save(img_bytes, format='PNG')
    window['-IMAGE-'].update(data=img_bytes.getvalue())


def save_image(filename):
    global image_path
    if image_path:
        image_atual = Image.open(image_path)
        with open(filename, 'wb') as file:
            image_atual.save(file)

def info_image():
    global image_atual
    global image_path
    if image_atual:
        largura, altura = image_atual.size
        formato = image_atual.format
        tamanho_bytes = os.path.getsize(image_path)
        tamanho_mb = tamanho_bytes / (1024 * 1024)
        sg.popup(f"Tamanho: {largura} x {altura}\nFormato: {formato}\nTamanho em MB: {tamanho_mb:.2f}")

layout = [
    [sg.Menu([
            ['Arquivo', ['Abrir', 'Salvar', 'Fechar']],
            ['Sobre a image', ['Informacoes', 'Preto', 'metade', 'negativo']], 
            ['Sobre', ['Desenvolvedor']],

        ])],
    [sg.Image(key='-IMAGE-', size=(800, 600))],
]

window = sg.Window('Aplicativo de image', layout)

while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, 'Fechar'):
        break
    elif event == 'Abrir':
        arquivo = sg.popup_get_file('Selecionar image', file_types=(("Imagens", "*.png;*.jpg;*.jpeg;*.gif"),))
        if arquivo:
            open_image(arquivo)
    elif event == 'Salvar':
        if image_atual:
            arquivo = sg.popup_get_file('Salvar image como', save_as=True, file_types=(("Imagens", "*.png;*.jpg;*.jpeg;*.gif"),))
            if arquivo:
                save_image(arquivo)
    elif event == 'Informacoes':
        info_image()
    elif event == 'Desenvolvedor':
        sg.popup('Desenvolvido por [Seu Nome] - BCC 6º Semestre')
    elif event == 'Preto':
        cinza()
        resize_image(image_atual)
    elif event == 'metade':
        metade(image_atual)
    elif event == 'negativo':
        negativo()
window.close()
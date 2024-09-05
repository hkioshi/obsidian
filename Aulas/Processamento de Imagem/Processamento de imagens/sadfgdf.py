import PySimpleGUI as sg
from PIL import Image, ImageFilter, ExifTags, ImageDraw
import io
import os
import webbrowser
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

image_atual = None
previous_state = None
image_path = None
max_width = 500
max_height = 500
width_reduction = None
height_reduction = None


#Trabalhando com seleção
selecting = False
start_x, start_y = 0, 0
end_x, end_y = 0, 0

def url_download(url):
    global image_atual
    global previous_state
    try:
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            previous_state = image_atual.copy()
            image_atual = Image.open(io.BytesIO(r.content))
            show_image()
        else:
            sg.popup("Falha ao baixar a imagem. Verifique a URL e tente novamente.")
    except Exception as e:
        sg.popup(f"Erro ao baixar a imagem: {str(e)}")

def show_image():
    global image_atual
    try:
        resized_img = resize_image(image_atual)
        #Converte a image PIL para o formato que o PySimpleGUI
        img_bytes = io.BytesIO() #Permite criar objetos semelhantes a arquivos na memÃ³ria RAM
        resized_img.save(img_bytes, format='PNG')
        window['-IMAGE-'].draw_image(data=img_bytes.getvalue(), location=(0,400))
    except Exception as e:
        sg.popup(f"Erro ao exibir a imagem: {str(e)}")

def resize_image(img):
    global max_width
    global max_height
    global width_reduction
    global height_reduction
    
    try:
        width, height = img.size
        aspect_ratio = width / height

        new_width = max_width
        new_height = int(max_width / aspect_ratio)
        img = img.resize((new_width, new_height), Image.LANCZOS)

        new_height = max_height
        new_width = int(max_height * aspect_ratio)
        img = img.resize((new_width, new_height), Image.LANCZOS)

        #Calcula a redução da imagem
        width_reduction = width/new_width
        height_reduction = height/new_height

        return img

    except Exception as e:
        sg.popup(f"Erro ao redimensionar a imagem: {str(e)}")

def open_image(filename):
    global image_atual
    global image_path
    try:
        image_path = filename
        image_atual = Image.open(filename)    
        show_image()
    except Exception as e:
        sg.popup(f"Erro ao abrir a imagem: {str(e)}")

def undo():
    global image_atual
    global previous_state
    if previous_state:
        image_atual = previous_state.copy()
        show_image()
        previous_state = None
    else:
        sg.popup("Nada para desfazer.")

def save_image(filename):
    global image_atual
    try:
        if image_atual:
            with open(filename, 'wb') as file:
                image_atual.save(file)
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao salvar a imagem: {str(e)}")

def info_image():
    global image_atual
    global image_path
    try:
        if image_atual:
            largura, altura = image_atual.size
            formato = image_atual.format
            tamanho_bytes = os.path.getsize(image_path)
            tamanho_mb = tamanho_bytes / (1024 * 1024)
            sg.popup(f"Tamanho: {largura} x {altura}\nFormato: {formato}\nTamanho em MB: {tamanho_mb:.2f}")
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao exibir informações da imagem: {str(e)}")

def exif_data():
    global image_atual
    try:
        if image_atual:
            exif = image_atual._getexif() 
            if exif:
                exif_data = ""
                for tag, value in exif.items():
                    if tag in ExifTags.TAGS:
                        if tag == 37500 or tag == 34853: #Remove os dados customizados (37500) e de GPS (34853)
                            continue
                        tag_name = ExifTags.TAGS[tag]
                        exif_data += f"{tag_name}: {value}\n"
                sg.popup("Dados EXIF:", exif_data)
            else:
                sg.popup("A imagem não possui dados EXIF.")
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao ler dados EXIF: {str(e)}")

def gps_data():
    global image_atual
    try:
        if image_atual:
            exif = image_atual._getexif()
            if exif:
                gps_info = exif.get(34853)  #Tag para informações de GPS
                print (gps_info[1], gps_info[3])
                if gps_info:
                    latitude = int(gps_info[2][0]) + int(gps_info[2][1]) / 60 + int(gps_info[2][2]) / 3600
                    if gps_info[1] == 'S':  #Verifica se a direção é 'S' (sul)
                        latitude = -latitude
                    longitude = int(gps_info[4][0]) + int(gps_info[4][1]) / 60 + int(gps_info[4][2]) / 3600
                    if gps_info[3] == 'W':  #Verifica se a direção é 'W' (oeste)
                        longitude = -longitude
                    sg.popup(f"Latitude: {latitude:.6f}\nLongitude: {longitude:.6f}")
                    open_in_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
                    if sg.popup_yes_no("Deseja abrir no Google Maps?") == "Yes":
                        webbrowser.open(open_in_maps_url)
                else:
                    sg.popup("A imagem não possui informações de GPS.")
            else:
                sg.popup("A imagem não possui dados EXIF.")
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao ler dados de GPS: {str(e)}")

def rotate_image(degrees):
    global image_atual
    global previous_state
    try:
        if image_atual:
            previous_state = image_atual.copy()
            image_atual = image_atual.rotate(degrees, expand=True)
            show_image()
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao girar a imagem: {str(e)}")

def apply_grayscale_filter():
    global image_atual
    global previous_state
    try:
        if image_atual:
            width, height = image_atual.size
            pixels = image_atual.load()
            previous_state = image_atual.copy()

            for w in range(width):
                for h in range(height):
                    r, g, b = image_atual.getpixel((w, h))
                    gray = int(0.3 * r + 0.6 * g + 0.1 * b)
                    pixels[w, h] = (gray, gray, gray)
            
            show_image()
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao aplicar o filtro de escala de cinza: {str(e)}")

def apply_sepia_filter():
    global image_atual
    global previous_state
    try:
        if image_atual:
            width, height = image_atual.size
            pixels = image_atual.load()
            previous_state = image_atual.copy()

            for w in range(width):
                for h in range(height):
                    r, g, b = image_atual.getpixel((w, h))
                    gray = int(0.3 * r + 0.6 * g + 0.1 * b)
                    r = gray + 100
                    g = gray + 50
                    b = gray

                    if r > 255:
                        r = 255
                    if g > 255:
                        g = 255
                    if b > 255:
                        b = 255

                    pixels[w, h] = (r, g, b)
            
            show_image()
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao aplicar o filtro sépia: {str(e)}")

def apply_negative_filter():
    global image_atual
    global previous_state
    try:
        if image_atual:
            width, height = image_atual.size
            pixels = image_atual.load()
            previous_state = image_atual.copy()

            for w in range(width):
                for h in range(height):
                    r, g, b = image_atual.getpixel((w, h))
                    r = 255 - r
                    g = 255 - g
                    b = 255 - b

                    pixels[w, h] = (r, g, b)
            
            show_image()
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao aplicar o filtro negativo: {str(e)}")

def apply_four_bits_filter():
    global image_atual
    global previous_state
    try:
        if image_atual:
            previous_state = image_atual.copy()
            image_atual = image_atual.convert("P", palette="Image.ADAPTIVE", colors=4)
            show_image()
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao aplicar o filtro de 4 bits: {str(e)}")

def apply_blur_filter():
    global image_atual
    global previous_state

    radius = sg.popup_get_text("Digite a quantidade de Blur (0 a 20):", default_text="2")
    try:
        radius = int(radius)
        radius = max(0, min(20, radius))
    except ValueError:
        sg.popup("Por favor, insira um valor numérico válido.")
        return
    
    try:
        if image_atual:
            previous_state = image_atual.copy()
            image_atual = image_atual.filter(ImageFilter.GaussianBlur(radius))
            show_image()
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao aplicar o filtro de desfoque: {str(e)}")

def apply_contour_filter():
    global image_atual
    global previous_state
    try:
        if image_atual:
            previous_state = image_atual.copy()
            image_atual = image_atual.filter(ImageFilter.CONTOUR)
            show_image()
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao aplicar o filtro de contorno: {str(e)}")

def apply_detail_filter():
    global image_atual
    global previous_state
    try:
        if image_atual:
            previous_state = image_atual.copy()
            image_atual = image_atual.filter(ImageFilter.DETAIL)
            show_image()
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao aplicar o filtro de detalhe: {str(e)}")

def apply_edge_enhance_filter():
    global image_atual
    global previous_state
    try:
        if image_atual:
            previous_state = image_atual.copy()
            image_atual = image_atual.filter(ImageFilter.EDGE_ENHANCE)
            show_image()
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao aplicar o filtro de realce de bordas: {str(e)}")

def apply_emboss_filter():
    global image_atual
    global previous_state
    try:
        if image_atual:
            previous_state = image_atual.copy()
            image_atual = image_atual.filter(ImageFilter.EMBOSS)
            show_image()
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao aplicar o filtro de relevo: {str(e)}")

def apply_find_edges_filter():
    global image_atual
    global previous_state
    try:
        if image_atual:
            previous_state = image_atual.copy()
            image_atual = image_atual.filter(ImageFilter.FIND_EDGES)
            show_image()
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao aplicar o filtro de detectar bordas: {str(e)}")

def apply_sharpen_filter():
    global image_atual
    global previous_state
    try:
        if image_atual:
            previous_state = image_atual.copy()
            image_atual = image_atual.filter(ImageFilter.SHARPEN)
            show_image()
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao aplicar o filtro de nitidez: {str(e)}")

def apply_smooth_filter():
    global image_atual
    global previous_state
    try:
        if image_atual:
            previous_state = image_atual.copy()
            image_atual = image_atual.filter(ImageFilter.SMOOTH)
            show_image()
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao aplicar o filtro de suavizar: {str(e)}")

def apply_minfilter_filter():
    global image_atual
    global previous_state

    size = sg.popup_get_text("Digite a quantidade de filtro (3 a 20):", default_text="3")
    try:
        size = int(size)
        size = max(3, min(20, size))
    except ValueError:
        sg.popup("Por favor, insira um valor numérico válido.")
        return

    try:
        if image_atual:
            previous_state = image_atual.copy()
            image_atual = image_atual.filter(ImageFilter.MinFilter(size=size))
            show_image()
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao aplicar o filtro mínimo: {str(e)}")

def apply_maxfilter_filter():
    global image_atual
    global previous_state

    size = sg.popup_get_text("Digite a quantidade de filtro (3 a 20):", default_text="3")
    try:
        size = int(size)
        size = max(3, min(20, size))
    except ValueError:
        sg.popup("Por favor, insira um valor numérico válido.")
        return

    try:
        if image_atual:
            previous_state = image_atual.copy()
            image_atual = image_atual.filter(ImageFilter.MaxFilter(size=size))
            show_image()
        else:
            sg.popup("Nenhuma imagem aberta.")
    except Exception as e:
        sg.popup(f"Erro ao aplicar o filtro máximo: {str(e)}")

def calculate_histogram(image):
    if image.mode != 'L':
        image = image.convert('L')
    histogram = image.histogram()
    
    return histogram

def show_histogram(image):
    histogram = calculate_histogram(image)
    
    layout = [
        [sg.Canvas(key='-CANVAS-')],
        [sg.Button('Fechar')]
    ]
    
    window = sg.Window('Histograma', layout, finalize=True)
    
    fig, ax = plt.subplots()
    ax.hist(range(256), bins=256, weights=histogram)
    
    canvas_elem = window['-CANVAS-']
    canvas = FigureCanvasTkAgg(fig, canvas_elem.Widget)
    canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
    

def crop_selected_area():
    global image_atual, selecting, width_reduction, height_reduction

    if not selecting:
        x1, y1 = min(start_x, end_x), min(start_y, end_y)
        x2, y2 = max(start_x, end_x), max(start_y, end_y)

        #Área de seleção inválida
        if x1 == x2 or y1 == y2:
            return 

        x1 = int(x1*width_reduction)
        x2 = int(x2*width_reduction)
        y1 = int(y1*height_reduction)
        y2 = int(y2*height_reduction)

        cropped_image = image_atual.crop((x1, y1, x2, y2))
        image_atual = cropped_image
        show_image()

layout = [
    [sg.Menu([
            ['Arquivo', ['Abrir', 'Abrir URL', 'Salvar', 'Fechar']],
            ['Editar', ['Desfazer']],
            ['Imagem', [
                'Girar', ['Girar 90 graus à direita', 'Girar 90 graus à esquerda'], 
                'Filtro', ['Preto e Branco', 'Sépia', 'Negativo', '4 bits', 
                           'Blur', 'Contorno', 'Detalhe', 'Realce de bordas',
                           'Relevo', 'Detectar bordas', 'Nitidez', 'Suavizar',
                           'Filtro mínimo', 'Filtro máximo'],
                'Histograma'
            ]],
            ['EXIF', ['Mostrar dados da imagem', 'Mostrar dados de GPS']], 
            ['Sobre a image', ['Informacoes']], 
            ['Sobre', ['Desenvolvedor']]
        ])],
    [sg.Graph(key='-IMAGE-', canvas_size=(500, 500), change_submits=True, drag_submits=True,graph_bottom_left=(0, 0), graph_top_right=(400, 400))],
]

window = sg.Window('Photo Shopee', layout, finalize=True)

while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, 'Fechar'):
        break
    elif event == 'Abrir':
        arquivo = sg.popup_get_file('Selecionar image', file_types=(("Imagens", "*.png;*.jpg;*.jpeg;*.gif"),))
        if arquivo:
            open_image(arquivo)
    elif event == 'Abrir URL':
        url = sg.popup_get_text("Digite a url")
        if url:
            url_download(url)
    elif event == 'Desfazer':
        undo()
    elif event == 'Salvar':
        if image_atual:
            arquivo = sg.popup_get_file('Salvar image como', save_as=True, file_types=(("Imagens", "*.png;*.jpg;*.jpeg;*.gif"),))
            if arquivo:
                save_image(arquivo)
    elif event == 'Informacoes':
        info_image()
    elif event == 'Mostrar dados da imagem':
        exif_data()
    elif event == 'Mostrar dados de GPS':
        gps_data()
    elif event == 'Girar 90 graus à direita':
        rotate_image(-90)
    elif event == 'Girar 90 graus à esquerda':
        rotate_image(90)
    elif event == 'Preto e Branco':
        apply_grayscale_filter()
    elif event == 'Sépia':
        apply_sepia_filter()
    elif event == 'Negativo':
        apply_negative_filter()
    elif event == '4 bits':
        apply_four_bits_filter()
    elif event == 'Blur':
        apply_blur_filter()
    elif event == 'Contorno':
        apply_contour_filter()
    elif event == 'Detalhe':
        apply_detail_filter()
    elif event == 'Realce de bordas':
        apply_edge_enhance_filter()
    elif event == 'Relevo':
        apply_emboss_filter()
    elif event == 'Detectar bordas':
        apply_find_edges_filter()
    elif event == 'Nitidez':
        apply_sharpen_filter()
    elif event == 'Suavizar':
        apply_smooth_filter()
    elif event == 'Filtro mínimo':
        apply_minfilter_filter()
    elif event == 'Filtro máximo':
        apply_maxfilter_filter()
    elif event == 'Histograma':
        if image_atual:
            show_histogram(image_atual)
        else:
            sg.popup("Nenhuma imagem aberta.")
    elif event == 'Desenvolvedor':
        sg.popup('Desenvolvido por Thyago Quintas - BCC 6º Semestre')
    elif event.startswith('-IMAGE-'):
        if '-IMAGE-' in values and values['-IMAGE-'] is not None:
            if event.endswith('-IMAGE-+UP'):
                selecting = False
                end_x, end_y = values['-IMAGE-']
                end_y = 400 - end_y
                crop_selected_area()
            elif not selecting:
                selecting = True
                start_x, start_y = values['-IMAGE-']
                start_y = 400 - start_y

window.close()
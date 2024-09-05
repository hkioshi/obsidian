import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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


[sg.Graph(key='-IMAGE-', canvas_size=(500, 500), change_submits=True, drag_submits=True,graph_bottom_left=(0, 0), graph_top_right=(400, 400))],


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

x
from PIL import Image as im
import re 
import PySimpleGUI 

image = im.open("Imagens/mc.gif")
#image.show("mc")
image_blur = image.filter(ImageFilter.BLUR)
print(f"tamanhao da imagem: {image.size} \nlocal do arquivo: {image.filename}\nformato: {image.format_description}")



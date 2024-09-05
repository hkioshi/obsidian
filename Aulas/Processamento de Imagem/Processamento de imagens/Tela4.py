from PIL import Image as im
import re 
import PySimpleGUI 

image = im.open("Imagens/IMG_0667.jpeg")
#image.show("mc")
ima = image._getexif()
print(ima)
print(f"tamanhao da imagem: {image.size} \nlocal do arquivo: {image.filename}\nformato: {image.format_description}")



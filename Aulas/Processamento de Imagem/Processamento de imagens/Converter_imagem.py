from PIL import Image as im
import pathlib

def image_converter(i, o):
    image = im.open(i)
    image.save(o)
    original_suffix = pathlib.Path(i).suffix
    new_suffix = pathlib.Path(o).suffix
    print(f"convertendo para {new_suffix}")



image_converter("Imagens/mc.jpg","Imagens/mc.png")
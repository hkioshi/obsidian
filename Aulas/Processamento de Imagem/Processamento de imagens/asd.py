from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_decimal_from_dms(dms, ref):
    degrees, minutes, seconds = dms
    decimal = degrees + minutes / 60.0 + seconds / 3600.0
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal

def get_exif_data(image):
    exif_data = {}
    info = image._getexif()
    if info is not None:
        for tag, value in info.items():
            tag_name = TAGS.get(tag, tag)
            exif_data[tag_name] = value
    return exif_data

def get_gps_info(exif_data):
    gps_info = {}
    if 'GPSInfo' in exif_data:
        for key in exif_data['GPSInfo'].keys():
            name = GPSTAGS.get(key, key)
            gps_info[name] = exif_data['GPSInfo'][key]
    return gps_info

def get_coordinates(gps_info):
    if 'GPSLatitude' in gps_info and 'GPSLongitude' in gps_info:
        lat = get_decimal_from_dms(gps_info['GPSLatitude'], gps_info['GPSLatitudeRef'])
        lon = get_decimal_from_dms(gps_info['GPSLongitude'], gps_info['GPSLongitudeRef'])
        return lat, lon
    return None

# Carrega a imagem
image = Image.open('Imagens/IMG_0667.jpeg')

# Obtém dados EXIF
exif_data = get_exif_data(image)

# Obtém informações de GPS
gps_info = get_gps_info(exif_data)

# Obtém as coordenadas
coordinates = get_coordinates(gps_info)

if coordinates:
    print(f"Latitude: {coordinates[0]}, Longitude: {coordinates[1]}")
else:
    print("Nenhuma coordenada GPS encontrada.")

import os
import requests


def send_image(img_path):
    url = 'http://127.0.0.1:8000/detectar'

    with open(img_path, 'rb') as img:
        name_img = os.path.basename(img_path)
        files = {'imagem': (name_img, img, 'multipart/form-data',)}
        with requests.Session() as s:
            r = s.post(url, files=files)
            if r.status_code == 200:
                print('Total de rostos:', r.json()['total_rostos'])
